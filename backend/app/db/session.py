import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


password = os.environ.get("MPS_DB_PASSWORD")

if not password:
    raise RuntimeError("MPS_DB_PASSWORD environment variable is not set.")

DATABASE_URL = (
    f"postgresql+psycopg://user:{password}"
    "@localhost:5432/mps_dss_dev"
)


engine = create_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
