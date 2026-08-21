from datetime import datetime, timezone

from sqlalchemy.orm import update

from app.db.session import SessionLocal
from app.models.work_center import WorkCenter


work_center_id = 3
expected_version = 2

with SessionLocal() as session:

    
