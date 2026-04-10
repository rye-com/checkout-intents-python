# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .money import Money
from .._models import BaseModel

__all__ = ["BillingCreateTopupInvoiceResponse", "BankTransferDetails"]


class BankTransferDetails(BaseModel):
    """Vendor-agnostic bank transfer details for push-based payment"""

    account_holder_name: str = FieldInfo(alias="accountHolderName")

    account_number: str = FieldInfo(alias="accountNumber")

    bank_name: str = FieldInfo(alias="bankName")

    routing_number: str = FieldInfo(alias="routingNumber")


class BillingCreateTopupInvoiceResponse(BaseModel):
    id: str

    amount: Money

    bank_transfer_details: BankTransferDetails = FieldInfo(alias="bankTransferDetails")
    """Vendor-agnostic bank transfer details for push-based payment"""

    status: Literal["draft", "open", "paid", "uncollectible", "void", "unknown"]
    """Vendor-agnostic provider types"""

    url: Optional[str] = None
