# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DatabaseCreateParams"]


class DatabaseCreateParams(TypedDict, total=False):
    description: Optional[str]
    """The description of the KV database.

    If this is `null`, an empty string will be set.
    """
