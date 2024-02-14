# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from subhosting import Subhosting, AsyncSubhosting
from tests.utils import assert_matches_type
from subhosting.types.shared import Deployment
from subhosting.types.projects import DeploymentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Subhosting) -> None:
        deployment = client.projects.deployments.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Subhosting) -> None:
        deployment = client.projects.deployments.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {
                    "content": 'Deno.serve((req: Request) => new Response("Hello World"));\n',
                    "encoding": "utf-8",
                    "git_sha1": "string",
                    "kind": "file",
                },
                "images/cat1.png": {
                    "content": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk",
                    "encoding": "base64",
                    "git_sha1": "string",
                    "kind": "file",
                },
                "images/cat2.png": {
                    "content": "string",
                    "encoding": "utf-8",
                    "git_sha1": "5c4f8729e5c30a91a890e24d7285e89f418c637b",
                    "kind": "file",
                },
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
            compiler_options={
                "jsx": "string",
                "jsx_factory": "string",
                "jsx_fragment_factory": "string",
                "jsx_import_source": "string",
            },
            databases={"default": "5b484959-cba2-482d-95ab-ba592784af80"},
            description="My first deployment",
            import_map_url=None,
            lock_file_url=None,
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Subhosting) -> None:
        response = client.projects.deployments.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Subhosting) -> None:
        with client.projects.deployments.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.deployments.with_raw_response.create(
                "",
                assets={
                    "main.ts": {"kind": "file"},
                    "images/cat1.png": {"kind": "file"},
                    "images/cat2.png": {"kind": "file"},
                    "symlink.png": {
                        "target": "images/cat1.png",
                        "kind": "symlink",
                    },
                },
                entry_point_url="main.ts",
                env_vars={"MY_ENV": "hey"},
            )

    @parametrize
    def test_method_list(self, client: Subhosting) -> None:
        deployment = client.projects.deployments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Subhosting) -> None:
        deployment = client.projects.deployments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            order="string",
            page=1,
            q="string",
            sort="string",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Subhosting) -> None:
        response = client.projects.deployments.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Subhosting) -> None:
        with client.projects.deployments.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentListResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Subhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.deployments.with_raw_response.list(
                "",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSubhosting) -> None:
        deployment = await async_client.projects.deployments.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSubhosting) -> None:
        deployment = await async_client.projects.deployments.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {
                    "content": 'Deno.serve((req: Request) => new Response("Hello World"));\n',
                    "encoding": "utf-8",
                    "git_sha1": "string",
                    "kind": "file",
                },
                "images/cat1.png": {
                    "content": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk",
                    "encoding": "base64",
                    "git_sha1": "string",
                    "kind": "file",
                },
                "images/cat2.png": {
                    "content": "string",
                    "encoding": "utf-8",
                    "git_sha1": "5c4f8729e5c30a91a890e24d7285e89f418c637b",
                    "kind": "file",
                },
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
            compiler_options={
                "jsx": "string",
                "jsx_factory": "string",
                "jsx_fragment_factory": "string",
                "jsx_import_source": "string",
            },
            databases={"default": "5b484959-cba2-482d-95ab-ba592784af80"},
            description="My first deployment",
            import_map_url=None,
            lock_file_url=None,
        )
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.projects.deployments.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Deployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSubhosting) -> None:
        async with async_client.projects.deployments.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assets={
                "main.ts": {"kind": "file"},
                "images/cat1.png": {"kind": "file"},
                "images/cat2.png": {"kind": "file"},
                "symlink.png": {
                    "target": "images/cat1.png",
                    "kind": "symlink",
                },
            },
            entry_point_url="main.ts",
            env_vars={"MY_ENV": "hey"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Deployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.deployments.with_raw_response.create(
                "",
                assets={
                    "main.ts": {"kind": "file"},
                    "images/cat1.png": {"kind": "file"},
                    "images/cat2.png": {"kind": "file"},
                    "symlink.png": {
                        "target": "images/cat1.png",
                        "kind": "symlink",
                    },
                },
                entry_point_url="main.ts",
                env_vars={"MY_ENV": "hey"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSubhosting) -> None:
        deployment = await async_client.projects.deployments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSubhosting) -> None:
        deployment = await async_client.projects.deployments.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            order="string",
            page=1,
            q="string",
            sort="string",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSubhosting) -> None:
        response = await async_client.projects.deployments.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSubhosting) -> None:
        async with async_client.projects.deployments.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentListResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSubhosting) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.deployments.with_raw_response.list(
                "",
            )
