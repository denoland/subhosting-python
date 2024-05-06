# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import deployment_redeploy_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .app_logs import (
    AppLogsResource,
    AsyncAppLogsResource,
    AppLogsResourceWithRawResponse,
    AsyncAppLogsResourceWithRawResponse,
    AppLogsResourceWithStreamingResponse,
    AsyncAppLogsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .build_logs import (
    BuildLogsResource,
    AsyncBuildLogsResource,
    BuildLogsResourceWithRawResponse,
    AsyncBuildLogsResourceWithRawResponse,
    BuildLogsResourceWithStreamingResponse,
    AsyncBuildLogsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared.deployment import Deployment

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def build_logs(self) -> BuildLogsResource:
        return BuildLogsResource(self._client)

    @cached_property
    def app_logs(self) -> AppLogsResource:
        return AppLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self)

    def delete(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a deployment

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Get deployment details

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deployment,
        )

    def redeploy(
        self,
        deployment_id: str,
        *,
        databases: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        env_vars: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Redeploy a deployment with different configuration

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          databases: KV database ID mappings to associate with the deployment.

              A key represents a KV database name (e.g. `"default"`), and a value is a KV
              database ID.

              Currently, only `"default"` database is supported. If any other database name is
              specified, that will be rejected.

              The provided KV database mappings will be _merged_ with the existing one, just
              like `env_vars`.

              If `databases` itself is not provided, no update will happen to the existing KV
              database mappings.

          description: A description of the created deployment. If not provided, no update will happen
              to the description.

          env_vars: A dictionary of environment variables to be set in the runtime environment of
              the deployment.

              The provided environment variables will be _merged_ with the existing one. For
              example, if the existing environment variables are:

              ```json
              {
              "a": "alice",
              "b": "bob"
              "c": "charlie"
              }
              ```

              and you pass the following environment variables in your redeploy request:

              ```json
              {
                "a": "alice2",
                "b": null,
                "d": "david"
              }
              ```

              then the result will be:

              ```json
              {
                "a": "alice2",
                "c": "charlie",
                "d": "david"
              }
              ```

              If `env_vars` itself is not provided, no update will happen to the existing
              environment variables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            f"/deployments/{deployment_id}/redeploy",
            body=maybe_transform(
                {
                    "databases": databases,
                    "description": description,
                    "env_vars": env_vars,
                },
                deployment_redeploy_params.DeploymentRedeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deployment,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def build_logs(self) -> AsyncBuildLogsResource:
        return AsyncBuildLogsResource(self._client)

    @cached_property
    def app_logs(self) -> AsyncAppLogsResource:
        return AsyncAppLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def delete(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a deployment

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        deployment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Get deployment details

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deployment,
        )

    async def redeploy(
        self,
        deployment_id: str,
        *,
        databases: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        env_vars: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Redeploy a deployment with different configuration

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          databases: KV database ID mappings to associate with the deployment.

              A key represents a KV database name (e.g. `"default"`), and a value is a KV
              database ID.

              Currently, only `"default"` database is supported. If any other database name is
              specified, that will be rejected.

              The provided KV database mappings will be _merged_ with the existing one, just
              like `env_vars`.

              If `databases` itself is not provided, no update will happen to the existing KV
              database mappings.

          description: A description of the created deployment. If not provided, no update will happen
              to the description.

          env_vars: A dictionary of environment variables to be set in the runtime environment of
              the deployment.

              The provided environment variables will be _merged_ with the existing one. For
              example, if the existing environment variables are:

              ```json
              {
              "a": "alice",
              "b": "bob"
              "c": "charlie"
              }
              ```

              and you pass the following environment variables in your redeploy request:

              ```json
              {
                "a": "alice2",
                "b": null,
                "d": "david"
              }
              ```

              then the result will be:

              ```json
              {
                "a": "alice2",
                "c": "charlie",
                "d": "david"
              }
              ```

              If `env_vars` itself is not provided, no update will happen to the existing
              environment variables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            f"/deployments/{deployment_id}/redeploy",
            body=await async_maybe_transform(
                {
                    "databases": databases,
                    "description": description,
                    "env_vars": env_vars,
                },
                deployment_redeploy_params.DeploymentRedeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Deployment,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.delete = to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = to_raw_response_wrapper(
            deployments.get,
        )
        self.redeploy = to_raw_response_wrapper(
            deployments.redeploy,
        )

    @cached_property
    def build_logs(self) -> BuildLogsResourceWithRawResponse:
        return BuildLogsResourceWithRawResponse(self._deployments.build_logs)

    @cached_property
    def app_logs(self) -> AppLogsResourceWithRawResponse:
        return AppLogsResourceWithRawResponse(self._deployments.app_logs)


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.delete = async_to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_raw_response_wrapper(
            deployments.get,
        )
        self.redeploy = async_to_raw_response_wrapper(
            deployments.redeploy,
        )

    @cached_property
    def build_logs(self) -> AsyncBuildLogsResourceWithRawResponse:
        return AsyncBuildLogsResourceWithRawResponse(self._deployments.build_logs)

    @cached_property
    def app_logs(self) -> AsyncAppLogsResourceWithRawResponse:
        return AsyncAppLogsResourceWithRawResponse(self._deployments.app_logs)


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.delete = to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = to_streamed_response_wrapper(
            deployments.get,
        )
        self.redeploy = to_streamed_response_wrapper(
            deployments.redeploy,
        )

    @cached_property
    def build_logs(self) -> BuildLogsResourceWithStreamingResponse:
        return BuildLogsResourceWithStreamingResponse(self._deployments.build_logs)

    @cached_property
    def app_logs(self) -> AppLogsResourceWithStreamingResponse:
        return AppLogsResourceWithStreamingResponse(self._deployments.app_logs)


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.delete = async_to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            deployments.get,
        )
        self.redeploy = async_to_streamed_response_wrapper(
            deployments.redeploy,
        )

    @cached_property
    def build_logs(self) -> AsyncBuildLogsResourceWithStreamingResponse:
        return AsyncBuildLogsResourceWithStreamingResponse(self._deployments.build_logs)

    @cached_property
    def app_logs(self) -> AsyncAppLogsResourceWithStreamingResponse:
        return AsyncAppLogsResourceWithStreamingResponse(self._deployments.app_logs)
