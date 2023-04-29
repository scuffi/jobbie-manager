from fastapi import APIRouter
from typing import Optional, List
import uuid

from config import Endpoints

from database import SurrealDatabase

database = SurrealDatabase()

run_router = APIRouter(tags=["Run"])


# ! Endpoints for running Jobs


@run_router.post(Endpoints.RUN_JOB)
def run_job(
    job_id: str,
    version: str,
    tags: Optional[List[str]] = None,
    run_id: Optional[str] = None,
):
    return database.run_job(
        job_id=job_id,
        run_id=run_id or str(uuid.uuid4()),
        tags=tags or [],
        version=version,
    )


@run_router.get(Endpoints.GET_RUN_JOB)
def get_run_job(run_id: str):
    return database.get_job_run(run_id)


@run_router.get(Endpoints.GET_JOB_RUNS)
def get_job_runs(job_id: Optional[str] = None, query: Optional[str] = None):
    return database.get_job_runs(
        job_id=job_id,
        query=query,
    )


@run_router.patch(Endpoints.UPDATE_RUN_JOB)
def update_run_job(run_id: str, changes: dict):
    return database.modify_job_run(
        run_id=run_id,
        changes=changes,
    )


@run_router.delete(Endpoints.DELETE_RUN_JOB)
def delete_run_job(run_id: str):
    return database.delete_job_run(run_id)


@run_router.get(Endpoints.COUNT_JOB_RUNS)
def count_job_runs(job_id: str, query: Optional[str] = None):
    return database.count_job_runs(job_id=job_id, query=query)
