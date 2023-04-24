import asyncio
from typing import List

from surrealdb import SurrealHTTP

from .database import Database, RegisterJob, Job, DeleteJob

from config import Databases


class SurrealDatabase(Database):
    def __init__(self) -> None:
        self.surreal: SurrealHTTP = SurrealHTTP(
            Databases.SURREAL,
            username="root",
            password="root",
            namespace="ns",
            database="db",
        )

        asyncio.run(self.surreal.connect())

    def _create(self, id: str, data: dict):
        return asyncio.run(self.surreal.create(id, data))

    def _select(self, id: str):
        return asyncio.run(self.surreal.select(id))

    def _update(self, id: str, data: dict):
        return asyncio.run(self.surreal.update(id, data))

    def _delete(self, id: str):
        return asyncio.run(self.surreal.delete(id))

    def _query(self, query: str, data: dict = None):
        return asyncio.run(self.surreal.query(query, data))

    # * Static Jobs
    def register_job(
        self,
        workspace_id: str,
        job_name: str,
        # TODO: Add more configurable parameters here
        tags: list[str] | None,
        environment: str | None,
    ) -> RegisterJob:
        ...

    def get_job(
        self,
        workspace_id: str,
        job_name: str,
    ) -> Job:
        ...

    def delete_job(
        self,
        workspace_id: str,
        job_name: str,
    ) -> DeleteJob:
        ...

    def get_jobs(
        self,
        workspace_id: str = None,
        node_id: str = None,
    ) -> List[Job]:
        ...

    # * Job Runs
    def run_job(
        self,
        job_name: str,
        run_id: str,
        # Does this job get called inside of another job?
        parent: str = None,
    ):
        ...

    def get_job_run(
        self,
        run_id: str,
    ):
        ...

    def delete_job_run(
        self,
        run_id: str,
    ):
        ...

    def modify_job_run(
        self,
        run_id: str,
        changes: dict,
    ):
        ...

    def get_job_runs(
        self,
        job_name: str,
        # TODO: This should take more query parameters
    ):
        # Should just return basic metadata info about the runs, not everything
        ...

    def count_job_runs(
        self,
        job_name: str,
        # TODO: This should take more query parameters
    ):
        ...

    def run_task(
        self,
        run_id: str,
        task_id: str,
        # TODO: Should take more options like tags, descriptions, start time, etc
    ):
        ...

    def get_task_run(
        self,
        task_id: str,
    ):
        ...

    def modify_task_run(
        self,
        task_id: str,
        changes: dict,
    ):
        ...
