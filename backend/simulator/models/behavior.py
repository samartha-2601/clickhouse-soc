from dataclasses import dataclass
from enum import Enum


class BehaviorType(str, Enum):
    LOGIN = "login"
    LOGOUT = "logout"
    SSH = "ssh"
    SUDO = "sudo"
    GIT_PULL = "git_pull"
    DOCKER_BUILD = "docker_build"
    SYSTEM_UPDATE = "system_update"
    FAILED_LOGIN = "failed_login"
    PORT_SCAN = "port_scan"
    REVERSE_SHELL = "reverse_shell"


@dataclass(frozen=True)
class Behavior:
    behavior_type: BehaviorType
    probability: float