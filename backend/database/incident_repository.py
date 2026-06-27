from backend.database.client import get_client
from backend.models.security_incident import SecurityIncident


class IncidentRepository:

    def __init__(self):
        self.client = get_client()

    # ---------------------------------------------------------
    # Insert Incident
    # ---------------------------------------------------------
    def insert_incident(
        self,
        incident: SecurityIncident,
    ):

        self.client.insert(

            "security_incidents",

            [[
                str(incident.incident_id),
                incident.created_at,
                incident.updated_at,
                incident.title,
                incident.severity,
                incident.status,
                incident.affected_host,
                incident.affected_user,
                incident.alert_count,
                incident.mitre_tactics,
                incident.timeline,
                incident.ai_summary,
            ]],

            column_names=[
                "incident_id",
                "created_at",
                "updated_at",
                "title",
                "severity",
                "status",
                "affected_host",
                "affected_user",
                "alert_count",
                "mitre_tactics",
                "timeline",
                "ai_summary",
            ],
        )

    # ---------------------------------------------------------
    # Recent Incidents
    # ---------------------------------------------------------
    def get_recent_incidents(
        self,
        limit: int = 100,
    ):

        result = self.client.query(
            """
            SELECT
                incident_id,
                created_at,
                updated_at,
                title,
                severity,
                status,
                affected_host,
                affected_user,
                alert_count,
                mitre_tactics,
                timeline,
                ai_summary
            FROM security_incidents
            ORDER BY created_at DESC
            LIMIT {limit:UInt32}
            """,
            parameters={
                "limit": limit,
            },
        )

        columns = [
            "incident_id",
            "created_at",
            "updated_at",
            "title",
            "severity",
            "status",
            "affected_host",
            "affected_user",
            "alert_count",
            "mitre_tactics",
            "timeline",
            "ai_summary",
        ]

        incidents = []

        for row in result.result_rows:
            incidents.append(dict(zip(columns, row)))

        return incidents

    # ---------------------------------------------------------
    # Single Incident
    # ---------------------------------------------------------
    def get_incident(
        self,
        incident_id: str,
    ):

        result = self.client.query(
            """
            SELECT
                incident_id,
                created_at,
                updated_at,
                title,
                severity,
                status,
                affected_host,
                affected_user,
                alert_count,
                mitre_tactics,
                timeline,
                ai_summary
            FROM security_incidents
            WHERE incident_id = {incident_id:UUID}
            LIMIT 1
            """,
            parameters={
                "incident_id": incident_id,
            },
        )

        if not result.result_rows:
            return None

        row = result.result_rows[0]

        return {
            "incident_id": row[0],
            "created_at": row[1],
            "updated_at": row[2],
            "title": row[3],
            "severity": row[4],
            "status": row[5],
            "affected_host": row[6],
            "affected_user": row[7],
            "alert_count": row[8],
            "mitre_tactics": row[9],
            "timeline": row[10],
            "ai_summary": row[11],
        }