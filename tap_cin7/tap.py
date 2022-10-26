"""CIN7 tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_cin7.streams import (
    BranchesStream,
    ContactsStream,
    OrderStream,
    ProductStream,
    PurchaseOrdersStream,
    StockStream,
    VoucherStream,
)

STREAM_TYPES = [
    ProductStream,
    PurchaseOrdersStream,
    OrderStream,
    StockStream,
    VoucherStream,
    ContactsStream,
    BranchesStream,
]


class TapCIN7(Tap):
    """CIN7 tap class."""

    name = "tap-cin7"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True, description="api_key"),
        th.Property(
            "api_password", th.StringType, required=True, description="api_password"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapCIN7.cli()
