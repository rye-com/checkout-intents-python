# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .buyer_param import BuyerParam
from .payment_method_param import PaymentMethodParam
from .variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutIntentPurchaseParams"]


class CheckoutIntentPurchaseParams(TypedDict, total=False):
    buyer: Required[BuyerParam]

    payment_method: Required[Annotated[PaymentMethodParam, PropertyInfo(alias="paymentMethod")]]

    product_url: Required[Annotated[str, PropertyInfo(alias="productUrl")]]

    quantity: Required[float]

    promo_codes: Annotated[SequenceNotStr[str], PropertyInfo(alias="promoCodes")]

    variant_selections: Annotated[Iterable[VariantSelectionParam], PropertyInfo(alias="variantSelections")]
