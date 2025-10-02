# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hbs import Hbs, AsyncHbs
from tests.utils import assert_matches_type
from hbs.types.account_info.v3 import APIUsageGetDailyUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_daily_usage(self, client: Hbs) -> None:
        api_usage = client.account_info.v3.api_usage.get_daily_usage()
        assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_daily_usage(self, client: Hbs) -> None:
        response = client.account_info.v3.api_usage.with_raw_response.get_daily_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_usage = response.parse()
        assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_daily_usage(self, client: Hbs) -> None:
        with client.account_info.v3.api_usage.with_streaming_response.get_daily_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_usage = response.parse()
            assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_daily_usage(self, async_client: AsyncHbs) -> None:
        api_usage = await async_client.account_info.v3.api_usage.get_daily_usage()
        assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_daily_usage(self, async_client: AsyncHbs) -> None:
        response = await async_client.account_info.v3.api_usage.with_raw_response.get_daily_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_usage = await response.parse()
        assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_daily_usage(self, async_client: AsyncHbs) -> None:
        async with async_client.account_info.v3.api_usage.with_streaming_response.get_daily_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_usage = await response.parse()
            assert_matches_type(APIUsageGetDailyUsageResponse, api_usage, path=["response"])

        assert cast(Any, response.is_closed) is True
