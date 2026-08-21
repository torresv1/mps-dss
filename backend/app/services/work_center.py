from sqlalchemy.orm import Session

from app.repositories.work_center import WorkCenterRepository


class WorkCenterService:

    def __init__(self, session: Session):
        self.repository = WorkCenterRepository(session)

    def get_by_code(self, code: str):
        return self.repository.get_by_code(code)
