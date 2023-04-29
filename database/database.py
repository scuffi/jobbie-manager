from abc import ABC, abstractmethod
from typing import List

from .database_types import Job, Run, Task


class Database(ABC):
    # * Static Jobs
    @abstractmethod
    def register_job(
        self,
        workspace_id: str,
        job_name: str,
        tags: list[str] | None,
    ) -> List[Job]:
        """Register a new Job, if already registered, does nothing.

        Args:
            job_name (str): The unique name of this job
            tags (list[str] | None): Any tags that apply to this job
            environment (str | None): The environment this job should run in

        Returns:
            RegisterJob: Status of creation
        """
        ...

    @abstractmethod
    def get_job(
        self,
        job_id: str,
    ) -> Job:
        """Get information about a registered job

        Args:
            job_name (str): The unique identifier of this job

        Returns:
            Job: The job
        """
        ...

    @abstractmethod
    def delete_job(
        self,
        job_id: str,
    ) -> None:
        """Delete a registered job

        Args:
            job_name (str): The unique identifier of this job

        Returns:
            DeleteJob: Database response
        """
        ...

    @abstractmethod
    def get_jobs(
        self,
        query: str = None,
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
        job_id: str,
        run_id: str,
        tags: List[str] = None,
        version: str = None,
    ) -> Run:
        """Run a registered job

        Args:
            job_name (str): The registered job unique identifier
            run_id (str): A unique identifier for this specific run
            data (dict): Any data this run should hold
            tags (list[str]): Any tags that apply to this job run
            environment (str, optional): The environment this job ran in. Defaults to None.
        """  # noqa: E501
        ...

    @abstractmethod
    def get_job_run(
        self,
        run_id: str,
    ) -> Run:
        """Get a job run for a specific run

        Args:
            run_id (str): The unique run ID to fetch
        """
        ...

    @abstractmethod
    def delete_job_run(
        self,
        run_id: str,
    ) -> None:
        """Delete a run job

        Args:
            run_id (str): The unique run ID to delete
        """
        ...

    @abstractmethod
    def modify_job_run(
        self,
        run_id: str,
        changes: dict,
    ) -> Run:
        """Update a job run, if job doesn't exist, return error

        Args:
            run_id (str): The unique run ID to update
            changes (dict): key-value pair of changes to make
        """
        ...

    @abstractmethod
    def get_job_runs(
        self,
        job_name: str,
        query: str = None,
    ) -> List[Run]:
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
        query: str = None,
    ) -> int:
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
        function: str,
        description: str,
        inputs: dict,
        max_retries: int,
        parent: str = None,
    ) -> Task:
        """Run a task inside of a job

        Args:
            run_id (str): The run ID this task is executed in
            task_id (str): A unique ID for this specific task
            data (dict): Any data this task should hold
            parent (str, optional): The parent this task was called inside of. Defaults to None.
        """  # noqa: E501
        ...

    @abstractmethod
    def get_task_run(
        self,
        task_id: str,
    ) -> Task:
        """Get a task run

        Args:
            task_id (str): The unique task run ID
        """
        ...

    @abstractmethod
    def get_task_runs(
        self,
        run_id: str,
    ) -> List[Task]:
        """Get all the run tasks for a given run

        Args:
            run_id (str): The id of the run to get tasks for
        """
        # Should return metadata about the tasks, not all information
        ...

    @abstractmethod
    def modify_task_run(
        self,
        task_id: str,
        changes: dict,
    ) -> Task:
        """Update a task run

        Args:
            task_id (str): The unique task run ID to update
            changes (dict): key-value pairs of changes to make
        """
        ...

    @abstractmethod
    def create_workspace(workspace_id: str, workspace_name: str):
        """Create a workspace with a given name

        Args:
            workspace_id (str): Unique identifier for the workspace
            workspace_name (str): The name of the workspace
        """
        ...

    @abstractmethod
    def change_workspace_permission(user: str, type: str, allow: bool):
        """Change the permissions for a given user in this workspace.

        Args:
            user (str): The user to change permissions for
            type (str): The 'type' of permission, i.e. 'select', 'create', 'update', etc
            allow (bool): Is this permssion allow or not?
        """
        ...

    @abstractmethod
    def update_workspace(workspace_id: str, changes: dict):
        """Update a workspace

        Args:
            workspace_id (str): The workspace to update
            changes (dict): The changes to be made
        """
        ...

    @abstractmethod
    def delete_workspace(workspace_id: str):
        """Delete a workspace

        Args:
            workspace_id (str): The workspace to delete
        """
        ...
