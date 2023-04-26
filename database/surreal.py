# from typing import List

import pysurrealdb

from .database import Database  # , RegisterJob, Job, DeleteJob

from config import Databases


class SurrealDatabase(Database):
    def __init__(self) -> None:
        self.surreal = pysurrealdb.connect(
            host=Databases.SURREAL_HOST,
            port=Databases.SURREAL_PORT,
            user="root",
            password="root",
            namespace="ns",
            database="db",
        )
