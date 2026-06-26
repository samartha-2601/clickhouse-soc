import re
import uuid
from datetime import datetime

from backend.models.security_event import SecurityEvent

SSH_PATTERN = re.compile(
    r"(?P<month>\w+)\s+(?P<day>\d+)\s+"
    r"(?P<time>\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+sshd.*?:\s+"
    r"(?P<status>Failed|Accepted)\s+password\s+for\s+"
    r"(?P<user>\S+)\s+from\s+"
    r"(?P<ip>\d+\.\d+\.\d+\.\d+)"
)


def parse_linux_auth_line(line: str):

    match = SSH_PATTERN.search(line)

    if not match:
        return None

    year = datetime.now().year

    timestamp = datetime.strptime(
        f"{year} {match.group('month')} {match.group('day')} {match.group('time')}",
        "%Y %b %d %H:%M:%S"
    )

    status = match.group("status")

    return SecurityEvent(

        event_id=uuid.uuid4(),

        timestamp=timestamp,

        source="linux",

        host=match.group("host"),

        username=match.group("user"),

        source_ip=match.group("ip"),

        destination_ip="",

        event_type="failed_login" if status == "Failed" else "successful_login",

        severity="medium",

        mitre_tactic="Credential Access",

        mitre_technique="T1110",

        message=line.strip(),

        raw_log=line.strip()
    )