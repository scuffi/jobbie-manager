from abc import ABC, abstractmethod

from .database_types import Job, RegisterJob, DeleteJob


class Database(ABC):
    @abstractmethod
    def register_job(
        workspace_id: str,
        job_name: str,
        tags: list[str] | None,
        environment: str | None,
    ) -> RegisterJob:
        ...

    @abstractmethod
    def get_job(
        workspace_id: str,
        job_name: str,
    ) -> Job:
        ...

    @abstractmethod
    def delete_job(
        workspace_id: str,
        job_name: str,
    ) -> DeleteJob:
        ...
