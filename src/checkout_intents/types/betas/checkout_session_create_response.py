# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CheckoutSessionCreateResponse"]


class CheckoutSessionCreateResponse(BaseModel):
    url: str
    """URL to send your user to for checkout."""
