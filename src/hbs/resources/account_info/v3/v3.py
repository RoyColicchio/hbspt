# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .api_usage import (
    APIUsageResource,
    AsyncAPIUsageResource,
    APIUsageResourceWithRawResponse,
    AsyncAPIUsageResourceWithRawResponse,
    APIUsageResourceWithStreamingResponse,
    AsyncAPIUsageResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.account_info.v3_get_account_details_response import V3GetAccountDetailsResponse

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def activity(self) -> ActivityResource:
        return ActivityResource(self._client)

    @cached_property
    def api_usage(self) -> APIUsageResource:
        return APIUsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RoyColicchio/hbspt#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RoyColicchio/hbspt#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)

    def get_account_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3GetAccountDetailsResponse:
        """Get account details"""
        return self._get(
            "/account-info/v3/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetAccountDetailsResponse,
        )


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def activity(self) -> AsyncActivityResource:
        return AsyncActivityResource(self._client)

    @cached_property
    def api_usage(self) -> AsyncAPIUsageResource:
        return AsyncAPIUsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RoyColicchio/hbspt#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RoyColicchio/hbspt#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)

    async def get_account_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V3GetAccountDetailsResponse:
        """Get account details"""
        return await self._get(
            "/account-info/v3/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V3GetAccountDetailsResponse,
        )


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.get_account_details = to_raw_response_wrapper(
            v3.get_account_details,
        )

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        return ActivityResourceWithRawResponse(self._v3.activity)

    @cached_property
    def api_usage(self) -> APIUsageResourceWithRawResponse:
        return APIUsageResourceWithRawResponse(self._v3.api_usage)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.get_account_details = async_to_raw_response_wrapper(
            v3.get_account_details,
        )

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        return AsyncActivityResourceWithRawResponse(self._v3.activity)

    @cached_property
    def api_usage(self) -> AsyncAPIUsageResourceWithRawResponse:
        return AsyncAPIUsageResourceWithRawResponse(self._v3.api_usage)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

        self.get_account_details = to_streamed_response_wrapper(
            v3.get_account_details,
        )

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        return ActivityResourceWithStreamingResponse(self._v3.activity)

    @cached_property
    def api_usage(self) -> APIUsageResourceWithStreamingResponse:
        return APIUsageResourceWithStreamingResponse(self._v3.api_usage)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

        self.get_account_details = async_to_streamed_response_wrapper(
            v3.get_account_details,
        )

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        return AsyncActivityResourceWithStreamingResponse(self._v3.activity)

    @cached_property
    def api_usage(self) -> AsyncAPIUsageResourceWithStreamingResponse:
        return AsyncAPIUsageResourceWithStreamingResponse(self._v3.api_usage)
