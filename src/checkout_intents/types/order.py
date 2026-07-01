# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Order",
    "Cancellation",
    "CancellationRequestedCancellation",
    "CancellationRequestedCancellationReason",
    "CancellationCompletedCancellation",
    "CancellationCompletedCancellationReason",
    "CancellationDeniedCancellation",
    "CancellationDeniedCancellationDenialReason",
    "CancellationDeniedCancellationReason",
]


class CancellationRequestedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class CancellationRequestedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: CancellationRequestedCancellationReason

    state: Literal["requested"]


class CancellationCompletedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class CancellationCompletedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: CancellationCompletedCancellationReason

    state: Literal["completed"]


class CancellationDeniedCancellationDenialReason(BaseModel):
    code: Literal["other", "already_shipped", "non_cancellable_item", "cancellation_window_expired"]

    message: str


class CancellationDeniedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class CancellationDeniedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    denial_reason: CancellationDeniedCancellationDenialReason = FieldInfo(alias="denialReason")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: CancellationDeniedCancellationReason

    state: Literal["denied"]


Cancellation: TypeAlias = Union[
    CancellationRequestedCancellation, CancellationCompletedCancellation, CancellationDeniedCancellation, None
]


class Order(BaseModel):
    """Represents a completed order.

    Orders are created after a checkout intent reaches
    the `completed` state.
    """

    id: str

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
