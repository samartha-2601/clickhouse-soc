from backend.database.client import get_client
from backend.models.security_event import SecurityEvent


class EventRepository:

    def __init__(self):
        self.client = get_client()

    def insert_event(self, event: SecurityEvent):

        self.client.insert(
            "security_events",

            [[
                str(event.event_id),
                event.timestamp,
                event.source,
                event.host,
                event.username,
                event.source_ip,
                event.destination_ip,
                event.event_type,
                event.severity,
                event.mitre_tactic,
                event.mitre_technique,
                event.message,
                event.raw_log
            ]],

            column_names=[
                "event_id",
                "timestamp",
                "source",
                "host",
                "username",
                "source_ip",
                "destination_ip",
                "event_type",
                "severity",
                "mitre_tactic",
                "mitre_technique",
                "message",
                "raw_log"
            ]
        )