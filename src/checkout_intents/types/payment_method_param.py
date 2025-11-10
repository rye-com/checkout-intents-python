# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentMethodParam"]


class PaymentMethodParam(TypedDict, total=False):
    stripe_token: Required[Annotated[str, PropertyInfo(alias="stripeToken")]]

    type: Required[Literal["stripe_token"]]
