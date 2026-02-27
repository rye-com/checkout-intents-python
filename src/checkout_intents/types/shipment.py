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
    "DeliveredShipment",
    "DeliveredShipmentTrackingEvent",
    "DeliveredShipmentTrackingEventLocation",
    "WithStatusBaseShipmentWithTrackingDelayed",
    "WithStatusBaseShipmentWithTrackingDelayedTrackingEvent",
    "WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation",
    "WithStatusBaseShipmentWithTrackingOutForDelivery",
    "WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEvent",
    "WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation",
    "WithStatusBaseShipmentOrdered",
    "WithStatusBaseShipmentCanceled",
]


class WithStatusBaseShipmentWithTrackingShippedTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingShippedTrackingEvent(BaseModel):
    description: Optional[str] = None

    display_date: Optional[str] = FieldInfo(alias="displayDate", default=None)

    display_time: Optional[str] = FieldInfo(alias="displayTime", default=None)

    location: WithStatusBaseShipmentWithTrackingShippedTrackingEventLocation


class WithStatusBaseShipmentWithTrackingShipped(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["shipped"]

    tracking: ShipmentTracking

    tracking_events: List[WithStatusBaseShipmentWithTrackingShippedTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class DeliveredShipmentTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class DeliveredShipmentTrackingEvent(BaseModel):
    description: Optional[str] = None

    display_date: Optional[str] = FieldInfo(alias="displayDate", default=None)

    display_time: Optional[str] = FieldInfo(alias="displayTime", default=None)

    location: DeliveredShipmentTrackingEventLocation


class DeliveredShipment(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    delivered_at: datetime = FieldInfo(alias="deliveredAt")

    external_id: str = FieldInfo(alias="externalId")

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["delivered"]

    tracking: ShipmentTracking

    tracking_events: List[DeliveredShipmentTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingDelayedTrackingEvent(BaseModel):
    description: Optional[str] = None

    display_date: Optional[str] = FieldInfo(alias="displayDate", default=None)

    display_time: Optional[str] = FieldInfo(alias="displayTime", default=None)

    location: WithStatusBaseShipmentWithTrackingDelayedTrackingEventLocation


class WithStatusBaseShipmentWithTrackingDelayed(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")

    shipped_at: datetime = FieldInfo(alias="shippedAt")

    status: Literal["delayed"]

    tracking: ShipmentTracking

    tracking_events: List[WithStatusBaseShipmentWithTrackingDelayedTrackingEvent] = FieldInfo(alias="trackingEvents")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    province: Optional[str] = None


class WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEvent(BaseModel):
    description: Optional[str] = None

    display_date: Optional[str] = FieldInfo(alias="displayDate", default=None)

    display_time: Optional[str] = FieldInfo(alias="displayTime", default=None)

    location: WithStatusBaseShipmentWithTrackingOutForDeliveryTrackingEventLocation


class WithStatusBaseShipmentWithTrackingOutForDelivery(BaseModel):
    id: str

    checkout_intent_id: str = FieldInfo(alias="checkoutIntentId")

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")

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
