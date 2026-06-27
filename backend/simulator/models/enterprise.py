from dataclasses import dataclass

from backend.simulator.models.user import User
from backend.simulator.models.host import Host


@dataclass(frozen=True)
class Enterprise:
    name: str
    users: list[User]
    hosts: list[Host]