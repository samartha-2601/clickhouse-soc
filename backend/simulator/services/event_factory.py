import uuid
from datetime import datetime

from backend.models.security_event import SecurityEvent
from backend.simulator.models.session import Session


class EventFactory:

    @staticmethod
    def create_event(
        session: Session,
        event_type: str,
        severity: str = "low",
        message: str = "",
        destination_ip: str = "",
        mitre_tactic: str = "",
        mitre_technique: str = "",
        timestamp: datetime | None = None,
    ) -> SecurityEvent:
        
        event_time = timestamp or datetime.now()

        return SecurityEvent(

            event_id=uuid.uuid4(),

            timestamp=event_time,

            source="simulator",

            host=session.hostname,

            username=session.username,

            source_ip=session.source_ip,

            destination_ip=destination_ip,

            event_type=event_type,

            severity=severity,

            mitre_tactic=mitre_tactic,

            mitre_technique=mitre_technique,

            message=message,

            raw_log=message,

            
        )