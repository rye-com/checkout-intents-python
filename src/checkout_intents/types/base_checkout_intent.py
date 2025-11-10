# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .buyer import Buyer
from .._models import BaseModel
from .variant_selection import VariantSelection

__all__ = ["BaseCheckoutIntent"]


class BaseCheckoutIntent(BaseModel):
    id: str

    buyer: Buyer

    created_at: datetime = FieldInfo(alias="createdAt")

    product_url: str = FieldInfo(alias="productUrl")

    quantity: float

    variant_selections: Optional[List[VariantSelection]] = FieldInfo(alias="variantSelections", default=None)
