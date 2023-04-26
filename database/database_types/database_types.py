from dataclasses import dataclass, asdict

from typing import List


class BaseClass:
    @classmethod
    def from_list(cls, objects):
        return [cls(**object) for object in objects]

    def dict(self):
        return asdict(self)

    def __repr__(self) -> str:
        return str(self.dict())

    __str__ = __repr__


@dataclass
class Job(BaseClass):
    id: str
    job_name: str
    workspace: str
    registered: int
    tags: List[str]


@dataclass
class DeleteJob:
    ...
