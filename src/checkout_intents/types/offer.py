# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["Offer", "Cost", "Shipping", "ShippingAvailableOption"]


class Cost(BaseModel):
    subtotal: Money

    total: Money

    discount: Optional[Money] = None

    shipping: Optional[Money] = None

    surcharge: Optional[Money] = None

    tax: Optional[Money] = None


class ShippingAvailableOption(BaseModel):
    id: str

    cost: Money

    discount: Optional[Money] = None


class Shipping(BaseModel):
    available_options: List[ShippingAvailableOption] = FieldInfo(alias="availableOptions")

    selected_option_id: Optional[str] = FieldInfo(alias="selectedOptionId", default=None)


class Offer(BaseModel):
    cost: Cost

    shipping: Shipping

    applied_promo_codes: Optional[List[str]] = FieldInfo(alias="appliedPromoCodes", default=None)
