# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ReturnReason"]

ReturnReason: TypeAlias = Literal[
    "defective",
    "wrong_item",
    "unwanted",
    "color",
    "not_as_described",
    "size_too_large",
    "size_too_small",
    "style",
    "other",
]
