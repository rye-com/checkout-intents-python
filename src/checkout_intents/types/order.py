# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .buyer import Buyer
from .._models import BaseModel
from .cancellation import Cancellation

__all__ = ["Order"]


class Order(BaseModel):
    """Represents a completed order.

    Orders are created after a checkout intent reaches
    the `completed` state.
    """

    id: str

    buyer: Buyer
    """Buyer and shipping-address details captured for this order."""

    cancellation: Optional[Cancellation] = None
    """
    The cancellation for this order, or `null` if none has been requested. Populated
    by joining the separate cancellations collection on the order's marketplace
    order id.
    """

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")
    """ID of the checkout intent that was responsible for creating this order."""

    created_at: str = FieldInfo(alias="createdAt")
    """Timestamp the order was persisted to Rye."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Timestamp the order was last updated at"""

    reference_id: Optional[str] = FieldInfo(alias="referenceId", default=None)
    """
    The `referenceId` you supplied on the checkout intent, echoed back so you can
    reconcile this order against your own records. Absent when none was supplied.
    """
