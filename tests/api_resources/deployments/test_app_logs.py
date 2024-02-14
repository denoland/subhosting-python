# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting._utils import parse_datetime
from subhosting.types.deployments import AppLogGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAppLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Subhosting) -> None:
        app_log = client.deployments.app_logs.get(
            "string",
        )
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Subhosting) -> None:
        app_log = client.deployments.app_logs.get(
            "string",
            cursor="string",
            level="error",
            limit=1,
            order="string",
            q="string",
            region="gcp-asia-east1",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="string",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Subhosting) -> None:
        response = client.deployments.app_logs.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_log = response.parse()
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Subhosting) -> None:
        with client.deployments.app_logs.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_log = response.parse()
            assert_matches_type(AppLogGetResponse, app_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.app_logs.with_raw_response.get(
                "",
            )


class TestAsyncAppLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncSubhosting) -> None:
        app_log = await async_client.deployments.app_logs.get(
            "string",
        )
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncSubhosting) -> None:
        app_log = await async_client.deployments.app_logs.get(
            "string",
            cursor="string",
            level="error",
            limit=1,
            order="string",
            q="string",
            region="gcp-asia-east1",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="string",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.deployments.app_logs.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app_log = await response.parse()
        assert_matches_type(AppLogGetResponse, app_log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSubhosting) -> None:
        async with async_client.deployments.app_logs.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app_log = await response.parse()
            assert_matches_type(AppLogGetResponse, app_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.app_logs.with_raw_response.get(
                "",
            )
