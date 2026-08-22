from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.work_centers import router as work_centers_router
from app.core.exceptions import DuplicateWorkCenterCodeError


app = FastAPI(
    title="Manufacturing Planning & Scheduling DSS",
    version="0.1.0",
)


@app.exception_handler(DuplicateWorkCenterCodeError)
async def duplicate_work_center_code_handler(
    request: Request,
    exc: DuplicateWorkCenterCodeError
):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )


app.include_router(work_centers_router)
