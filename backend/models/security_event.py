from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SecurityEvent(BaseModel):
    event_id: UUID

    timestamp: datetime

    source: str

    host: str

    username: str

    source_ip: str

    destination_ip: str

    event_type: str

    severity: str

    mitre_tactic: str

    mitre_technique: str

    message: str

    raw_log: str