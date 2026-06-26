import os

import clickhouse_connect

from dotenv import load_dotenv

load_dotenv()


def get_client():
    return clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST"),
        port=int(os.getenv("CLICKHOUSE_PORT")),
        username=os.getenv("CLICKHOUSE_USERNAME"),
        password=os.getenv("CLICKHOUSE_PASSWORD"),
        database=os.getenv("CLICKHOUSE_DATABASE"),
    )