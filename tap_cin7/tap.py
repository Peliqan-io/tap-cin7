"""CIN7 tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_cin7.streams import (
    ProductStream,
    PurchaseOrdersStream,
    OrderStream,
    StockStream,
    VoucherStream

)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    ProductStream,
    PurchaseOrdersStream,
    OrderStream,
    StockStream,
    VoucherStream
]


class TapCIN7(Tap):
    """CIN7 tap class."""
    name = "tap-cin7"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="api_key"
        ),
        th.Property(
            "api_password",
            th.StringType,
            required=True,
            description="api_password"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


def main():
    TapCIN7.cli()

if __name__ == "__main__":
    main()