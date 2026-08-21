from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.work_center import WorkCenterResponse
from app.services.work_center import WorkCenterService


router = APIRouter(
    prefix="/work-centers",
    tags=["work-centers"],
)


@router.get("/{code}", response_model=WorkCenterResponse)
def get_work_center(
    code: str,
    db: Session = Depends(get_db),
):
    service = WorkCenterService(db)

    work_center = service.get_by_code(code)

    if work_center is None:
        raise HTTPException(
            status_code=404,
            detail="Work center not found",
        )

    return work_center
