# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..return_reason import ReturnReason

__all__ = ["ReturnCreateParams", "LineItem"]


class ReturnCreateParams(TypedDict, total=False):
    order_id: Required[Annotated[str, PropertyInfo(alias="orderId")]]
    """Rye order id (`oi_<hex>` / `order_<hex>`) to open the simulated return against."""

    line_items: Annotated[Iterable[LineItem], PropertyInfo(alias="lineItems")]
    """Subset of order line items to return.

    Defaults to every order item at full quantity.
    """

    reason: ReturnReason
    """Defaults to `other` when omitted."""


class LineItem(TypedDict, total=False):
    order_line_item_id: Required[Annotated[str, PropertyInfo(alias="orderLineItemId")]]
    """Order line item id (`oi_<hex>`) to return."""

    quantity: Required[int]
    """Units of this line item to return."""
