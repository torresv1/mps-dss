from datetime import datetime, timezone

from sqlalchemy import update

from app.db.session import SessionLocal
from app.models.work_center import WorkCenter


work_center_id = 3
expected_version = 2

with SessionLocal() as session:

    # Simulate another user changing the record first.
    work_center = session.get(WorkCenter, work_center_id)

    if work_center is None:
        raise RuntimeError("Work Center not found.")

    work_center.name = "Stranding Line 1 - Updated by another user"
    work_center.updated_at = datetime.now(timezone.utc)
    work_center.version += 1

    session.commit()

    print(f"Database is now at version: {work_center.version}")

    # Now try to update using the stale version.
    statement = (
        update(WorkCenter)
        .where(
            WorkCenter.work_center_id == work_center_id,
            WorkCenter.version == expected_version,
        )
        .values(
            name="Stranding Line 1 - My Change",
            updated_at=datetime.now(timezone.utc),
            version=WorkCenter.version + 1,
        )
    )

    result = session.execute(statement)

    if result.rowcount == 0:
        session.rollback()
        print(
            "CONCURRENCY CONFLICT: Work Center was modified by another user."
        )
        print("Please refresh before continuing.")
    else:
        session.commit()
        print("Update successful.")
