# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ShipmentStatus"]

ShipmentStatus: TypeAlias = Literal["out_for_delivery", "delivered", "shipped", "canceled", "delayed", "ordered"]
