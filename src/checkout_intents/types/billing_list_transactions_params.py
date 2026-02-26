# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillingListTransactionsParams"]


class BillingListTransactionsParams(TypedDict, total=False):
    after: str
    """Cursor for forward pagination (transaction ID to start after)"""

    before: str
    """Cursor for backward pagination (transaction ID to end before)"""

    limit: int
    """Maximum number of transactions to return (default 20)"""
