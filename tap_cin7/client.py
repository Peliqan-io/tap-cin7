"""REST client handling, including CIN7Stream base class."""

import requests
from pathlib import Path
from typing import Any,Callable, Dict, Optional, Union, List, Iterable
import backoff
import time
import json
import singer
import logging
from memoization import cached
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BasicAuthenticator

LOGGER = singer.get_logger()
logging.getLogger('backoff').setLevel(logging.CRITICAL)

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class CIN7Stream(RESTStream):
    """CIN7 stream class."""

    url_base = "https://api.cin7.com/api"

    # OR use a dynamic url_base:
    # @property
    # def url_base(self) -> str:
    #     """Return the API URL root, configurable via tap settings."""
    #     return self.config["api_url"]
    
    
    check_empty_response = True


    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = ""  # Or override `get_next_page_token`.

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
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers
    


    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if previous_token is None:
            # If previous_token is None, we only got the first page so we should request page 2
            return 2

        # Parse response as JSON
        res = response.json()
        if len(res) == 0:
            # If this page was empty, we are done querying
            return None
        
        # time.sleep(1)
        # Else, query next page
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

    

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    
    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row

    def log_backoff_attempt(self, details):
        LOGGER.info("ConnectionFailure detected, triggering backoff: %d try", details.get("tries"))
    
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
                requests.exceptions.TooManyRedirects
            ),
            max_tries=10,
            factor=2,
            max_time=600,
            on_backoff=self.log_backoff_attempt
        )(func)
        return decorator
    