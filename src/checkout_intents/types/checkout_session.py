# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CheckoutSession"]


class CheckoutSession(BaseModel):
    """
    A checkout session represents a hosted checkout form that shoppers can use to complete their purchases.

    Checkout sessions provide a pre-built UI for collecting payment and shipping information, allowing you to quickly integrate checkout functionality without building your own forms.
    """

    url: str
    """URL to send your user to for checkout. This URL is valid for 4 hours."""
