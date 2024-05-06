# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
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
from ...types.organizations import database_list_params, database_create_params
from ...types.shared.kv_database import KvDatabase
from ...types.organizations.database_list_response import DatabaseListResponse

__all__ = ["DatabasesResource", "AsyncDatabasesResource"]


class DatabasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabasesResourceWithRawResponse:
        return DatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabasesResourceWithStreamingResponse:
        return DatabasesResourceWithStreamingResponse(self)

    def create(
        self,
        organization_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KvDatabase:
        """
        Create a KV database

        This API allows you to create a new KV database under the specified
        organization. You will then be able to associate the created KV database with a
        new deployment by specifying the KV database ID in the "Create a deployment" API
        call.

        Args:
          description: The description of the KV database. If this is `null`, an empty string will be
              set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._post(
            f"/organizations/{organization_id}/databases",
            body=maybe_transform({"description": description}, database_create_params.DatabaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvDatabase,
        )

    def list(
        self,
        organization_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        order: Optional[str] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        q: Optional[str] | NotGiven = NOT_GIVEN,
        sort: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
        """
        List KV databases of an organization

        This API returns a list of KV databases belonging to the specified organization
        in a pagenated manner. The URLs for the next, previous, first, and last page are
        returned in the `Link` header of the response, if any.

        Args:
          limit: The maximum number of items to return per page.

          order: Sort order, either `asc` or `desc`. Defaults to `asc`.

          page: The page number to return.

          q: Query by KV database ID

          sort: The field to sort by. Currently only `created_at` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/organizations/{organization_id}/databases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "order": order,
                        "page": page,
                        "q": q,
                        "sort": sort,
                    },
                    database_list_params.DatabaseListParams,
                ),
            ),
            cast_to=DatabaseListResponse,
        )


class AsyncDatabasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabasesResourceWithRawResponse:
        return AsyncDatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabasesResourceWithStreamingResponse:
        return AsyncDatabasesResourceWithStreamingResponse(self)

    async def create(
        self,
        organization_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KvDatabase:
        """
        Create a KV database

        This API allows you to create a new KV database under the specified
        organization. You will then be able to associate the created KV database with a
        new deployment by specifying the KV database ID in the "Create a deployment" API
        call.

        Args:
          description: The description of the KV database. If this is `null`, an empty string will be
              set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._post(
            f"/organizations/{organization_id}/databases",
            body=await async_maybe_transform({"description": description}, database_create_params.DatabaseCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvDatabase,
        )

    async def list(
        self,
        organization_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        order: Optional[str] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        q: Optional[str] | NotGiven = NOT_GIVEN,
        sort: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
        """
        List KV databases of an organization

        This API returns a list of KV databases belonging to the specified organization
        in a pagenated manner. The URLs for the next, previous, first, and last page are
        returned in the `Link` header of the response, if any.

        Args:
          limit: The maximum number of items to return per page.

          order: Sort order, either `asc` or `desc`. Defaults to `asc`.

          page: The page number to return.

          q: Query by KV database ID

          sort: The field to sort by. Currently only `created_at` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/organizations/{organization_id}/databases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "order": order,
                        "page": page,
                        "q": q,
                        "sort": sort,
                    },
                    database_list_params.DatabaseListParams,
                ),
            ),
            cast_to=DatabaseListResponse,
        )


class DatabasesResourceWithRawResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.create = to_raw_response_wrapper(
            databases.create,
        )
        self.list = to_raw_response_wrapper(
            databases.list,
        )


class AsyncDatabasesResourceWithRawResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.create = async_to_raw_response_wrapper(
            databases.create,
        )
        self.list = async_to_raw_response_wrapper(
            databases.list,
        )


class DatabasesResourceWithStreamingResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.create = to_streamed_response_wrapper(
            databases.create,
        )
        self.list = to_streamed_response_wrapper(
            databases.list,
        )


class AsyncDatabasesResourceWithStreamingResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.create = async_to_streamed_response_wrapper(
            databases.create,
        )
        self.list = async_to_streamed_response_wrapper(
            databases.list,
        )
