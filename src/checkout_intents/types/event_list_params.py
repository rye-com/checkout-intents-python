# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after: str

    before: str

    limit: int
    """Maximum number of results to return (default 100)"""
