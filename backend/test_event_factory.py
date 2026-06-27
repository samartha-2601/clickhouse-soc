import uuid

from backend.simulator.models.session import Session
from backend.simulator.services.event_factory import EventFactory


session = Session(
    session_id=uuid.uuid4(),
    username="alice",
    hostname="dev-01",
    source_ip="10.0.0.5",
)

event = EventFactory.create_event(
    session=session,
    event_type="successful_login",
    message="Alice logged in successfully",
)

print(event)