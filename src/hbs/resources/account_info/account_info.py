# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v3.v3 import (
    V3Resource,
    AsyncV3Resource,
    V3ResourceWithRawResponse,
    AsyncV3ResourceWithRawResponse,
    V3ResourceWithStreamingResponse,
    AsyncV3ResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccountInfoResource", "AsyncAccountInfoResource"]


class AccountInfoResource(SyncAPIResource):
    @cached_property
    def v3(self) -> V3Resource:
        return V3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RoyColicchio/hbspt#accessing-raw-response-data-eg-headers
        """
        return AccountInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RoyColicchio/hbspt#with_streaming_response
        """
        return AccountInfoResourceWithStreamingResponse(self)


class AsyncAccountInfoResource(AsyncAPIResource):
    @cached_property
    def v3(self) -> AsyncV3Resource:
        return AsyncV3Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RoyColicchio/hbspt#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RoyColicchio/hbspt#with_streaming_response
        """
        return AsyncAccountInfoResourceWithStreamingResponse(self)


class AccountInfoResourceWithRawResponse:
    def __init__(self, account_info: AccountInfoResource) -> None:
        self._account_info = account_info

    @cached_property
    def v3(self) -> V3ResourceWithRawResponse:
        return V3ResourceWithRawResponse(self._account_info.v3)


class AsyncAccountInfoResourceWithRawResponse:
    def __init__(self, account_info: AsyncAccountInfoResource) -> None:
        self._account_info = account_info

    @cached_property
    def v3(self) -> AsyncV3ResourceWithRawResponse:
        return AsyncV3ResourceWithRawResponse(self._account_info.v3)


class AccountInfoResourceWithStreamingResponse:
    def __init__(self, account_info: AccountInfoResource) -> None:
        self._account_info = account_info

    @cached_property
    def v3(self) -> V3ResourceWithStreamingResponse:
        return V3ResourceWithStreamingResponse(self._account_info.v3)


class AsyncAccountInfoResourceWithStreamingResponse:
    def __init__(self, account_info: AsyncAccountInfoResource) -> None:
        self._account_info = account_info

    @cached_property
    def v3(self) -> AsyncV3ResourceWithStreamingResponse:
        return AsyncV3ResourceWithStreamingResponse(self._account_info.v3)
