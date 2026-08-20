# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderUpdateBuyerParams", "Buyer"]


class OrderUpdateBuyerParams(TypedDict, total=False):
    buyer: Required[Buyer]
    """Buyer fields to merge over the order's current buyer."""


class Buyer(TypedDict, total=False):
    """Buyer fields to merge over the order's current buyer."""

    address1: str

    address2: str

    city: str

    country: str

    email: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    phone: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    province: str
