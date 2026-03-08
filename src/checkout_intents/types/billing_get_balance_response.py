# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["BillingGetBalanceResponse"]


class BillingGetBalanceResponse(BaseModel):
    balance: Money

    drawdown_enabled: bool = FieldInfo(alias="drawdownEnabled")
