from dataclasses import dataclass


@dataclass(frozen=True)
class Host:
    hostname: str
    operating_system: str
    department: str
    criticality: str