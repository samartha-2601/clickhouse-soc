import uuid
import json
from datetime import datetime

from backend.config import settings
from backend.models.security_investigation import (
    SecurityInvestigation,
)


class InvestigationService:

    def build(
        self,
        incident: dict,
        investigation: dict,
    ):

        timeline = investigation.get("timeline", [])
        containment = investigation.get("containment", [])
        remediation = investigation.get("remediation", [])

        return SecurityInvestigation(

            investigation_id=uuid.uuid4(),

            incident_id=incident["incident_id"],

            created_at=datetime.now(),

            model=settings.OPENAI_MODEL,

            executive_summary=investigation.get(
                "executive_summary",
                "",
            ),

            technical_summary=investigation.get(
                "technical_summary",
                "",
            ),

            root_cause=investigation.get(
                "root_cause",
                "",
            ),

            mitre_analysis=investigation.get(
                "mitre_analysis",
                "",
            ),

            attack_timeline=json.dumps(
                timeline,
                indent=2,
            ),

            containment=json.dumps(
                containment,
                indent=2,
            ),

            remediation=json.dumps(
                remediation,
                indent=2,
            ),

            confidence=float(
                investigation.get(
                    "confidence",
                    0.0,
                )
            ),
        )