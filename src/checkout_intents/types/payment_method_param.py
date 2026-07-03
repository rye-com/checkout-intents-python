# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PaymentMethodParam",
    "StripeTokenPaymentMethod",
    "BasisTheoryPaymentMethod",
    "DrawdownPaymentMethod",
    "X402PaymentMethod",
]


class StripeTokenPaymentMethod(TypedDict, total=False):
    stripe_token: Required[Annotated[str, PropertyInfo(alias="stripeToken")]]

    type: Required[Literal["stripe_token"]]


class BasisTheoryPaymentMethod(TypedDict, total=False):
    basis_theory_token: Required[Annotated[str, PropertyInfo(alias="basisTheoryToken")]]

    type: Required[Literal["basis_theory_token"]]


class DrawdownPaymentMethod(TypedDict, total=False):
    type: Required[Literal["drawdown"]]


class X402PaymentMethod(TypedDict, total=False):
    network: Required[Literal["base", "solana", "tempo"]]

    type: Required[Literal["x402"]]


PaymentMethodParam: TypeAlias = Union[
    StripeTokenPaymentMethod, BasisTheoryPaymentMethod, DrawdownPaymentMethod, X402PaymentMethod
]
