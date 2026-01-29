# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Money"]


class Money(BaseModel):
    amount_subunits: int = FieldInfo(alias="amountSubunits")

    currency_code: str = FieldInfo(alias="currencyCode")
