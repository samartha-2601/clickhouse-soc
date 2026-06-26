from dataclasses import dataclass


@dataclass
class DetectionRule:

    id: str

    name: str

    description: str

    severity: str

    mitre_tactic: str

    mitre_technique: str

    sql: str