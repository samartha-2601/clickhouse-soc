from backend.database.client import get_client
from backend.database.alert_repository import AlertRepository
from backend.detection_engine.rule_loader import load_rules
from backend.services.alert_service import AlertService


class DetectionEngine:

    def __init__(self):

        self.client = get_client()

        self.alert_repository = AlertRepository()

        self.alert_service = AlertService()

        self.rules = load_rules()

    def run(self):

        print("=" * 60)
        print("Detection Engine")
        print("=" * 60)

        for rule in self.rules:

            print(f"\nRunning Rule: {rule.name}")

            results = self.client.query(rule.sql)

            if not results.result_rows:

                print("No detections.")

                continue

            print(f"Detections Found: {len(results.result_rows)}")

            for row in results.result_rows:

                source_ip = row[0]
                username = row[1]
                host = row[2]
                failures = row[3]

                alert = self.alert_service.build_alert(
                    rule=rule,
                    source_ip=source_ip,
                    event_count=failures,
                    username=username,
                    host=host,
                )

                self.alert_repository.insert_alert(alert)

                print(
                    f"Created Alert -> "
                    f"{alert.rule_name} "
                    f"({alert.username} @ {alert.host})"
                )

        print("\nDetection run complete.")