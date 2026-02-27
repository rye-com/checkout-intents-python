# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .shipment_status import ShipmentStatus

__all__ = ["ShipmentListParams"]


class ShipmentListParams(TypedDict, total=False):
    after: str

    before: str

    ids: SequenceNotStr[str]

    limit: float

    status: List[ShipmentStatus]
