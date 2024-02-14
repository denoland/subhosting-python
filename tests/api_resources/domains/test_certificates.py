# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Subhosting) -> None:
        certificate = client.domains.certificates.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        )
        assert certificate is None

    @parametrize
    def test_raw_response_create(self, client: Subhosting) -> None:
        response = client.domains.certificates.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_create(self, client: Subhosting) -> None:
        with client.domains.certificates.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.certificates.with_raw_response.create(
                "",
                certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
                private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
            )

    @parametrize
    def test_method_provision(self, client: Subhosting) -> None:
        certificate = client.domains.certificates.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert certificate is None

    @parametrize
    def test_raw_response_provision(self, client: Subhosting) -> None:
        response = client.domains.certificates.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert certificate is None

    @parametrize
    def test_streaming_response_provision(self, client: Subhosting) -> None:
        with client.domains.certificates.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.domains.certificates.with_raw_response.provision(
                "",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSubhosting) -> None:
        certificate = await async_client.domains.certificates.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.certificates.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.certificates.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
            private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.certificates.with_raw_response.create(
                "",
                certificate_chain="-----BEGIN CERTIFICATE-----\nfoobar\n-----END CERTIFICATE-----\n",
                private_key="-----BEGIN EC PRIVATE KEY-----\nfoobar\n-----END EC PRIVATE KEY-----\n",
            )

    @parametrize
    async def test_method_provision(self, async_client: AsyncSubhosting) -> None:
        certificate = await async_client.domains.certificates.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert certificate is None

    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.domains.certificates.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert certificate is None

    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncSubhosting) -> None:
        async with async_client.domains.certificates.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert certificate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.domains.certificates.with_raw_response.provision(
                "",
            )
