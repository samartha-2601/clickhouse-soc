from dataclasses import dataclass
from enum import Enum


class ActorType(str, Enum):
    EMPLOYEE = "employee"
    ADMINISTRATOR = "administrator"
    SERVICE_ACCOUNT = "service_account"
    ATTACKER = "attacker"


@dataclass(frozen=True)
class Actor:
    username: str
    actor_type: ActorType
    department: str
    host: str
    privileged: bool