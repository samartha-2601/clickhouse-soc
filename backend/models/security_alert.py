from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SecurityAlert(BaseModel):
    alert_id: UUID

    event_id: UUID | None = None

    timestamp: datetime

    rule_id: str

    rule_name: str

    severity: str

    mitre_tactic: str

    mitre_technique: str

    status: str

    description: str