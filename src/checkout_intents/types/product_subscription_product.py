# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProductSubscriptionProduct"]


class ProductSubscriptionProduct(BaseModel):
    id: str
    """Product id."""

    subscribed: bool
    """Whether the resolved product is subscribed after the mutation."""

    type: Literal["product"]
    """Scope of the subscription change."""

    url: str
    """Product subscription URL."""
