# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ShipmentTracking"]


class ShipmentTracking(BaseModel):
    number: Optional[str] = None

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)

    estimated_delivery_date: Optional[datetime] = FieldInfo(alias="estimatedDeliveryDate", default=None)

    url: Optional[str] = None
