# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandRetrieveResponse"]


class BrandRetrieveResponse(BaseModel):
    id: str
    """A unique identifier for the brand."""

    marketplace: Literal["AMAZON", "SHOPIFY", "BESTBUY", "UNKNOWN"]
    """Indicates what ecommerce platform the brand uses."""

    supported: bool
    """
    If `false`, then products from this brand cannot be purchased through the Sell
    Anything API.
    """
