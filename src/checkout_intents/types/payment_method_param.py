# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentMethodParam", "StripeTokenPaymentMethod", "BasisTheoryPaymentMethod", "NekudaPaymentMethod"]


class StripeTokenPaymentMethod(TypedDict, total=False):
    stripe_token: Required[Annotated[str, PropertyInfo(alias="stripeToken")]]

    type: Required[Literal["stripe_token"]]


class BasisTheoryPaymentMethod(TypedDict, total=False):
    basis_theory_token: Required[Annotated[str, PropertyInfo(alias="basisTheoryToken")]]

    type: Required[Literal["basis_theory_token"]]


class NekudaPaymentMethod(TypedDict, total=False):
    nekuda_user_id: Required[Annotated[str, PropertyInfo(alias="nekudaUserId")]]

    type: Required[Literal["nekuda_token"]]

    nekuda_mandate_data: Annotated[Dict[str, Union[str, float]], PropertyInfo(alias="nekudaMandateData")]
    """Construct a type with a set of properties K of type T"""


PaymentMethodParam: TypeAlias = Union[StripeTokenPaymentMethod, BasisTheoryPaymentMethod, NekudaPaymentMethod]
