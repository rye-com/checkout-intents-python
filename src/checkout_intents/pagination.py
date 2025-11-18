# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPaginationPageInfo", "SyncCursorPagination", "AsyncCursorPagination"]

_T = TypeVar("_T")


class CursorPaginationPageInfo(BaseModel):
    end_cursor: Optional[str] = FieldInfo(alias="endCursor", default=None)

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    has_previous_page: Optional[bool] = FieldInfo(alias="hasPreviousPage", default=None)

    start_cursor: Optional[str] = FieldInfo(alias="startCursor", default=None)


class SyncCursorPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page_info: Optional[CursorPaginationPageInfo] = FieldInfo(alias="pageInfo", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            start_cursor = None
            if self.page_info is not None:
                if self.page_info.start_cursor is not None:
                    start_cursor = self.page_info.start_cursor
            if not start_cursor:
                return None

            return PageInfo(params={"before": start_cursor})

        end_cursor = None
        if self.page_info is not None:
            if self.page_info.end_cursor is not None:
                end_cursor = self.page_info.end_cursor
        if not end_cursor:
            return None

        return PageInfo(params={"after": end_cursor})


class AsyncCursorPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page_info: Optional[CursorPaginationPageInfo] = FieldInfo(alias="pageInfo", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            start_cursor = None
            if self.page_info is not None:
                if self.page_info.start_cursor is not None:
                    start_cursor = self.page_info.start_cursor
            if not start_cursor:
                return None

            return PageInfo(params={"before": start_cursor})

        end_cursor = None
        if self.page_info is not None:
            if self.page_info.end_cursor is not None:
                end_cursor = self.page_info.end_cursor
        if not end_cursor:
            return None

        return PageInfo(params={"after": end_cursor})
