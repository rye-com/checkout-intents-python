# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .offer import Offer
from .._models import BaseModel
from .payment_method import PaymentMethod
from .base_checkout_intent import BaseCheckoutIntent

__all__ = [
    "CheckoutIntent",
    "RetrievingOfferCheckoutIntent",
    "AwaitingConfirmationCheckoutIntent",
    "PlacingOrderCheckoutIntent",
    "CompletedCheckoutIntent",
    "FailedCheckoutIntent",
    "FailedCheckoutIntentFailureReason",
]


class RetrievingOfferCheckoutIntent(BaseCheckoutIntent):
    state: Literal["retrieving_offer"]


class AwaitingConfirmationCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    state: Literal["awaiting_confirmation"]

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)


class PlacingOrderCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    state: Literal["placing_order"]


class CompletedCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    order_id: Optional[str] = FieldInfo(alias="orderId", default=None)

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    state: Literal["completed"]


class FailedCheckoutIntentFailureReason(BaseModel):
    code: Literal[
        "checkout_intent_expired",
        "payment_failed",
        "insufficient_stock",
        "product_out_of_stock",
        "offer_retrieval_failed",
        "order_placement_failed",
        "developer_not_found",
        "missing_shipping_method",
        "unsupported_currency",
        "invalid_input",
        "incorrect_cost_breakdown",
        "unsupported_store_no_guest_checkout",
        "workflow_invocation_failed",
        "variant_selections_invalid",
        "variant_selections_required",
        "form_validation_error",
        "captcha_blocked",
        "bot_protection_blocked",
        "constraint_total_price_exceeded",
        "constraint_shipping_cost_exceeded",
        "unknown",
    ]
    """Type derived from runtime array - always in sync"""

    message: str


class FailedCheckoutIntent(BaseCheckoutIntent):
    failure_reason: FailedCheckoutIntentFailureReason = FieldInfo(alias="failureReason")

    state: Literal["failed"]

    offer: Optional[Offer] = None

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)


CheckoutIntent: TypeAlias = Union[
    RetrievingOfferCheckoutIntent,
    AwaitingConfirmationCheckoutIntent,
    PlacingOrderCheckoutIntent,
    CompletedCheckoutIntent,
    FailedCheckoutIntent,
]
