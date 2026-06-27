import uuid
from datetime import datetime

from backend.models.security_incident import SecurityIncident


class IncidentService:

    def build_incident(
        self,
        *,
        user: str,
        host: str,
        severity: str,
        alert_count: int,
        mitre_tactics: str,
        timeline: str,
    ) -> SecurityIncident:

        now = datetime.now()

        return SecurityIncident(

            incident_id=uuid.uuid4(),

            created_at=now,

            updated_at=now,

            title=f"Security Incident - {user}",

            severity=severity,

            status="OPEN",

            affected_host=host,

            affected_user=user,

            alert_count=alert_count,

            mitre_tactics=mitre_tactics,

            timeline=timeline,
        )