# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting.types.shared import Domain

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Subhosting) -> None:
        domain = client.domains.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    def test_method_update_with_all_params(self, client: Subhosting) -> None:
        domain = client.domains.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            deployment_id="abcde12vwxyz",
        )
        assert domain is None

    @parametrize
    def test_raw_response_update(self, client: Subhosting) -> None:
        response = client.domains.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @parametrize
    def test_streaming_response_update(self, client: Subhosting) -> None:
        with client.domains.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Subhosting) -> None:
        domain = client.domains.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    def test_raw_response_delete(self, client: Subhosting) -> None:
        response = client.domains.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @parametrize
    def test_streaming_response_delete(self, client: Subhosting) -> None:
        with client.domains.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Subhosting) -> None:
        domain = client.domains.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Subhosting) -> None:
        response = client.domains.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Subhosting) -> None:
        with client.domains.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_verify(self, client: Subhosting) -> None:
        domain = client.domains.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    def test_raw_response_verify(self, client: Subhosting) -> None:
        response = client.domains.with_raw_response.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @parametrize
    def test_streaming_response_verify(self, client: Subhosting) -> None:
        with client.domains.with_streaming_response.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_verify(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.with_raw_response.verify(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.domains.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.domains.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            deployment_id="abcde12vwxyz",
        )
        assert domain is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.domains.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.domains.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_verify(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.domains.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert domain is None

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.with_raw_response.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.with_streaming_response.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_verify(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.with_raw_response.verify(
                "",
            )
