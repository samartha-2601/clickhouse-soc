import uuid

from backend.simulator.generators.authentication import AuthenticationGenerator
from backend.simulator.generators.windows import WindowsGenerator
from backend.simulator.generators.administrator import AdministratorGenerator
from backend.simulator.models.session import Session


session = Session(
    session_id=uuid.uuid4(),
    username="alice",
    hostname="dev-01",
    source_ip="10.0.0.5",
)

print("=" * 60)
print("Developer")
print("=" * 60)

for event in AuthenticationGenerator.developer_login(session):
    print(event.event_type)

print()

print("=" * 60)
print("Windows User")
print("=" * 60)

for event in WindowsGenerator.office_user(session):
    print(event.event_type)

print()

print("=" * 60)
print("Administrator")
print("=" * 60)

for event in AdministratorGenerator.maintenance(session):
    print(event.event_type)