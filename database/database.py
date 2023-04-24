from abc import ABC, abstractmethod
from typing import List

from .database_types import Job, RegisterJob, DeleteJob


class Database(ABC):
    # * Static Jobs
    @abstractmethod
    def register_job(
        self,
        workspace_id: str,
        job_name: str,
        # TODO: Add more configurable parameters here
        tags: list[str] | None,
        environment: str | None,
    ) -> RegisterJob:
        ...

    @abstractmethod
    def get_job(
        self,
        workspace_id: str,
        job_name: str,
    ) -> Job:
        ...

    @abstractmethod
    def delete_job(
        self,
        workspace_id: str,
        job_name: str,
    ) -> DeleteJob:
        ...

    @abstractmethod
    def get_jobs(
        self,
        workspace_id: str = None,
        node_id: str = None,
    ) -> List[Job]:
        ...

    # * Job Runs
    @abstractmethod
    def run_job(
        self,
        job_name: str,
        run_id: str,
        # Does this job get called inside of another job?
        parent: str = None,
    ):
        ...

    @abstractmethod
    def get_job_run(
        self,
        run_id: str,
    ):
        ...

    @abstractmethod
    def delete_job_run(
        self,
        run_id: str,
    ):
        ...

    @abstractmethod
    def modify_job_run(
        self,
        run_id: str,
        changes: dict,
    ):
        ...

    @abstractmethod
    def get_job_runs(
        self,
        job_name: str,
        # TODO: This should take more query parameters
    ):
        # Should just return basic metadata info about the runs, not everything
        ...

    @abstractmethod
    def count_job_runs(
        self,
        job_name: str,
        # TODO: This should take more query parameters
    ):
        ...

    @abstractmethod
    def run_task(
        self,
        run_id: str,
        task_id: str,
        # TODO: Should take more options like tags, descriptions, start time, etc
    ):
        ...

    @abstractmethod
    def get_task_run(
        self,
        task_id: str,
    ):
        ...

    @abstractmethod
    def modify_task_run(
        self,
        task_id: str,
        changes: dict,
    ):
        ...
