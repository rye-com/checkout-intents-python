# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shipment_tracking import ShipmentTracking

__all__ = [
    "Shipment",
    "WithStatusBaseShipmentWithTrackingShipped",
    "WithStatusBaseShipmentWithTrackingShippedTrackingEvent",
    "WithStatusBaseShipmentWithTrackingShippedTrackingEventLocation",
    "WithStatusBaseShipmentWithTrackingShippedTrackingEventTimestamp",
    "DeliveredShipment",
    "DeliveredShipmentTrackingEvent",
    "DeliveredShipmentTrackingEventLocation",
    "DeliveredShipmentTrackingEventTimestamp",
    "WithStatusBaseShipmentWithTrackingDelayed",
    "WithStatusBaseShipmentWithTrackingDelayedTrackingEvent",
    "WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation",
    "WithStatusBaseShipmentWithTrackingDelayedTrackingEventTimestamp",
    "WithStatusBaseShipmentWithTrackingOutForDelivery",
    "WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEvent",
    "WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation",
    "WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventTimestamp",
    "WithStatusBaseShipmentOrdered",
    "WithStatusBaseShipmentCanceled",
]


class WithStatusBaseShipmentWithTrackingShippedTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingShippedTrackingEventTimestamp(BaseModel):
    local: str
    """ISO 8601 string with timezone offset, e.g. "2025-02-05T17:02:00.000-05:00" """

    utc: datetime
    """UTC timestamp"""


class WithStatusBaseShipmentWithTrackingShippedTrackingEvent(BaseModel):
    description: Optional[str] = None

    location: WithStatusBaseShipmentWithTrackingShippedTrackingEventLocation

    timestamp: Optional[WithStatusBaseShipmentWithTrackingShippedTrackingEventTimestamp] = None


class WithStatusBaseShipmentWithTrackingShipped(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")
    """
    The external ID is provided by the marketplace and matches the shipment to their
    system.
    """

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["shipped"]

    tracking: ShipmentTracking

    tracking_events: List[WithStatusBaseShipmentWithTrackingShippedTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class DeliveredShipmentTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class DeliveredShipmentTrackingEventTimestamp(BaseModel):
    local: str
    """ISO 8601 string with timezone offset, e.g. "2025-02-05T17:02:00.000-05:00" """

    utc: datetime
    """UTC timestamp"""


class DeliveredShipmentTrackingEvent(BaseModel):
    description: Optional[str] = None

    location: DeliveredShipmentTrackingEventLocation

    timestamp: Optional[DeliveredShipmentTrackingEventTimestamp] = None


class DeliveredShipment(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    delivered_at: datetime = FieldInfo(alias="deliveredAt")

    external_id: str = FieldInfo(alias="externalId")
    """
    The external ID is provided by the marketplace and matches the shipment to their
    system.
    """

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["delivered"]

    tracking: ShipmentTracking

    tracking_events: List[DeliveredShipmentTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingDelayedTrackingEventTimestamp(BaseModel):
    local: str
    """ISO 8601 string with timezone offset, e.g. "2025-02-05T17:02:00.000-05:00" """

    utc: datetime
    """UTC timestamp"""


class WithStatusBaseShipmentWithTrackingDelayedTrackingEvent(BaseModel):
    description: Optional[str] = None

    location: WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation

    timestamp: Optional[WithStatusBaseShipmentWithTrackingDelayedTrackingEventTimestamp] = None


class WithStatusBaseShipmentWithTrackingDelayed(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")
    """
    The external ID is provided by the marketplace and matches the shipment to their
    system.
    """

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["delayed"]

    tracking: ShipmentTracking

    tracking_events: List[WithStatusBaseShipmentWithTrackingDelayedTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventTimestamp(BaseModel):
    local: str
    """ISO 8601 string with timezone offset, e.g. "2025-02-05T17:02:00.000-05:00" """

    utc: datetime
    """UTC timestamp"""


class WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEvent(BaseModel):
    description: Optional[str] = None

    location: WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation

    timestamp: Optional[WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventTimestamp] = None


class WithStatusBaseShipmentWithTrackingOutForDelivery(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")
    """
    The external ID is provided by the marketplace and matches the shipment to their
    system.
    """

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["out_for_delivery"]

    tracking: ShipmentTracking

    tracking_events: List[WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEvent] = FieldInfo(
        alias="trackingEvents"
    )

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentOrdered(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    status: Literal["ordered"]

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentCanceled(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    status: Literal["canceled"]

    updated_at: datetime = FieldInfo(alias="updatedAt")


Shipment: TypeAlias = Union[
    WithStatusBaseShipmentWithTrackingShipped,
    DeliveredShipment,
    WithStatusBaseShipmentWithTrackingDelayed,
    WithStatusBaseShipmentWithTrackingOutForDelivery,
    WithStatusBaseShipmentOrdered,
    WithStatusBaseShipmentCanceled,
]
