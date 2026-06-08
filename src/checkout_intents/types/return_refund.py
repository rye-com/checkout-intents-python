# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["ReturnRefund"]


class ReturnRefund(BaseModel):
    """A single refund issued against a `refunded` Return."""

    id: str
    """Rye refund id."""

    refunded_at: datetime = FieldInfo(alias="refundedAt")
    """When this refund was reconciled."""

    shopper_refund_total: Money = FieldInfo(alias="shopperRefundTotal")
    """Amount returned to the shopper, in the shopper's presentment currency."""
