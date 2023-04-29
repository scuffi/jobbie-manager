from fastapi import APIRouter, Response, status
from typing import Optional, List

from config import Endpoints

from database import SurrealDatabase

database = SurrealDatabase()

jobs_router = APIRouter(tags=["Jobs"])


@jobs_router.post(Endpoints.REGISTER_JOB)
def register_job(workspace: str, job: str, tags: Optional[List[str]] = None):
    return [job.dict() for job in database.register_job(workspace, job, tags)]


@jobs_router.get(Endpoints.GET_JOB)
def get_job(job: str):
    job_doc = database.get_job(job)

    if job is not None:
        return job_doc.dict()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# TODO: Should this be QUERY?
@jobs_router.get(Endpoints.GET_JOBS)
def get_jobs(
    query: Optional[str] = None,
    workspace: Optional[str] = None,
    node: Optional[str] = None,
):
    return database.get_jobs(query, workspace, node)


@jobs_router.delete(Endpoints.DELETE_JOB)
def delete_job(job: str):
    return database.delete_job(job)
