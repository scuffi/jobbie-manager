from typing import List
import time
import pysurrealdb

from .database import Database, RegisterJob, Job, DeleteJob

from config import Databases


class SurrealDatabase(Database):
    def __init__(self) -> None:
        self.surreal = pysurrealdb.connect(
            host=Databases.SURREAL_HOST,
            port=Databases.SURREAL_PORT,
            user="root",
            password="root",
            namespace="test",
            database="test",
        )

    # * Static Jobs
    def register_job(
        self,
        workspace_id: str,
        job_name: str,
        tags: list[str] | None,
    ) -> RegisterJob:
        """Register a new Job, if already registered, does nothing.

        Args:
            job_name (str): The unique name of this job
            tags (list[str] | None): Any tags that apply to this job
            environment (str | None): The environment this job should run in

        Returns:
            RegisterJob: Status of creation
        """

        if len(self.surreal.query(f"SELECT _ FROM job WHERE job_name == '{job_name}'")):
            return Job.from_list(
                self.surreal.query(f"SELECT * FROM job WHERE job_name == '{job_name}'")
            )

        # TODO: Wrap in a RegisterJob
        return Job.from_list(
            self.surreal.create(
                "job",
                {
                    "job_name": job_name,
                    "workspace": workspace_id,
                    "registered": int(time.time()),
                    "tags": tags,
                },
            )
        )

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
        return self.surreal.get(f"job:{job_id}")

    def delete_job(
        self,
        job_id: str,
    ) -> DeleteJob:
        """Delete a registered job

        Args:
            job_name (str): The unique identifier of this job

        Returns:
            DeleteJob: Database response
        """
        # TODO: Wrap in DeleteJob
        return self.surreal.delete(f"job:{job_id}")

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
        # TODO: Add support for workspace and node id's
        if query:
            return self.surreal.query(f"SELECT * FROM job WHERE {query}")

        return self.surreal.query("SELECT * FROM job")

    # * Job Runs
    def run_job(
        self,
        job_id: str,
        run_id: str,
        tags: List[str] = None,
        version: str = "0.0.1",
    ):
        """Run a registered job

        Args:
            job_name (str): The registered job unique identifier
            run_id (str): A unique identifier for this specific run
            data (dict): Any data this run should hold
            tags (list[str]): Any tags that apply to this job run
            environment (str, optional): The environment this job ran in. Defaults to None.
        """  # noqa: E501
        return self.surreal.create(
            f"run:{run_id}",
            {
                "job_id": job_id,  # TODO: Should this be a reference or just the ID?
                "start_time": int(time.time()),
                "end_time": None,
                "status": "running",
                "tags": tags,
                "tasks": [],
                "version": version,
            },
        )

    def get_job_run(
        self,
        run_id: str,
    ):
        """Get a job run for a specific run

        Args:
            run_id (str): The unique run ID to fetch
        """
        return self.surreal.get(f"run:{run_id}")

    def delete_job_run(
        self,
        run_id: str,
    ):
        """Delete a run job

        Args:
            run_id (str): The unique run ID to delete
        """
        return self.surreal.delete(f"job:{run_id}")

    def modify_job_run(
        self,
        run_id: str,
        changes: dict,
    ):
        """Update a job run, if job doesn't exist, return error

        Args:
            run_id (str): The unique run ID to update
            changes (dict): key-value pair of changes to make
        """
        return self.surreal.update(f"run:{run_id}", changes)

    def get_job_runs(
        self,
        job_id: str,
        query: str = None,
    ):
        """Get all the runs for a specific job

        Args:
            job_name (str): The job id to get the runs for
            query (str, optional): Optional query to filter unwanted runs. Defaults to None.
        """  # noqa: E501
        if query:
            return self.surreal.query(
                f"SELECT * FROM run WHERE job_id == '{job_id}' AND {query}"
            )

        return self.surreal.query(f"SELECT * FROM run WHERE job_id == '{job_id}'")

    def count_job_runs(
        self,
        job_id: str,
        query: str = None,
    ):
        """Count the job runs for a specific job

        Args:
            job_name (str): The job id to count the runs for
            query (str, optional): Optional query to filter unwanted runs. Defaults to None.
        """  # noqa: E501

        # TODO: Refactor to use "SELECT count() AS count FROM job GROUP BY count"
        if query:
            return len(
                self.surreal.query(
                    f"SELECT _ FROM run WHERE job_id == '{job_id}' AND {query}"
                )
            )

        return len(self.surreal.query(f"SELECT _ FROM run WHERE job_id == '{job_id}'"))

    def run_task(
        self,
        run_id: str,
        task_id: str,
        function: str,
        description: str,
        inputs: dict,
        max_retries: int,
        parent: str = None,
    ):
        """Run a task inside of a job

        Args:
            run_id (str): The run ID this task is executed in
            task_id (str): A unique ID for this specific task
            data (dict): Any data this task should hold
            parent (str, optional): The parent this task was called inside of. Defaults to None.
        """  # noqa: E501
        insert = self.surreal.create(
            f"task:{task_id}",
            {
                "run_id": run_id,
                "start_time": int(time.time()),
                "end_time": None,
                "status": "running",
                "inputs": inputs,
                "output": None,
                "function": function,
                "description": description,
                "retries": 0,
                "max_retries": max_retries,
                "children": [],
            },
        )

        if parent:
            self.surreal.query(
                f"UPDATE task:{parent} SET children += ['task:{task_id}']"
            )

        return insert

    def get_task_run(
        self,
        task_id: str,
    ):
        """Get a task run

        Args:
            task_id (str): The unique task run ID
        """
        return self.surreal.get(f"task:{task_id}")

    def get_task_runs(
        self,
        run_id: str,
    ):
        """Get all the run tasks for a given run

        Args:
            run_id (str): The id of the run to get tasks for
        """
        # Should return metadata about the tasks, not all information
        return self.surreal.query(f"SELECT * FROM task WHERE run_id == '{run_id}'")

    def modify_task_run(
        self,
        task_id: str,
        changes: dict,
    ):
        """Update a task run

        Args:
            task_id (str): The unique task run ID to update
            changes (dict): key-value pairs of changes to make
        """
        return self.surreal.update(f"run:{task_id}", changes)
