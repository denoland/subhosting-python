# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import domain_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared.domain import Domain

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self)

    def update(
        self,
        domain_id: str,
        *,
        deployment_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Associate a domain with a deployment

        This API allows you to either:

        1.

        associate a domain with a deployment, or
        2. disassociate a domain from a deployment

        Domain association is required in order to serve the deployment on the domain.

        If the ownership of the domain is not verified yet, this API will trigger the
        verification process before associating the domain with the deployment.

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/domains/{domain_id}",
            body=maybe_transform({"deployment_id": deployment_id}, domain_update_params.DomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Domain:
        """
        Get domain details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            f"/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Domain,
        )

    def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify ownership of a domain

        This API triggers the ownership verification of a domain. It should be called
        after necessary DNS records are properly set up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/domains/{domain_id}/verify",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        domain_id: str,
        *,
        deployment_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Associate a domain with a deployment

        This API allows you to either:

        1.

        associate a domain with a deployment, or
        2. disassociate a domain from a deployment

        Domain association is required in order to serve the deployment on the domain.

        If the ownership of the domain is not verified yet, this API will trigger the
        verification process before associating the domain with the deployment.

        Args:
          deployment_id: A deployment ID

              Note that this is not UUID v4, as opposed to organization ID and project ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/domains/{domain_id}",
            body=await async_maybe_transform({"deployment_id": deployment_id}, domain_update_params.DomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Domain:
        """
        Get domain details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            f"/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Domain,
        )

    async def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Verify ownership of a domain

        This API triggers the ownership verification of a domain. It should be called
        after necessary DNS records are properly set up.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/domains/{domain_id}/verify",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )
        self.verify = to_raw_response_wrapper(
            domains.verify,
        )

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._domains.certificates)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )
        self.verify = async_to_raw_response_wrapper(
            domains.verify,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._domains.certificates)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )
        self.verify = to_streamed_response_wrapper(
            domains.verify,
        )

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._domains.certificates)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
        self.verify = async_to_streamed_response_wrapper(
            domains.verify,
        )

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._domains.certificates)
