# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentGatewaySession"]


class PaymentGatewaySession(BaseModel):
    container: str

    gateway: Literal["basis_theory"]

    session_key: str = FieldInfo(alias="sessionKey")
