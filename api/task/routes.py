from fastapi import APIRouter
from typing import Optional
import uuid

from config import Endpoints

from database import SurrealDatabase

database = SurrealDatabase()

task_router = APIRouter(tags=["Tasks"])


# ! Endpoints for running Jobs


@task_router.post(Endpoints.RUN_TASK)
def run_task(
    run_id: str,
    function_name: str,
    inputs: dict,
    max_retries: int = 0,
    task_id: Optional[str] = None,
    description: Optional[str] = None,
    parent: Optional[str] = None,
):
    return database.run_task(
        run_id=run_id,
        task_id=task_id or str(uuid.uuid4()),
        function=function_name,
        inputs=inputs,
        max_retries=max_retries,
        description=description,
        parent=parent,
    )


@task_router.get(Endpoints.GET_RUN_TASK)
def get_task(task_id: str):
    return database.get_task_run(task_id)


@task_router.get(Endpoints.GET_RUN_JOB_TASKS)
def get_tasks(run_id: str):
    return database.get_task_runs(run_id)


@task_router.patch(Endpoints.UPDATE_RUN_TASK)
def modify_task(task_id: str, changes: dict):
    return database.modify_task_run(
        task_id=task_id,
        changes=changes,
    )
