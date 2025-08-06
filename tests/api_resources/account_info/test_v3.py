# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hbs import Hbs, AsyncHbs
from tests.utils import assert_matches_type
from hbs.types.account_info import V3GetAccountDetailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_account_details(self, client: Hbs) -> None:
        v3 = client.account_info.v3.get_account_details()
        assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_account_details(self, client: Hbs) -> None:
        response = client.account_info.v3.with_raw_response.get_account_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = response.parse()
        assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_account_details(self, client: Hbs) -> None:
        with client.account_info.v3.with_streaming_response.get_account_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = response.parse()
            assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_account_details(self, async_client: AsyncHbs) -> None:
        v3 = await async_client.account_info.v3.get_account_details()
        assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_account_details(self, async_client: AsyncHbs) -> None:
        response = await async_client.account_info.v3.with_raw_response.get_account_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v3 = await response.parse()
        assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_account_details(self, async_client: AsyncHbs) -> None:
        async with async_client.account_info.v3.with_streaming_response.get_account_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v3 = await response.parse()
            assert_matches_type(V3GetAccountDetailsResponse, v3, path=["response"])

        assert cast(Any, response.is_closed) is True
