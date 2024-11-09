import asyncio
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import insert_data, insert_data_async
from queries.core import create_tables

create_tables()
asyncio.run(insert_data_async())

