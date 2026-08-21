from sqlalchemy.orm import Session

from app.models.work_center import WorkCenter


class WorkCenterRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, work_center_id: int) -> WorkCenter | None:
        return self.session.get(WorkCenter, work_center_id)

    def get_by_code(self, code: str) -> WorkCenter | None:
        return (
            self.session.query(WorkCenter)
            .filter(WorkCenter.code == code)
            .first()
        )
