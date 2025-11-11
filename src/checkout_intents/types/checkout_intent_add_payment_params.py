# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .payment_method_param import PaymentMethodParam

__all__ = ["CheckoutIntentAddPaymentParams"]


class CheckoutIntentAddPaymentParams(TypedDict, total=False):
    payment_method: Required[Annotated[PaymentMethodParam, PropertyInfo(alias="paymentMethod")]]
