# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BuyerParam"]


class BuyerParam(TypedDict, total=False):
    address1: Required[str]

    city: Required[str]

    country: Required[str]

    email: Required[str]

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]

    phone: Required[str]

    postal_code: Required[Annotated[str, PropertyInfo(alias="postalCode")]]

    province: Required[str]

    address2: str
