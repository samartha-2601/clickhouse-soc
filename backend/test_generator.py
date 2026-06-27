import uuid

from backend.simulator.generators.authentication import AuthenticationGenerator
from backend.simulator.models.session import Session


session = Session(
    session_id=uuid.uuid4(),
    username="alice",
    hostname="dev-01",
    source_ip="10.0.0.5",
)

events = AuthenticationGenerator.developer_login(session)

for event in events:
    print(event)