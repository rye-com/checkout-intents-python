# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Buyer"]


class Buyer(BaseModel):
    address1: str

    city: str

    country: str

    email: str

    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")

    phone: str

    postal_code: str = FieldInfo(alias="postalCode")

    province: str

    address2: Optional[str] = None
