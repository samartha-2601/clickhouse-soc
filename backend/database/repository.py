from backend.database.client import get_client
from backend.models.security_event import SecurityEvent


class EventRepository:

    def __init__(self):
        self.client = get_client()

    # ---------------------------------------------------------
    # Insert Single Event
    # ---------------------------------------------------------
    def insert_event(
        self,
        event: SecurityEvent,
    ):

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
                event.raw_log,
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
                "raw_log",
            ],
        )

    # ---------------------------------------------------------
    # Bulk Insert
    # ---------------------------------------------------------
    def insert_events(
        self,
        events: list[SecurityEvent],
    ):

        rows = []

        for event in events:

            rows.append([
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
                event.raw_log,
            ])

        self.client.insert(
            "security_events",
            rows,
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
                "raw_log",
            ],
        )

    # ---------------------------------------------------------
    # Event Search API
    # ---------------------------------------------------------
    def get_events(
        self,
        limit: int = 100,
        offset: int = 0,
        username: str | None = None,
        host: str | None = None,
        severity: str | None = None,
        event_type: str | None = None,
    ):

        query = """
        SELECT
            event_id,
            timestamp,
            source,
            host,
            username,
            source_ip,
            destination_ip,
            event_type,
            severity,
            mitre_tactic,
            mitre_technique,
            message,
            raw_log
        FROM security_events
        WHERE 1 = 1
        """

        parameters = {}

        if username:
            query += " AND username={username:String}"
            parameters["username"] = username

        if host:
            query += " AND host={host:String}"
            parameters["host"] = host

        if severity:
            query += " AND severity={severity:String}"
            parameters["severity"] = severity

        if event_type:
            query += " AND event_type={event_type:String}"
            parameters["event_type"] = event_type

        query += """
        ORDER BY timestamp DESC
        LIMIT {limit:UInt32}
        OFFSET {offset:UInt32}
        """

        parameters["limit"] = limit
        parameters["offset"] = offset

        result = self.client.query(
            query,
            parameters=parameters,
        )

        columns = [
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
            "raw_log",
        ]

        events = []

        for row in result.result_rows:
            events.append(dict(zip(columns, row)))

        return events

    # ---------------------------------------------------------
    # Timeline for AI Investigation
    # ---------------------------------------------------------
    def get_events_for_incident(
        self,
        username: str,
        host: str,
    ):

        result = self.client.query(
            """
            SELECT
                event_id,
                timestamp,
                source,
                host,
                username,
                source_ip,
                destination_ip,
                event_type,
                severity,
                mitre_tactic,
                mitre_technique,
                message,
                raw_log
            FROM security_events
            WHERE username={username:String}
              AND host={host:String}
            ORDER BY timestamp
            """,
            parameters={
                "username": username,
                "host": host,
            },
        )

        columns = [
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
            "raw_log",
        ]

        events = []

        for row in result.result_rows:
            events.append(dict(zip(columns, row)))

        return events