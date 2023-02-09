"""REST client handling, including CIN7Stream base class."""

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Union

import backoff
import requests
import singer
from memoization import cached
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

LOGGER = singer.get_logger()
logging.getLogger("backoff").setLevel(logging.CRITICAL)


class CIN7Stream(RESTStream):
    """CIN7 stream class."""

    url_base = "https://api.cin7.com/api"

    check_empty_response = True

    records_jsonpath = "$[*]"
    next_page_token_jsonpath = ""

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object."""
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("api_key"),
            password=self.config.get("api_password"),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if previous_token is None:
            return 2

        # Parse response as JSON
        res = response.json()
        if len(res) == 0:
            return None
        return previous_token + 1

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token is None:
            params["page"] = 1
        else:
            params["page"] = next_page_token

        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        response_str = json.loads(response.text.replace("\\r", ""))
        yield from extract_jsonpath(self.records_jsonpath, input=response_str)

    def log_backoff_attempt(self, details):
        LOGGER.info(
            "ConnectionFailure detected, triggering backoff: %d try",
            details.get("tries"),
        )

    def request_decorator(self, func: Callable) -> Callable:
        """Instantiate a decorator for handling request failures.

        Developers may override this method to provide custom backoff or retry
        handling.

        Args:
            func: Function to decorate.

        Returns:
            A decorated method.
        """
        decorator: Callable = backoff.on_exception(
            backoff.expo,
            (
                RetriableAPIError,
                FatalAPIError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.TooManyRedirects,
                requests.exceptions.ConnectionError
            ),
            max_tries=10,
            factor=2,
            max_time=600,
            on_backoff=self.log_backoff_attempt,
        )(func)
        return decorator
