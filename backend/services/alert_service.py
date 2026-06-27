import uuid
from datetime import datetime

from backend.models.alert_status import AlertStatus
from backend.models.security_alert import SecurityAlert


class AlertService:

    def build_alert(
        self,
        rule,
        source_ip,
        event_count,
        username="",
        host="",
    ):

        now = datetime.now()

        return SecurityAlert(

            alert_id=uuid.uuid4(),

            created_at=now,

            updated_at=now,

            first_seen=now,

            last_seen=now,

            rule_id=rule.id,

            rule_name=rule.name,

            severity=rule.severity,

            status=AlertStatus.OPEN,

            source_ip=source_ip,

            host=host,

            username=username,

            event_count=event_count,

            mitre_tactic=rule.mitre_tactic,

            mitre_technique=rule.mitre_technique,

            description=(
                f"{username} on {host} generated "
                f"{event_count} failed SSH logins from {source_ip}"
            )
        )