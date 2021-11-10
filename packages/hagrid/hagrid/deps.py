"""The purpose of these functions is to check the local dependencies of the person running the CLI
tool and ensure that things are properly configured for the cli's full use (depending on the user's
operating system.) When dependencies are missing the CLI tool should offer helpful hints about what
course of action to take to install missing dependencies, even offering to run appropriate
installation commands where applicable."""

# stdlib
import platform
import shutil
from typing import Any
from typing import Dict
from typing import Optional


class MissingDependency(Exception):
    pass


allowed_hosts = ["docker", "vm", "azure", "aws", "gcp"]
commands = ["docker", "git", "vagrant", "virtualbox", "ansible-playbook"]


def check_deps() -> Dict[str, Optional[str]]:
    paths = {}
    for dep in commands:
        paths[dep] = shutil.which(dep)
    return paths


def get_environment() -> Dict[str, Any]:
    return {
        "uname": platform.uname(),
        "platform": platform.system().lower(),
        "os_version": platform.release(),
        "python_version": platform.python_version(),
    }


DEPENDENCIES = check_deps()

ENVIRONMENT = get_environment()


def is_windows() -> bool:
    if "platform" in ENVIRONMENT and ENVIRONMENT["platform"] == "windows":
        return True
    return False
