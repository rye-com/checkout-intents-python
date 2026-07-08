# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProductSubscribeParams"]


class ProductSubscribeParams(TypedDict, total=False):
    type: Required[Literal["store", "product"]]
    """Scope of the subscription change."""

    url: Required[str]
    """Store or product URL to subscribe or unsubscribe."""
