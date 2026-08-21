# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReturnRefundParams"]


class ReturnRefundParams(TypedDict, total=False):
    cost_bearer: Annotated[Literal["shopper", "developer", "rye"], PropertyInfo(alias="costBearer")]
    """Defaults to `shopper`."""
