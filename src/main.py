import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from queries.orm import SyncORM, AsyncOrm
from queries.core import SyncCore, AsyncCore

SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.insert_resumes()
SyncORM.insert_additional_resumes()

SyncORM.select_workers_with_lazy_relationship()
