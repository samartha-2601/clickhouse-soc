import uuid
from datetime import datetime

from backend.database.client import get_client
from backend.database.alert_repository import AlertRepository
from backend.detection_engine.rule_loader import load_rules
from backend.models.security_alert import SecurityAlert


class DetectionEngine:

    def __init__(self):

        self.client = get_client()

        self.alert_repo = AlertRepository()

        self.rules = load_rules()

    def run(self):

        print(f"Loaded {len(self.rules)} detection rule(s)\n")

        for rule in self.rules:

            print(f"Running: {rule.name}")

            results = self.client.query(rule.sql)

            if not results.result_rows:

                print("No detections.\n")

                continue

            print(f"Found {len(results.result_rows)} detection(s)\n")

            for row in results.result_rows:

                source_ip = row[0]

                failures = row[1]

                alert = SecurityAlert(

                    alert_id=uuid.uuid4(),

                    timestamp=datetime.now(),

                    rule_id=rule.id,

                    rule_name=rule.name,

                    severity=rule.severity,

                    mitre_tactic=rule.mitre_tactic,

                    mitre_technique=rule.mitre_technique,

                    status="OPEN",

                    description=(
                        f"{source_ip} generated "
                        f"{failures} failed SSH logins."
                    )
                )

                self.alert_repo.insert_alert(alert)

                print(f"Alert created for {source_ip}")