# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .product_subscription_store import ProductSubscriptionStore
from .product_subscription_product import ProductSubscriptionProduct

__all__ = ["ProductSubscription"]

ProductSubscription: TypeAlias = Union[ProductSubscriptionProduct, ProductSubscriptionStore]
