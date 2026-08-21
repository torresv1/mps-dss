from app.db.session import SessionLocal
from app.repositories.work_center import WorkCenterRepository


with SessionLocal() as session:
    repository = WorkCenterRepository(session)

    work_center = repository.get_by_code("STR-01")

    if work_center is None:
        print("Work center not found.")
    else:
        print("Work center found")
        print(f"ID: {work_center.work_center_id}")
        print(f"Code: {work_center.code}")
        print(f"Name: {work_center.name}")
        print(f"Version: {work_center.version}")
