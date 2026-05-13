# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel
from .commission_type import CommissionType
from .commission_status import CommissionStatus
from .settlement_direction import SettlementDirection

__all__ = ["Commission"]


class Commission(BaseModel):
    """A commission earned (or owed) on a completed checkout intent."""

    id: str
    """Unique identifier for this commission."""

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")
    """The checkout intent this commission was generated from."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Time the commission was first recorded."""

    developer_share_amount: Money = FieldInfo(alias="developerShareAmount")
    """Portion of `grossAmount` allocated to the developer."""

    developer_share_percent: float = FieldInfo(alias="developerSharePercent")
    """Developer's share of `grossAmount` expressed as a percentage (0–100)."""

    gross_amount: Money = FieldInfo(alias="grossAmount")
    """Gross commission amount before splitting between developer and Rye."""

    rye_share_amount: Money = FieldInfo(alias="ryeShareAmount")
    """Portion of `grossAmount` allocated to Rye."""

    settlement_direction: SettlementDirection = FieldInfo(alias="settlementDirection")
    """Whether Rye owes the developer or vice versa once settled."""

    status: CommissionStatus
    """Lifecycle status, e.g. pending, finalized, refunded."""

    type: CommissionType
    """Kind of commission, e.g. surcharge, discount_code, affiliate."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Time the commission last changed (e.g. status transition)."""

    finalized_at: Optional[datetime] = FieldInfo(alias="finalizedAt", default=None)
    """Time the commission moved to a terminal status. Unset until finalized."""
