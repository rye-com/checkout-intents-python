# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckoutIntentAddPaymentParams"]


class CheckoutIntentAddPaymentParams(TypedDict, total=False):
    body: Required[object]
    """The request body containing the payment details"""
