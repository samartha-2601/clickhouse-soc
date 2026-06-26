from backend.database.repository import EventRepository
from backend.ingestion.parser import parse_linux_auth_line

repo = EventRepository()

with open("sample_logs/linux/auth.log") as file:

    for line in file:

        event = parse_linux_auth_line(line)

        if event:
            repo.insert_event(event)
            print(
                f"Inserted: {event.event_type} | "
                f"{event.username} | "
                f"{event.source_ip}"
            )