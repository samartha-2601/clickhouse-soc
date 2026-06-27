from backend.database.client import get_client
from backend.models.alert_status import AlertStatus
from backend.models.security_alert import SecurityAlert


class AlertRepository:

    def __init__(self):
        self.client = get_client()

    # ---------------------------------------------------------
    # Insert Alert
    # ---------------------------------------------------------
    def insert_alert(
        self,
        alert: SecurityAlert,
    ):

        self.client.insert(
            "security_alerts",
            [[
                str(alert.alert_id),
                str(alert.event_id) if alert.event_id else None,
                alert.created_at,
                alert.updated_at,
                alert.first_seen,
                alert.last_seen,
                alert.rule_id,
                alert.rule_name,
                alert.severity,
                alert.status.value,
                alert.source_ip,
                alert.host,
                alert.username,
                alert.event_count,
                alert.mitre_tactic,
                alert.mitre_technique,
                alert.description,
            ]],
            column_names=[
                "alert_id",
                "event_id",
                "created_at",
                "updated_at",
                "first_seen",
                "last_seen",
                "rule_id",
                "rule_name",
                "severity",
                "status",
                "source_ip",
                "host",
                "username",
                "event_count",
                "mitre_tactic",
                "mitre_technique",
                "description",
            ],
        )

    # ---------------------------------------------------------
    # Open Alerts
    # ---------------------------------------------------------
    def get_open_alerts(self) -> list[SecurityAlert]:

        result = self.client.query(
            """
            SELECT
                alert_id,
                event_id,
                created_at,
                updated_at,
                first_seen,
                last_seen,
                rule_id,
                rule_name,
                severity,
                status,
                source_ip,
                host,
                username,
                event_count,
                mitre_tactic,
                mitre_technique,
                description
            FROM security_alerts
            WHERE status='OPEN'
            """
        )

        alerts = []

        for row in result.result_rows:

            alerts.append(
                SecurityAlert(
                    alert_id=row[0],
                    event_id=row[1],
                    created_at=row[2],
                    updated_at=row[3],
                    first_seen=row[4],
                    last_seen=row[5],
                    rule_id=row[6],
                    rule_name=row[7],
                    severity=row[8],
                    status=AlertStatus(row[9]),
                    source_ip=row[10],
                    host=row[11],
                    username=row[12],
                    event_count=row[13],
                    mitre_tactic=row[14],
                    mitre_technique=row[15],
                    description=row[16],
                )
            )

        return alerts

    # ---------------------------------------------------------
    # Recent Alerts
    # ---------------------------------------------------------
    def get_recent_alerts(
        self,
        limit: int = 100,
    ):

        result = self.client.query(
            """
            SELECT
                alert_id,
                event_id,
                created_at,
                updated_at,
                first_seen,
                last_seen,
                rule_id,
                rule_name,
                severity,
                status,
                source_ip,
                host,
                username,
                event_count,
                mitre_tactic,
                mitre_technique,
                description
            FROM security_alerts
            ORDER BY created_at DESC
            LIMIT {limit:UInt32}
            """,
            parameters={
                "limit": limit,
            },
        )

        columns = [
            "alert_id",
            "event_id",
            "created_at",
            "updated_at",
            "first_seen",
            "last_seen",
            "rule_id",
            "rule_name",
            "severity",
            "status",
            "source_ip",
            "host",
            "username",
            "event_count",
            "mitre_tactic",
            "mitre_technique",
            "description",
        ]

        alerts = []

        for row in result.result_rows:
            alerts.append(dict(zip(columns, row)))

        return alerts

    # ---------------------------------------------------------
    # Alerts for Incident
    # ---------------------------------------------------------
    def get_alerts_for_incident(
        self,
        username: str,
        host: str,
    ):

        result = self.client.query(
            """
            SELECT
                alert_id,
                event_id,
                created_at,
                updated_at,
                first_seen,
                last_seen,
                rule_id,
                rule_name,
                severity,
                status,
                source_ip,
                host,
                username,
                event_count,
                mitre_tactic,
                mitre_technique,
                description
            FROM security_alerts
            WHERE username={username:String}
              AND host={host:String}
            ORDER BY created_at
            """,
            parameters={
                "username": username,
                "host": host,
            },
        )

        columns = [
            "alert_id",
            "event_id",
            "created_at",
            "updated_at",
            "first_seen",
            "last_seen",
            "rule_id",
            "rule_name",
            "severity",
            "status",
            "source_ip",
            "host",
            "username",
            "event_count",
            "mitre_tactic",
            "mitre_technique",
            "description",
        ]

        alerts = []

        for row in result.result_rows:
            alerts.append(dict(zip(columns, row)))

        return alerts