# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .buyer_param import BuyerParam
from .payment_method_param import PaymentMethodParam
from .variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutIntentPurchaseParams", "Constraints"]


class CheckoutIntentPurchaseParams(TypedDict, total=False):
    buyer: Required[BuyerParam]

    payment_method: Required[Annotated[PaymentMethodParam, PropertyInfo(alias="paymentMethod")]]

    product_url: Required[Annotated[str, PropertyInfo(alias="productUrl")]]

    quantity: Required[int]

    constraints: Constraints

    promo_codes: Annotated[SequenceNotStr[str], PropertyInfo(alias="promoCodes")]

    variant_selections: Annotated[Iterable[VariantSelectionParam], PropertyInfo(alias="variantSelections")]


class Constraints(TypedDict, total=False):
    max_shipping_price: Annotated[int, PropertyInfo(alias="maxShippingPrice")]

    max_total_price: Annotated[int, PropertyInfo(alias="maxTotalPrice")]

    offer_retrieval_effort: Annotated[Literal["max", "low"], PropertyInfo(alias="offerRetrievalEffort")]
    """Controls how much effort the system should spend retrieving an offer.

    - 'max': Full effort including AI agent fallback (slower, higher success rate)
    - 'low': Fast API-only retrieval, fails if API unavailable (faster, lower
      success rate)

    Default: 'max'
    """
