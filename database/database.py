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
        query: str,
        workspace_id: str = None,
        node_id: str = None,
    ) -> List[Job]:
        """Allow searching for jobs with a given query

        Args:
            query (str): The query to search for
            workspace_id (str, optional): Workspace to search in. Defaults to None.
            node_id (str, optional): Node to match against. Defaults to None.

        Returns:
            List[Job]: _description_
        """
        ...

    # * Job Runs
    @abstractmethod
    def run_job(
        self,
        job_name: str,
        run_id: str,
        data: dict,
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
        query: str = None,
    ):
        """Get all the runs for a specific job

        Args:
            job_name (str): The job id to get the runs for
            query (str, optional): Optional query to filter unwanted runs. Defaults to None.
        """  # noqa: E501
        # Should just return basic metadata info about the runs, not everything
        ...

    @abstractmethod
    def count_job_runs(
        self,
        job_name: str,
        # TODO: This should take more query parameters
        query: str = None,
    ):
        """Count the job runs for a specific job

        Args:
            job_name (str): The job id to count the runs for
            query (str, optional): Optional query to filter unwanted runs. Defaults to None.
        """  # noqa: E501
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
