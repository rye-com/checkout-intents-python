# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReturnNextAction", "ShipItemsToMerchant", "ShipItemsToMerchantLabel"]


class ShipItemsToMerchantLabel(BaseModel):
    """A prepaid return shipping label the shopper uses to send items back."""

    url: str
    """URL to the downloadable/printable label."""


class ShipItemsToMerchant(BaseModel):
    """Prepaid return label. Present only when `type` is `ship_items_to_merchant`."""

    label: ShipItemsToMerchantLabel
    """A prepaid return shipping label the shopper uses to send items back."""


class ReturnNextAction(BaseModel):
    """What the shopper has to do next to complete the return.

    Present once the
    Return is approved.

    `type` is the discriminator: `ship_items_to_merchant` carries the matching
    `shipItemsToMerchant` payload (a prepaid label); `no_action_required` means
    the merchant approved a keep-the-item / no-ship return and the shopper just
    waits for the refund (no payload). The `requires_action` state is reached
    only for `ship_items_to_merchant`; a `no_action_required` approval skips
    straight to `processing`.
    """

    type: Literal["ship_items_to_merchant", "no_action_required"]
    """Discriminator for the action the shopper must take."""

    ship_items_to_merchant: Optional[ShipItemsToMerchant] = FieldInfo(alias="shipItemsToMerchant", default=None)
    """Prepaid return label. Present only when `type` is `ship_items_to_merchant`."""
