import uuid
from datetime import datetime

from backend.simulator.attacks.ssh_bruteforce import SSHBruteForceCampaign
from backend.simulator.models.session import Session

session = Session(
    session_id=uuid.uuid4(),
    username="alice",
    hostname="dev-01",
    source_ip="203.0.113.55",
)

events = SSHBruteForceCampaign.execute(
    session=session,
    start_time=datetime.now(),
)

for event in events:
    print(
        event.timestamp.strftime("%H:%M:%S"),
        event.event_type,
        event.severity,
        event.mitre_technique,
    )