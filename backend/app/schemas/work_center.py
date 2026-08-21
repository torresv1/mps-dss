from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkCenterCreate(BaseModel):
    code: str
    name: str
    description: str | None = None


class WorkCenterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    work_center_id: int
    code: str
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime
    version: int
