# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .forward_paging import ForwardPaging

__all__ = ["ActivityGetAuditLogsResponse", "Result", "ResultActingUser"]


class ResultActingUser(BaseModel):
    user_id: int = FieldInfo(alias="userId")

    user_email: Optional[str] = FieldInfo(alias="userEmail", default=None)


class Result(BaseModel):
    id: str

    acting_user: ResultActingUser = FieldInfo(alias="actingUser")

    action: str

    category: str

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)

    target_object_id: Optional[str] = FieldInfo(alias="targetObjectId", default=None)


class ActivityGetAuditLogsResponse(BaseModel):
    results: List[Result]

    paging: Optional[ForwardPaging] = None
