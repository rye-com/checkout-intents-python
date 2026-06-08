# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReturnDenial"]


class ReturnDenial(BaseModel):
    """Why a return was declined by the merchant."""

    reason: Literal["final_sale", "return_period_ended", "other"]
    """Machine-readable decline reason."""

    note: Optional[str] = None
    """Optional human-readable detail from the merchant."""
