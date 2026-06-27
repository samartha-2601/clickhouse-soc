from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SecurityInvestigation(BaseModel):

    investigation_id: UUID

    incident_id: UUID

    created_at: datetime

    model: str

    executive_summary: str

    technical_summary: str

    root_cause: str

    mitre_analysis: str

    attack_timeline: str

    containment: str

    remediation: str

    confidence: float