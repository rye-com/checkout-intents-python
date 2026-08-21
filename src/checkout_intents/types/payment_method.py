# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PaymentMethod",
    "StripeTokenPaymentMethod",
    "BasisTheoryPaymentMethod",
    "DrawdownPaymentMethod",
    "X402PaymentMethod",
]


class StripeTokenPaymentMethod(BaseModel):
    stripe_token: str = FieldInfo(alias="stripeToken")

    type: Literal["stripe_token"]


class BasisTheoryPaymentMethod(BaseModel):
    basis_theory_token: str = FieldInfo(alias="basisTheoryToken")

    type: Literal["basis_theory_token"]


class DrawdownPaymentMethod(BaseModel):
    type: Literal["drawdown"]


class X402PaymentMethod(BaseModel):
    network: Literal["base", "solana", "tempo"]

    type: Literal["x402"]


PaymentMethod: TypeAlias = Union[
    StripeTokenPaymentMethod, BasisTheoryPaymentMethod, DrawdownPaymentMethod, X402PaymentMethod
]
