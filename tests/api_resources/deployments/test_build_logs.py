# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting.types.deployments import BuildLogGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuildLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Subhosting) -> None:
        build_log = client.deployments.build_logs.get(
            "string",
        )
        assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Subhosting) -> None:
        response = client.deployments.build_logs.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_log = response.parse()
        assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Subhosting) -> None:
        with client.deployments.build_logs.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_log = response.parse()
            assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.build_logs.with_raw_response.get(
                "",
            )


class TestAsyncBuildLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncSubhosting) -> None:
        build_log = await async_client.deployments.build_logs.get(
            "string",
        )
        assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.deployments.build_logs.with_raw_response.get(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        build_log = await response.parse()
        assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSubhosting) -> None:
        async with async_client.deployments.build_logs.with_streaming_response.get(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            build_log = await response.parse()
            assert_matches_type(BuildLogGetResponse, build_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.build_logs.with_raw_response.get(
                "",
            )
