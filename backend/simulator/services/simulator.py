from backend.simulator.models.enterprise import Enterprise
from backend.simulator.models.host import Host
from backend.simulator.models.user import User


def build_demo_enterprise() -> Enterprise:

    users = [
        User("alice", "Engineering", "Developer", "dev-01", False),
        User("bob", "Finance", "Analyst", "fin-01", False),
        User("charlie", "IT", "Administrator", "jumpbox", True),
        User("jenkins", "DevOps", "Service Account", "ci-server", True),
    ]

    hosts = [
        Host("dev-01", "Linux", "Engineering", "Medium"),
        Host("fin-01", "Windows", "Finance", "High"),
        Host("jumpbox", "Linux", "IT", "Critical"),
        Host("ci-server", "Linux", "DevOps", "High"),
    ]

    return Enterprise(
        name="Acme Corporation",
        users=users,
        hosts=hosts,
    )