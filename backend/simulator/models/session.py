from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class Session:
    session_id: UUID
    username: str
    hostname: str
    source_ip: str