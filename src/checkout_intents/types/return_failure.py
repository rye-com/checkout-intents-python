# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ReturnFailure"]


class ReturnFailure(BaseModel):
    """Details of a failed return."""

    code: Literal["drawdown_credit_failed", "merchant_unreachable", "other"]
    """Machine-readable failure code; switch on this."""

    message: str
    """Human-readable, stable summary of the failure."""
