# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.account_info.v3 import (
    activity_get_audit_logs_params,
    activity_get_login_activity_params,
    activity_get_security_activity_params,
)
from ....types.account_info.v3.activity_get_audit_logs_response import ActivityGetAuditLogsResponse
from ....types.account_info.v3.activity_get_login_activity_response import ActivityGetLoginActivityResponse
from ....types.account_info.v3.activity_get_security_activity_response import ActivityGetSecurityActivityResponse

__all__ = ["ActivityResource", "AsyncActivityResource"]


class ActivityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hbs-python#accessing-raw-response-data-eg-headers
        """
        return ActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hbs-python#with_streaming_response
        """
        return ActivityResourceWithStreamingResponse(self)

    def get_audit_logs(
        self,
        *,
        acting_user_id: Iterable[int] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        occurred_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occurred_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetAuditLogsResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/account-info/v3/activity/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "acting_user_id": acting_user_id,
                        "after": after,
                        "limit": limit,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "sort": sort,
                    },
                    activity_get_audit_logs_params.ActivityGetAuditLogsParams,
                ),
            ),
            cast_to=ActivityGetAuditLogsResponse,
        )

    def get_login_activity(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        user_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetLoginActivityResponse:
        """
        Get login activity.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to display per page. Max value of limit is 200.

          user_id: Identifier of user to retrieve activities for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/account-info/v3/activity/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_get_login_activity_params.ActivityGetLoginActivityParams,
                ),
            ),
            cast_to=ActivityGetLoginActivityResponse,
        )

    def get_security_activity(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        from_timestamp: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        user_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetSecurityActivityResponse:
        """
        Get security activity

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          from_timestamp: Limit to activities created after this epoch timestamp.

          limit: The maximum number of results to display per page. Max value of limit is 200.

          user_id: Identifier of user to retrieve activities for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/account-info/v3/activity/security",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_get_security_activity_params.ActivityGetSecurityActivityParams,
                ),
            ),
            cast_to=ActivityGetSecurityActivityResponse,
        )


class AsyncActivityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hbs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hbs-python#with_streaming_response
        """
        return AsyncActivityResourceWithStreamingResponse(self)

    async def get_audit_logs(
        self,
        *,
        acting_user_id: Iterable[int] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        occurred_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        occurred_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetAuditLogsResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/account-info/v3/activity/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "acting_user_id": acting_user_id,
                        "after": after,
                        "limit": limit,
                        "occurred_after": occurred_after,
                        "occurred_before": occurred_before,
                        "sort": sort,
                    },
                    activity_get_audit_logs_params.ActivityGetAuditLogsParams,
                ),
            ),
            cast_to=ActivityGetAuditLogsResponse,
        )

    async def get_login_activity(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        user_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetLoginActivityResponse:
        """
        Get login activity.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to display per page. Max value of limit is 200.

          user_id: Identifier of user to retrieve activities for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/account-info/v3/activity/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_get_login_activity_params.ActivityGetLoginActivityParams,
                ),
            ),
            cast_to=ActivityGetLoginActivityResponse,
        )

    async def get_security_activity(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        from_timestamp: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        user_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityGetSecurityActivityResponse:
        """
        Get security activity

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          from_timestamp: Limit to activities created after this epoch timestamp.

          limit: The maximum number of results to display per page. Max value of limit is 200.

          user_id: Identifier of user to retrieve activities for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/account-info/v3/activity/security",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "user_id": user_id,
                    },
                    activity_get_security_activity_params.ActivityGetSecurityActivityParams,
                ),
            ),
            cast_to=ActivityGetSecurityActivityResponse,
        )


class ActivityResourceWithRawResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.get_audit_logs = to_raw_response_wrapper(
            activity.get_audit_logs,
        )
        self.get_login_activity = to_raw_response_wrapper(
            activity.get_login_activity,
        )
        self.get_security_activity = to_raw_response_wrapper(
            activity.get_security_activity,
        )


class AsyncActivityResourceWithRawResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.get_audit_logs = async_to_raw_response_wrapper(
            activity.get_audit_logs,
        )
        self.get_login_activity = async_to_raw_response_wrapper(
            activity.get_login_activity,
        )
        self.get_security_activity = async_to_raw_response_wrapper(
            activity.get_security_activity,
        )


class ActivityResourceWithStreamingResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.get_audit_logs = to_streamed_response_wrapper(
            activity.get_audit_logs,
        )
        self.get_login_activity = to_streamed_response_wrapper(
            activity.get_login_activity,
        )
        self.get_security_activity = to_streamed_response_wrapper(
            activity.get_security_activity,
        )


class AsyncActivityResourceWithStreamingResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.get_audit_logs = async_to_streamed_response_wrapper(
            activity.get_audit_logs,
        )
        self.get_login_activity = async_to_streamed_response_wrapper(
            activity.get_login_activity,
        )
        self.get_security_activity = async_to_streamed_response_wrapper(
            activity.get_security_activity,
        )
