# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReturnTimeline"]


class ReturnTimeline(BaseModel):
    """Per-transition timestamps for a Return.

    `requestedAt` is always set; the rest
    fill in as the Return advances and reflect the path it actually took (a
    `denied` Return has `deniedAt` but never `refundedAt`).
    """

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """When the return was requested. Always present."""

    denied_at: Optional[datetime] = FieldInfo(alias="deniedAt", default=None)
    """When the return was denied. Present only on `denied`."""

    failed_at: Optional[datetime] = FieldInfo(alias="failedAt", default=None)
    """When the return failed. Present only on `failed`."""

    refunded_at: Optional[datetime] = FieldInfo(alias="refundedAt", default=None)
    """When the refund was fully reconciled and the Return reached `refunded`."""

    refund_issued_at: Optional[datetime] = FieldInfo(alias="refundIssuedAt", default=None)
    """When the merchant issued the refund on its side."""

    return_approved_at: Optional[datetime] = FieldInfo(alias="returnApprovedAt", default=None)
    """When the merchant approved the return."""
