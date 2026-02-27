# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["BillingListTransactionsResponse"]


class BillingListTransactionsResponse(BaseModel):
    id: str

    amount: Money

    created_at: datetime = FieldInfo(alias="createdAt")

    description: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None
    """Construct a type with a set of properties K of type T"""
