# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProductSubscriptionStore"]


class ProductSubscriptionStore(BaseModel):
    domain: str
    """Store domain."""

    subscribed: bool
    """Whether the resolved store is subscribed after the mutation."""

    type: Literal["store"]
    """Scope of the subscription change."""

    url: str
    """Store subscription URL."""
