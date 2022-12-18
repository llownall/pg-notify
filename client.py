import logging
import time

import psycopg2

from config import config
from src.notifier import Notifier

conn = psycopg2.connect(
    host=config.DB_HOST,
    port=config.DB_PORT,
    dbname=config.DB_NAME,
    user=config.DB_USERNAME,
    password=config.DB_PASSWORD,
)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

notifier = Notifier(conn=conn)
logging.basicConfig(level=logging.DEBUG)

notifier.notify('test1', '123')
time.sleep(1)

notifier.notify('test2', 123)
time.sleep(1)

notifier.notify('test3', {'a': 1})
time.sleep(1)

notifier.notify('test2', 'qwe')
