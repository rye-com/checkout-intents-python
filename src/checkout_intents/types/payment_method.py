# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentMethod"]


class PaymentMethod(BaseModel):
    stripe_token: str = FieldInfo(alias="stripeToken")

    type: Literal["stripe_token"]
