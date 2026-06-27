from enum import Enum


class AlertStatus(str, Enum):

    OPEN = "OPEN"

    ACKNOWLEDGED = "ACKNOWLEDGED"

    INVESTIGATING = "INVESTIGATING"

    RESOLVED = "RESOLVED"

    FALSE_POSITIVE = "FALSE_POSITIVE"