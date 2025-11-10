# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .._models import BaseModel

__all__ = ["VariantSelection"]


class VariantSelection(BaseModel):
    label: str
    """The label of the variant being selected.

    Match this label with what is used on the product page.
    """

    value: Union[str, float]
    """The value of the variant being selected.

    Match this value with what is used on the product page.
    """
