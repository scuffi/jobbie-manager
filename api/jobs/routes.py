from fastapi import APIRouter

from config import Endpoints

jobs_router = APIRouter()


@jobs_router.post(Endpoints.REGISTER_JOB)
def register_job():
    ...


@jobs_router.get(Endpoints.GET_JOB)
def get_job():
    ...


@jobs_router.delete(Endpoints.DELETE_JOB)
def delete_job():
    ...
