# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["Offer", "Cost", "Shipping", "ShippingAvailableOption", "ShippingAvailableOptionDeliveryEstimate"]


class Cost(BaseModel):
    subtotal: Money

    total: Money

    discount: Optional[Money] = None

    shipping: Optional[Money] = None

    surcharge: Optional[Money] = None

    tax: Optional[Money] = None


class ShippingAvailableOptionDeliveryEstimate(BaseModel):
    """Estimated range of dates that items will be delivered in.

    At least one of
    `earliest` or `latest` are guaranteed to be set.

    Interpretation:

    * If both `earliest` and `latest` are set, then the delivery estimate is the range between the two dates.
    * If only `earliest` is set, then the delivery estimate is any date after that date.
    * If only `latest` is set, then the delivery estimate is any date before that date.
    """

    earliest: Optional[datetime] = None
    """Earliest date that items will be delivered by."""

    latest: Optional[datetime] = None
    """Latest date that items will be delivered by."""


class ShippingAvailableOption(BaseModel):
    id: str

    cost: Money

    delivery_estimate: Optional[ShippingAvailableOptionDeliveryEstimate] = FieldInfo(
        alias="deliveryEstimate", default=None
    )
    """Estimated range of dates that items will be delivered in.

    At least one of `earliest` or `latest` are guaranteed to be set.

    Interpretation:

    - If both `earliest` and `latest` are set, then the delivery estimate is the
      range between the two dates.
    - If only `earliest` is set, then the delivery estimate is any date after that
      date.
    - If only `latest` is set, then the delivery estimate is any date before that
      date.
    """

    discount: Optional[Money] = None


class Shipping(BaseModel):
    available_options: List[ShippingAvailableOption] = FieldInfo(alias="availableOptions")

    selected_option_id: Optional[str] = FieldInfo(alias="selectedOptionId", default=None)


class Offer(BaseModel):
    cost: Cost

    shipping: Shipping

    applied_promo_codes: Optional[List[str]] = FieldInfo(alias="appliedPromoCodes", default=None)
