# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ShipmentTracking", "DeliveryDate"]


class DeliveryDate(BaseModel):
    estimated: datetime


class ShipmentTracking(BaseModel):
    number: Optional[str] = None

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)

    delivery_date: Optional[DeliveryDate] = FieldInfo(alias="deliveryDate", default=None)

    url: Optional[str] = None
