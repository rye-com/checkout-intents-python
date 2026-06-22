# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReturnApproveParams"]


class ReturnApproveParams(TypedDict, total=False):
    next_action: Annotated[Literal["ship_items_to_merchant", "no_action_required"], PropertyInfo(alias="nextAction")]
    """
    `ship_items_to_merchant` lands the return in `requires_action` with a stub
    shipping label; `no_action_required` lands it directly in `processing`. Defaults
    to `ship_items_to_merchant`.
    """
