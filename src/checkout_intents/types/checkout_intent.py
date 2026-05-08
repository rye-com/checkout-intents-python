# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .money import Money
from .offer import Offer
from .._models import BaseModel
from .payment_method import PaymentMethod
from .base_checkout_intent import BaseCheckoutIntent

__all__ = [
    "CheckoutIntent",
    "RetrievingOfferCheckoutIntent",
    "AwaitingConfirmationCheckoutIntent",
    "RequiresActionCheckoutIntent",
    "RequiresActionCheckoutIntentNextAction",
    "RequiresActionCheckoutIntentNextActionX402",
    "PlacingOrderCheckoutIntent",
    "CompletedCheckoutIntent",
    "CompletedCheckoutIntentCommissions",
    "CompletedCheckoutIntentCommissionsItem",
    "FailedCheckoutIntent",
    "FailedCheckoutIntentFailureReason",
]


class RetrievingOfferCheckoutIntent(BaseCheckoutIntent):
    state: Literal["retrieving_offer"]


class AwaitingConfirmationCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    state: Literal["awaiting_confirmation"]

    payment_method: Optional[PaymentMethod] = FieldInfo(alias="paymentMethod", default=None)


class RequiresActionCheckoutIntentNextActionX402(BaseModel):
    currency: Literal["USDC"]

    expires_at: str = FieldInfo(alias="expiresAt")

    max_amount_required: str = FieldInfo(alias="maxAmountRequired")

    network: str

    recipient: str

    scheme: Literal["exact"]


class RequiresActionCheckoutIntentNextAction(BaseModel):
    type: Literal["x402"]

    x402: RequiresActionCheckoutIntentNextActionX402


class RequiresActionCheckoutIntent(BaseCheckoutIntent):
    next_action: RequiresActionCheckoutIntentNextAction = FieldInfo(alias="nextAction")

    offer: Offer

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    state: Literal["requires_action"]


class PlacingOrderCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    state: Literal["placing_order"]


class CompletedCheckoutIntentCommissionsItem(BaseModel):
    id: str

    developer_share_amount: Money = FieldInfo(alias="developerShareAmount")

    gross_amount: Money = FieldInfo(alias="grossAmount")

    settlement_direction: Literal["rye_owes_developer", "developer_owes_rye"] = FieldInfo(alias="settlementDirection")
    """Direction of settlement: who owes whom once the commission is finalized."""

    status: Literal["pending", "confirmed", "updated", "finalized", "refunded", "expired"]
    """Lifecycle status of a commission record."""

    type: Literal["surcharge", "promo_arbitrage", "discount_code", "affiliate", "out_of_band"]
    """Type of commission earned on an order.

    Canonical definition used by both the API contract and the internal
    `@rye-com/ci-commissions` package.
    """


class CompletedCheckoutIntentCommissions(BaseModel):
    count: float

    items: List[CompletedCheckoutIntentCommissionsItem]


class CompletedCheckoutIntent(BaseCheckoutIntent):
    offer: Offer

    order_id: Optional[str] = FieldInfo(alias="orderId", default=None)

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    state: Literal["completed"]

    commissions: Optional[CompletedCheckoutIntentCommissions] = None

    estimated_delivery_date: Optional[datetime] = FieldInfo(alias="estimatedDeliveryDate", default=None)


class FailedCheckoutIntentFailureReason(BaseModel):
    code: Literal[
        "unknown",
        "checkout_intent_expired",
        "payment_failed",
        "payment_cvc_expired",
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
        "promo_code_discovery_not_enabled",
        "product_not_found",
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
    RequiresActionCheckoutIntent,
    PlacingOrderCheckoutIntent,
    CompletedCheckoutIntent,
    FailedCheckoutIntent,
]
