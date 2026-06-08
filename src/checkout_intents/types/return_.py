# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .return_state import ReturnState
from .return_denial import ReturnDenial
from .return_reason import ReturnReason
from .return_refund import ReturnRefund
from .return_failure import ReturnFailure
from .return_timeline import ReturnTimeline
from .return_next_action import ReturnNextAction

__all__ = ["Return"]


class Return(BaseModel):
    """A single Return record.

    The `state` discriminator tells you which of
    `denial`, `failure`, and `refunds` is populated; `nextAction` is set once the
    Return is approved (see {@link NextActionResponse}).
    """

    id: str
    """Rye return id (`ret_<32 hex>`)."""

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")
    """Rye checkout intent id that produced the order being returned."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the Return record was created."""

    order_id: str = FieldInfo(alias="orderId")
    """Rye order id (`order_<32 hex>`) this Return was opened against."""

    reason: ReturnReason
    """Reason the return was requested, echoed back from the create call."""

    state: ReturnState
    """Lifecycle state; the discriminator for the optional sub-objects below."""

    timeline: ReturnTimeline
    """Per-transition timestamps; later stamps fill in as the Return advances."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the Return record was last updated."""

    denial: Optional[ReturnDenial] = None
    """Why the merchant declined the return. Present only on `denied`."""

    failure: Optional[ReturnFailure] = None
    """What went wrong. Present only on `failed`."""

    next_action: Optional[ReturnNextAction] = FieldInfo(alias="nextAction", default=None)
    """What the shopper must do next (e.g.

    ship the items back). Present once the return is approved — i.e. on
    `requires_action`, `processing`, and `refunded` — and may be present on `denied`
    / `failed` if they were approved before terminating. Absent on `requested`.
    """

    refunds: Optional[List[ReturnRefund]] = None
    """Issued refunds. Present only on `refunded`."""
