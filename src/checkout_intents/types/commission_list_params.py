# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .commission_type import CommissionType
from .commission_status import CommissionStatus

__all__ = ["CommissionListParams"]


class CommissionListParams(TypedDict, total=False):
    after: str
    """Cursor from a previous response's `pageInfo.endCursor`"""

    before: str
    """Cursor from a previous response's `pageInfo.startCursor`"""

    limit: int
    """Maximum number of results to return (default 100)"""

    status: CommissionStatus
    """Lifecycle status of a commission record."""

    type: CommissionType
    """Type of commission earned on an order.

    Canonical definition used by both the API contract and the internal
    `@rye-com/ci-commissions` package.
    """
