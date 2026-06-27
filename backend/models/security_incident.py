from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SecurityIncident(BaseModel):

    incident_id: UUID

    created_at: datetime

    updated_at: datetime

    title: str

    severity: str

    status: str

    affected_host: str

    affected_user: str

    alert_count: int

    mitre_tactics: str

    timeline: str

    ai_summary: str = ""