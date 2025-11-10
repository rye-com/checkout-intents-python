# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["VariantSelectionParam"]


class VariantSelectionParam(TypedDict, total=False):
    label: Required[str]
    """The label of the variant being selected.

    Match this label with what is used on the product page.
    """

    value: Required[Union[str, float]]
    """The value of the variant being selected.

    Match this value with what is used on the product page.
    """
