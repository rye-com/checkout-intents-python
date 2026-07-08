# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .product_subscription import ProductSubscription

__all__ = ["ProductListSubscriptionsResponse"]


class ProductListSubscriptionsResponse(BaseModel):
    data: List[ProductSubscription]
