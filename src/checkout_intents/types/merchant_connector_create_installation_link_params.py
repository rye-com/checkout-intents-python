# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MerchantConnectorCreateInstallationLinkParams"]


class MerchantConnectorCreateInstallationLinkParams(TypedDict, total=False):
    store_url: Required[Annotated[str, PropertyInfo(alias="storeUrl")]]
    """Domain or URL of the merchant store to generate the installation link for"""

    private: bool
    """
    If true, the merchant onboarded via this link is exclusive to the calling
    developer
    """
