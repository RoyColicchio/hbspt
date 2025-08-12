# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hbs import Hbs, AsyncHbs
from hbs._utils import parse_datetime
from tests.utils import assert_matches_type
from hbs.types.account_info.v3 import (
    ActivityGetAuditLogsResponse,
    ActivityGetLoginActivityResponse,
    ActivityGetSecurityActivityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_audit_logs(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_audit_logs()
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_audit_logs_with_all_params(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_audit_logs(
            acting_user_id=[0],
            after="after",
            limit=0,
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
        )
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_audit_logs(self, client: Hbs) -> None:
        response = client.account_info.v3.activity.with_raw_response.get_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_audit_logs(self, client: Hbs) -> None:
        with client.account_info.v3.activity.with_streaming_response.get_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_login_activity(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_login_activity()
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_login_activity_with_all_params(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_login_activity(
            after="after",
            limit=0,
            user_id=0,
        )
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_login_activity(self, client: Hbs) -> None:
        response = client.account_info.v3.activity.with_raw_response.get_login_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_login_activity(self, client: Hbs) -> None:
        with client.account_info.v3.activity.with_streaming_response.get_login_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_security_activity(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_security_activity()
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_security_activity_with_all_params(self, client: Hbs) -> None:
        activity = client.account_info.v3.activity.get_security_activity(
            after="after",
            from_timestamp=0,
            limit=0,
            user_id=0,
        )
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_security_activity(self, client: Hbs) -> None:
        response = client.account_info.v3.activity.with_raw_response.get_security_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_security_activity(self, client: Hbs) -> None:
        with client.account_info.v3.activity.with_streaming_response.get_security_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActivity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_audit_logs(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_audit_logs()
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_audit_logs_with_all_params(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_audit_logs(
            acting_user_id=[0],
            after="after",
            limit=0,
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
        )
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_audit_logs(self, async_client: AsyncHbs) -> None:
        response = await async_client.account_info.v3.activity.with_raw_response.get_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_audit_logs(self, async_client: AsyncHbs) -> None:
        async with async_client.account_info.v3.activity.with_streaming_response.get_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityGetAuditLogsResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_login_activity(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_login_activity()
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_login_activity_with_all_params(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_login_activity(
            after="after",
            limit=0,
            user_id=0,
        )
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_login_activity(self, async_client: AsyncHbs) -> None:
        response = await async_client.account_info.v3.activity.with_raw_response.get_login_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_login_activity(self, async_client: AsyncHbs) -> None:
        async with async_client.account_info.v3.activity.with_streaming_response.get_login_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityGetLoginActivityResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_security_activity(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_security_activity()
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_security_activity_with_all_params(self, async_client: AsyncHbs) -> None:
        activity = await async_client.account_info.v3.activity.get_security_activity(
            after="after",
            from_timestamp=0,
            limit=0,
            user_id=0,
        )
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_security_activity(self, async_client: AsyncHbs) -> None:
        response = await async_client.account_info.v3.activity.with_raw_response.get_security_activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_security_activity(self, async_client: AsyncHbs) -> None:
        async with async_client.account_info.v3.activity.with_streaming_response.get_security_activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityGetSecurityActivityResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True
