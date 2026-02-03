# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["ShipmentListParams"]


class ShipmentListParams(TypedDict, total=False):
    after: str

    before: str

    ids: SequenceNotStr[str]

    limit: float

    status: List[Literal["out_for_delivery", "delivered", "shipped", "canceled", "delayed", "ordered"]]
