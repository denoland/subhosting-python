# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting.types.shared import Domain
from subhosting.types.organizations import DomainListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Subhosting) -> None:
        domain = client.organizations.domains.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Subhosting) -> None:
        response = client.organizations.domains.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Subhosting) -> None:
        with client.organizations.domains.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.domains.with_raw_response.create(
                "",
                domain="foo.example.com",
            )

    @parametrize
    def test_method_list(self, client: Subhosting) -> None:
        domain = client.organizations.domains.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Subhosting) -> None:
        domain = client.organizations.domains.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            order="string",
            page=1,
            q="string",
            sort="string",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Subhosting) -> None:
        response = client.organizations.domains.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Subhosting) -> None:
        with client.organizations.domains.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.domains.with_raw_response.list(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.organizations.domains.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.organizations.domains.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSubhosting) -> None:
        async with async_client.organizations.domains.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain="foo.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.domains.with_raw_response.create(
                "",
                domain="foo.example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.organizations.domains.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSubhosting) -> None:
        domain = await async_client.organizations.domains.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            order="string",
            page=1,
            q="string",
            sort="string",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.organizations.domains.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSubhosting) -> None:
        async with async_client.organizations.domains.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.domains.with_raw_response.list(
                "",
            )
