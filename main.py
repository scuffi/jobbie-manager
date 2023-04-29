import uvicorn
from fastapi import FastAPI

from api import jobs_router, run_router, task_router

api = FastAPI(title="Jobbie API")

api.include_router(jobs_router)
api.include_router(run_router)
api.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=3000, reload=True)
