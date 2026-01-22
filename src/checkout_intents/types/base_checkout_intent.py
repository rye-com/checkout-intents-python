# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .buyer import Buyer
from .._models import BaseModel
from .variant_selection import VariantSelection

__all__ = ["BaseCheckoutIntent", "Constraints"]


class Constraints(BaseModel):
    max_shipping_price: Optional[int] = FieldInfo(alias="maxShippingPrice", default=None)

    max_total_price: Optional[int] = FieldInfo(alias="maxTotalPrice", default=None)

    offer_retrieval_effort: Optional[Literal["max", "low"]] = FieldInfo(alias="offerRetrievalEffort", default=None)
    """Controls how much effort the system should spend retrieving an offer.

    - 'max': Full effort including AI agent fallback (slower, higher success rate)
    - 'low': Fast API-only retrieval, fails if API unavailable (faster, lower
      success rate)

    Default: 'max'
    """


class BaseCheckoutIntent(BaseModel):
    id: str

    buyer: Buyer

    created_at: datetime = FieldInfo(alias="createdAt")

    product_url: str = FieldInfo(alias="productUrl")

    quantity: int

    constraints: Optional[Constraints] = None

    promo_codes: Optional[List[str]] = FieldInfo(alias="promoCodes", default=None)

    variant_selections: Optional[List[VariantSelection]] = FieldInfo(alias="variantSelections", default=None)
