# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    deployment_id: Annotated[Optional[str], PropertyInfo(alias="deploymentId")]
    """A deployment ID

    Note that this is not UUID v4, as opposed to organization ID and project ID.
    """
