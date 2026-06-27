import random
import uuid
from datetime import datetime

from backend.simulator.generators.administrator import AdministratorGenerator
from backend.simulator.generators.authentication import AuthenticationGenerator
from backend.simulator.generators.windows import WindowsGenerator
from backend.simulator.attacks.ssh_bruteforce import SSHBruteForceCampaign
from backend.simulator.models.session import Session
from backend.simulator.services.simulator import build_demo_enterprise


class BulkSimulator:

    def __init__(self):

        self.enterprise = build_demo_enterprise()

    def generate(
        self,
        normal_sessions=200,
        attack_sessions=10,
    ):

        events = []

        # Normal enterprise activity
        for _ in range(normal_sessions):

            user = random.choice(self.enterprise.users)

            session = Session(
                session_id=uuid.uuid4(),
                username=user.username,
                hostname=user.host,
                source_ip=f"10.0.0.{random.randint(10,250)}",
            )

            if user.role == "Developer":

                events.extend(
                    AuthenticationGenerator.developer_login(session)
                )

            elif user.role == "Administrator":

                events.extend(
                    AdministratorGenerator.maintenance(session)
                )

            else:

                events.extend(
                    WindowsGenerator.office_user(session)
                )

        # Inject attack campaigns
        for _ in range(attack_sessions):

            session = Session(
                session_id=uuid.uuid4(),
                username="alice",
                hostname="dev-01",
                source_ip=f"203.0.113.{random.randint(1,50)}",
            )

            events.extend(
                SSHBruteForceCampaign.execute(
                    session,
                    datetime.now(),
                )
            )

        return events