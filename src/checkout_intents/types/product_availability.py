# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ProductAvailability"]

ProductAvailability: TypeAlias = Literal["in_stock", "out_of_stock", "preorder", "backorder", "unknown"]
