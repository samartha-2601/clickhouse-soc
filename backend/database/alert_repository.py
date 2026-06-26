from backend.database.client import get_client
from backend.models.security_alert import SecurityAlert


class AlertRepository:

    def __init__(self):
        self.client = get_client()

    def insert_alert(self, alert: SecurityAlert):

        self.client.insert(
            "security_alerts",
            [[
                str(alert.alert_id),
                str(alert.event_id) if alert.event_id else None,
                alert.timestamp,
                alert.rule_name,
                alert.severity,
                alert.mitre_tactic,
                alert.mitre_technique,
                alert.status,
                alert.description
            ]],
            column_names=[
                "alert_id",
                "event_id",
                "timestamp",
                "rule_name",
                "severity",
                "mitre_tactic",
                "mitre_technique",
                "status",
                "description"
            ]
        )