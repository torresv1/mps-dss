from fastapi import FastAPI

from app.api.work_centers import router as work_centers_router


app = FastAPI(
    title="Manufacturing Planning & Scheduling DSS",
    version="0.1.0",
)

app.include_router(work_centers_router)
