# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .._models import BaseModel

__all__ = ["VariantSelection"]


class VariantSelection(BaseModel):
    label: str

    value: Union[str, float]
