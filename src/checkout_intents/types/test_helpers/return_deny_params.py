# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReturnDenyParams"]


class ReturnDenyParams(TypedDict, total=False):
    note: str

    reason: Literal["final_sale", "return_period_ended", "other"]
    """Defaults to `other`."""
