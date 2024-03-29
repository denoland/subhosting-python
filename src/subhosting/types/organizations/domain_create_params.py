# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainCreateParams"]


class DomainCreateParams(TypedDict, total=False):
    domain: Required[str]
