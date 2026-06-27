from collections import defaultdict

from backend.database.alert_repository import AlertRepository
from backend.database.incident_repository import IncidentRepository
from backend.services.incident_service import IncidentService


class IncidentEngine:

    def __init__(self):

        self.alert_repo = AlertRepository()
        self.incident_repo = IncidentRepository()
        self.incident_service = IncidentService()

    def run(self):

        alerts = self.alert_repo.get_open_alerts()

        print(f"Loaded {len(alerts)} open alerts")

        grouped = defaultdict(list)

        for alert in alerts:

            key = (
                alert.username,
                alert.host,
            )

            grouped[key].append(alert)

        print(f"Found {len(grouped)} incident candidate(s)\n")

        for (user, host), alerts in grouped.items():

            severity = max(
                alert.severity for alert in alerts
            )

            tactics = sorted(
                {
                    alert.mitre_tactic
                    for alert in alerts
                    if alert.mitre_tactic
                }
            )

            timeline = "\n".join(
                alert.description
                for alert in alerts
            )

            incident = self.incident_service.build_incident(
                user=user,
                host=host,
                severity=severity,
                alert_count=len(alerts),
                mitre_tactics=", ".join(tactics),
                timeline=timeline,
            )

            self.incident_repo.insert_incident(incident)

            print(
                f"Created Incident: "
                f"{incident.title}"
            )