# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutSessionCreateParams", "Buyer", "Constraints"]


class CheckoutSessionCreateParams(TypedDict, total=False):
    product_url: Required[Annotated[str, PropertyInfo(alias="productUrl")]]

    quantity: Required[int]

    buyer: Buyer
    """
    Optional buyer information, used to pre-fill the checkout form with the buyer's
    information.
    """

    constraints: Constraints

    promo_codes: Annotated[SequenceNotStr[str], PropertyInfo(alias="promoCodes")]

    variant_selections: Annotated[Iterable[VariantSelectionParam], PropertyInfo(alias="variantSelections")]


class Buyer(TypedDict, total=False):
    """
    Optional buyer information, used to pre-fill the checkout form with the buyer's information.
    """

    address1: str

    address2: str

    city: str

    country: str

    email: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    phone: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    province: str


class Constraints(TypedDict, total=False):
    max_shipping_price: Annotated[int, PropertyInfo(alias="maxShippingPrice")]

    max_total_price: Annotated[int, PropertyInfo(alias="maxTotalPrice")]

    offer_retrieval_effort: Annotated[Literal["max", "low"], PropertyInfo(alias="offerRetrievalEffort")]
    """Controls how much effort the system should spend retrieving an offer.

    - 'max': Full effort including AI agent fallback (slower, higher success rate)
    - 'low': Fast API-only retrieval, fails if API unavailable (faster, lower
      success rate)

    Default: 'max'
    """
