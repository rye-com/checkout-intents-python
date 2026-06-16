# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    """Represents a completed order.

    Orders are created after a checkout intent reaches
    the `completed` state.
    """

    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")
    """ID of the checkout intent that was responsible for creating this order."""

    created_at: str = FieldInfo(alias="createdAt")
    """Timestamp the order was persisted to Rye."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Timestamp the order was last updated at"""
