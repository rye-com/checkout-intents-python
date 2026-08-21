# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CommissionStatus"]

CommissionStatus: TypeAlias = Literal["pending", "confirmed", "updated", "finalized", "refunded", "expired"]
