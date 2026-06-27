import json

from backend.database.client import get_client
from backend.models.security_investigation import (
    SecurityInvestigation,
)


class InvestigationRepository:

    def __init__(self):

        self.client = get_client()

    def insert_investigation(
        self,
        investigation: SecurityInvestigation,
    ):

        self.client.insert(

            "security_investigations",

            [[
                str(investigation.investigation_id),
                str(investigation.incident_id),
                investigation.created_at,
                investigation.model,
                investigation.executive_summary,
                investigation.technical_summary,
                investigation.root_cause,
                investigation.mitre_analysis,
                investigation.attack_timeline,
                investigation.containment,
                investigation.remediation,
                investigation.confidence,
            ]],

            column_names=[
                "investigation_id",
                "incident_id",
                "created_at",
                "model",
                "executive_summary",
                "technical_summary",
                "root_cause",
                "mitre_analysis",
                "attack_timeline",
                "containment",
                "remediation",
                "confidence",
            ],
        )

    def get_investigation(
        self,
        incident_id: str,
    ):

        result = self.client.query(
            """
            SELECT
                investigation_id,
                incident_id,
                created_at,
                model,
                executive_summary,
                technical_summary,
                root_cause,
                mitre_analysis,
                attack_timeline,
                containment,
                remediation,
                confidence
            FROM security_investigations
            WHERE incident_id={incident_id:UUID}
            LIMIT 1
            """,
            parameters={
                "incident_id": incident_id
            },
        )

        if not result.result_rows:
            return None

        row = result.result_rows[0]

        return SecurityInvestigation(

            investigation_id=row[0],

            incident_id=row[1],

            created_at=row[2],

            model=row[3],

            executive_summary=row[4],

            technical_summary=row[5],

            root_cause=row[6],

            mitre_analysis=row[7],

            attack_timeline=row[8],

            containment=row[9],

            remediation=row[10],

            confidence=row[11],
        )