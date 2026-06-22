# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shipment import Shipment

__all__ = ["ShipmentAdvanceResponse"]


class ShipmentAdvanceResponse(BaseModel):
    shipment: Shipment
