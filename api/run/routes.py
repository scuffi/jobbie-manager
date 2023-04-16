from fastapi import APIRouter

from config import Endpoints

run_router = APIRouter()


# ! Endpoints for running Jobs


@run_router.post(Endpoints.RUN_JOB)
def run_job():
    ...


@run_router.get(Endpoints.GET_RUN_JOB)
def get_run_job():
    ...


@run_router.patch(Endpoints.UPDATE_RUN_JOB)
def update_run_job():
    ...


@run_router.delete(Endpoints.DELETE_RUN_JOB)
def delete_run_job():
    ...


# ! Endpoints for running tasks


@run_router.post(Endpoints.RUN_TASK)
def run_task():
    ...


@run_router.get(Endpoints.GET_RUN_TASK)
def get_run_task():
    ...


@run_router.patch(Endpoints.UPDATE_RUN_TASK)
def update_run_task():
    ...


# ! Endpoints for querying job/task runs


@run_router.get(Endpoints.GET_JOB_RUNS)
def get_job_runs():
    ...


@run_router.get(Endpoints.COUNT_JOB_RUNS)
def count_job_runs():
    ...


@run_router.get(Endpoints.GET_RUN_JOB_TASKS)
def get_run_job_tasks():
    ...
