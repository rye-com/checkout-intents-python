# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrderCancelParams", "Reason"]


class OrderCancelParams(TypedDict, total=False):
    reason: Required[Reason]


class Reason(TypedDict, total=False):
    code: Required[Literal["requested_by_customer", "fraud", "inventory", "payment_issue", "staff_error", "other"]]

    message: str
    """
    Optional free-text note explaining the cancellation, forwarded to the merchant
    when possible.
    """
