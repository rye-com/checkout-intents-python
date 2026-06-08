# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .return_reason import ReturnReason

__all__ = ["ReturnCreateParams"]


class ReturnCreateParams(TypedDict, total=False):
    order_id: Required[Annotated[str, PropertyInfo(alias="orderId")]]
    """Rye order id (`order_<32 hex>`) of the order being returned."""

    reason: Required[ReturnReason]
    """Reason for the return."""
