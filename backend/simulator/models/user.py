from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    department: str
    role: str
    host: str
    privileged: bool
    