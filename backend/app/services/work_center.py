from sqlalchemy.orm import Session

from app.repositories.work_center import WorkCenterRepository
from app.models.work_center import WorkCenter
from app.schemas.work_center import WorkCenterCreate

from app.core.exceptions import DuplicateWorkCenterCodeError


class WorkCenterService:

    def __init__(self, session: Session):
        self.repository = WorkCenterRepository(session)
        self.session = session

    def get_by_code(self, code: str):
        return self.repository.get_by_code(code)

    def create(self, data: WorkCenterCreate) -> WorkCenter:
        existing = self.repository.get_by_code(data.code)

        if existing is not None:
            raise DuplicateWorkCenterCodeError(
                f"Work center with code '{data.code}' already exists."
            )

        work_center = WorkCenter(
            code=data.code,
            name=data.name,
            description=data.description,
        )

        self.repository.create(work_center)

        self.session.commit()
        self.session.refresh(work_center)

        return work_center
