import logging

import psycopg2

from config import config
from src.listener import Listener, PayloadType

conn = psycopg2.connect(
    host=config.DB_HOST,
    port=config.DB_PORT,
    dbname=config.DB_NAME,
    user=config.DB_USERNAME,
    password=config.DB_PASSWORD,
)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

listener = Listener(conn=conn)
logging.basicConfig(level=logging.DEBUG)


def print_payload(payload):
    print(type(payload), payload is None, payload)


@listener.listen('test1', payload_type=PayloadType.STRING)
def on_string(payload: str):
    print_payload(payload)


@listener.listen('test2', payload_type=PayloadType.INTEGER)
def on_integer(payload: int):
    print_payload(payload)


@listener.listen('test3', payload_type=PayloadType.DICT)
def on_json(payload: dict):
    print_payload(payload)


listener.start()
