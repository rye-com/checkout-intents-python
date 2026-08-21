# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ReturnState"]

ReturnState: TypeAlias = Literal["requested", "requires_action", "processing", "refunded", "denied", "failed"]
