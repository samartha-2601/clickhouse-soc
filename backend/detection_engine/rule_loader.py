from pathlib import Path

import yaml

from backend.detection_engine.models import DetectionRule


RULES_DIRECTORY = Path("detections")


def load_rules():

    rules = []

    for folder in RULES_DIRECTORY.iterdir():

        if not folder.is_dir():
            continue

        metadata_file = folder / "metadata.yaml"
        sql_file = folder / "detection.sql"

        metadata = yaml.safe_load(metadata_file.read_text())

        sql = sql_file.read_text()

        rules.append(

            DetectionRule(

                id=metadata["id"],

                name=metadata["name"],

                description=metadata["description"],

                severity=metadata["severity"],

                mitre_tactic=metadata["mitre"]["tactic"],

                mitre_technique=metadata["mitre"]["technique"],

                sql=sql

            )

        )

    return rules