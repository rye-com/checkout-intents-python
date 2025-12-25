# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .buyer import Buyer
from .._models import BaseModel
from .variant_selection import VariantSelection

__all__ = ["BaseCheckoutIntent", "Constraints"]


class Constraints(BaseModel):
    max_shipping_price: Optional[int] = FieldInfo(alias="maxShippingPrice", default=None)

    max_total_price: Optional[int] = FieldInfo(alias="maxTotalPrice", default=None)


class BaseCheckoutIntent(BaseModel):
    id: str

    buyer: Buyer

    created_at: datetime = FieldInfo(alias="createdAt")

    product_url: str = FieldInfo(alias="productUrl")

    quantity: float

    constraints: Optional[Constraints] = None

    promo_codes: Optional[List[str]] = FieldInfo(alias="promoCodes", default=None)

    variant_selections: Optional[List[VariantSelection]] = FieldInfo(alias="variantSelections", default=None)
