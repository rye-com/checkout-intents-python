# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillingCreateTopupInvoiceParams"]


class BillingCreateTopupInvoiceParams(TypedDict, total=False):
    amount_subunits: Required[Annotated[int, PropertyInfo(alias="amountSubunits")]]
    """Amount in smallest currency unit (e.g. cents)."""

    charge_automatically: Annotated[bool, PropertyInfo(alias="chargeAutomatically")]
    """
    Override whether to automatically charge the invoice. Defaults to the
    developer's drawdown config value if not specified.
    """
