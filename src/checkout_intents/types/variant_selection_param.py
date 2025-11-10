# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["VariantSelectionParam"]


class VariantSelectionParam(TypedDict, total=False):
    label: Required[str]

    value: Required[Union[str, float]]
