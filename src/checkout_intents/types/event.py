# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Event", "Source"]


class Source(BaseModel):
    """A reference to the object which triggered the event.

    You should use the API to fetch the full object details.
    """

    id: str
    """ID of the object which triggered the event."""

    type: Literal["checkout_intent", "shipment", "webhook_endpoint"]
    """Type of the object which triggered the event."""


class Event(BaseModel):
    id: str
    """Unique identifier for the event.

    This can be used as an idempotency key to avoid double-processing of the same
    underlying event.
    """

    created_at: str = FieldInfo(alias="createdAt")
    """Timestamp of when the event was created."""

    object: Literal["event"]

    source: Source
    """A reference to the object which triggered the event.

    You should use the API to fetch the full object details.
    """

    type: Literal[
        "checkout_intent.offer_retrieved",
        "checkout_intent.offer_failed",
        "checkout_intent.completed",
        "checkout_intent.order_failed",
        "shipment.created",
        "shipment.updated",
        "webhook_endpoint.verification_challenge",
    ]
    """Description of the event.

    Refer to [types of events](https://docs.rye.com/api-v2/webhooks/types) for a
    list of possible values.
    """
