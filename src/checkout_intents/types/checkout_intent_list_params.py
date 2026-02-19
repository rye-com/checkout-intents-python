# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["CheckoutIntentListParams"]


class CheckoutIntentListParams(TypedDict, total=False):
    id: SequenceNotStr[str]

    after: str

    before: str

    limit: float

    state: List[Literal["retrieving_offer", "awaiting_confirmation", "placing_order", "completed", "failed"]]
