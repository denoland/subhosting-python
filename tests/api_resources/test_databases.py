# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting.types.shared import KvDatabase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Subhosting) -> None:
        database = client.databases.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Subhosting) -> None:
        database = client.databases.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="My KV database",
        )
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Subhosting) -> None:
        response = client.databases.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Subhosting) -> None:
        with client.databases.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(KvDatabase, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.databases.with_raw_response.update(
                "",
            )


class TestAsyncDatabases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSubhosting) -> None:
        database = await async_client.databases.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSubhosting) -> None:
        database = await async_client.databases.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="My KV database",
        )
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.databases.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(KvDatabase, database, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSubhosting) -> None:
        async with async_client.databases.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(KvDatabase, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.databases.with_raw_response.update(
                "",
            )
