# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Cancellation",
    "RequestedCancellation",
    "RequestedCancellationReason",
    "CompletedCancellation",
    "CompletedCancellationReason",
    "DeniedCancellation",
    "DeniedCancellationDenialReason",
    "DeniedCancellationReason",
]


class RequestedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class RequestedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: RequestedCancellationReason

    state: Literal["requested"]


class CompletedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class CompletedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: CompletedCancellationReason

    state: Literal["completed"]


class DeniedCancellationDenialReason(BaseModel):
    code: Literal["other", "already_shipped", "non_cancellable_item", "cancellation_window_expired"]

    message: str


class DeniedCancellationReason(BaseModel):
    code: Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]

    message: Optional[str] = None
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """


class DeniedCancellation(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    denial_reason: DeniedCancellationDenialReason = FieldInfo(alias="denialReason")

    marketplace_order_id: str = FieldInfo(alias="marketplaceOrderId")

    reason: DeniedCancellationReason

    state: Literal["denied"]


Cancellation: TypeAlias = Union[RequestedCancellation, CompletedCancellation, DeniedCancellation]
