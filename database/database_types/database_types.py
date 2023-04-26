from dataclasses import dataclass, asdict

from typing import List, Dict, Optional


class BaseClass:
    @classmethod
    def from_list(cls, objects):
        return [cls(**object) for object in objects]

    def dict(self, id: bool = True):
        value = asdict(self)

        if id:
            return value

        del value["id"]
        return value

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
class Run(BaseClass):
    id: str
    job_id: str
    start_time: int
    end_time: Optional[int]
    status: str
    tags: List[str]
    version: str


@dataclass
class Task(BaseClass):
    id: str
    run_id: str
    start_time: int
    status: str
    inputs: Dict[str, str]
    output: Dict[str, str]
    function: str
    retries: int
    max_retries: int
    children: List[str]
    end_time: Optional[int]
    description: Optional[str]
