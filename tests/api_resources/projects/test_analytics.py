# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting._utils import parse_datetime
from subhosting.types.shared import Analytics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Subhosting) -> None:
        analytics = client.projects.analytics.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Analytics, analytics, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Subhosting) -> None:
        response = client.projects.analytics.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(Analytics, analytics, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Subhosting) -> None:
        with client.projects.analytics.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(Analytics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.with_raw_response.get(
                "",
                since=parse_datetime("2019-12-27T18:11:19.117Z"),
                until=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncSubhosting) -> None:
        analytics = await async_client.projects.analytics.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Analytics, analytics, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.projects.analytics.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(Analytics, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSubhosting) -> None:
        async with async_client.projects.analytics.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(Analytics, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.with_raw_response.get(
                "",
                since=parse_datetime("2019-12-27T18:11:19.117Z"),
                until=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
