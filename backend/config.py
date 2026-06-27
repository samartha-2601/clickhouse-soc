import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
    CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 8123))
    CLICKHOUSE_DATABASE = os.getenv("CLICKHOUSE_DATABASE", "sentinel")

    SIM_NORMAL_SESSIONS = int(os.getenv("SIM_NORMAL_SESSIONS", 1000))
    SIM_ATTACK_SESSIONS = int(os.getenv("SIM_ATTACK_SESSIONS", 50))

    CORRELATION_WINDOW_MINUTES = int(
        os.getenv("CORRELATION_WINDOW_MINUTES", 10)
    )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1-mini"
    )


settings = Settings()