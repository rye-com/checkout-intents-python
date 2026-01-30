# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .money import Money
from .._models import BaseModel
from .product_image import ProductImage
from .product_availability import ProductAvailability

__all__ = ["Product"]


class Product(BaseModel):
    id: str

    availability: ProductAvailability
    """The availability status of a product.

    - `in_stock`: Product is available for immediate purchase
    - `out_of_stock`: Product is currently unavailable
    - `preorder`: Product is available for pre-order before release
    - `backorder`: Product is temporarily out of stock but can be ordered
    - `unknown`: Availability could not be determined
    """

    brand: Optional[str] = None

    description: Optional[str] = None

    images: List[ProductImage]

    name: str

    price: Money

    sku: Optional[str] = None

    url: str
