# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentMethod", "StripeTokenPaymentMethod", "BasisTheoryPaymentMethod", "NekudaPaymentMethod"]


class StripeTokenPaymentMethod(BaseModel):
    stripe_token: str = FieldInfo(alias="stripeToken")

    type: Literal["stripe_token"]


class BasisTheoryPaymentMethod(BaseModel):
    basis_theory_token: str = FieldInfo(alias="basisTheoryToken")

    type: Literal["basis_theory_token"]


class NekudaPaymentMethod(BaseModel):
    nekuda_user_id: str = FieldInfo(alias="nekudaUserId")

    type: Literal["nekuda_token"]

    nekuda_mandate_data: Optional[Dict[str, Union[str, float]]] = FieldInfo(alias="nekudaMandateData", default=None)
    """Construct a type with a set of properties K of type T"""


PaymentMethod: TypeAlias = Union[StripeTokenPaymentMethod, BasisTheoryPaymentMethod, NekudaPaymentMethod]
