from fastapi import APIRouter

run_router = APIRouter()


# ! Endpoints for running Jobs


@run_router.post()
def run_job():
    ...


@run_router.get()
def get_run_job():
    ...


@run_router.patch()
def update_run_job():
    ...


@run_router.delete()
def delete_run_job():
    ...


# ! Endpoints for running tasks


@run_router.post()
def run_task():
    ...


@run_router.get()
def get_run_task():
    ...


@run_router.patch()
def update_run_task():
    ...


# ! Endpoints for querying job/task runs


@run_router.get()
def get_job_runs():
    ...


@run_router.get()
def count_job_runs():
    ...


@run_router.get()
def get_run_job_tasks():
    ...
