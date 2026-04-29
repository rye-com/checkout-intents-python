# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InstallationLink"]


class InstallationLink(BaseModel):
    """A merchant connector installation link."""

    connector: Literal["shopify"]
    """The merchant connector this installation link was generated for."""

    url: str
    """
    URL to redirect the merchant to in order to install the Rye app on their
    merchant platform.
    """
