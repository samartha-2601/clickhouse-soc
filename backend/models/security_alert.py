from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from backend.models.alert_status import AlertStatus


class SecurityAlert(BaseModel):

    alert_id: UUID

    event_id: UUID | None = None

    created_at: datetime

    updated_at: datetime

    first_seen: datetime

    last_seen: datetime

    rule_id: str

    rule_name: str

    severity: str

    status: AlertStatus

    source_ip: str

    host: str

    username: str

    event_count: int

    mitre_tactic: str

    mitre_technique: str

    description: str