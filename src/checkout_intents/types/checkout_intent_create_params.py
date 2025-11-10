# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .buyer_param import BuyerParam
from .variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutIntentCreateParams"]


class CheckoutIntentCreateParams(TypedDict, total=False):
    buyer: Required[BuyerParam]

    product_url: Required[Annotated[str, PropertyInfo(alias="productUrl")]]

    quantity: Required[float]

    variant_selections: Annotated[Iterable[VariantSelectionParam], PropertyInfo(alias="variantSelections")]
