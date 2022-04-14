"""Config functions."""
import os
from inspect import getmembers, isroutine
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

import json
import yaml


def _stat(filename: str) -> Union[Path, None]:
    """Return a file if it exists."""
    file = Path.cwd().joinpath(filename)
    if file.exists():
        return file
    return None

@dataclass
class Config:
    """Configuration namespace."""

    base_url: str = field(default=os.getenv("ASSERTIO_BASE_URL", ""))
    logfile: str = field(default=os.getenv("ASSERTIO_LOGFILE", ""))

    def is_any_field_missing(self):
        """Return if any field is missing."""
        members = getmembers(self, lambda attr: not isroutine(attr))
        attrs = [attr[0] for attr in members if "_" not in attr[0]]
        return not all(
            hasattr(self, attr) and getattr(self, attr) for attr in attrs
        )

    def from_json(self, config_file: str = "assertio.json"):
        """Create config object from a json file."""
        file = _stat(config_file)
        config_json = json.load(open(file))
        for key, value in config_json.items():
            setattr(self, key, value)

    def from_yaml(self, config_file: str = "assertio.yaml"):
        """Create config object from a yaml file."""
        file = _stat(config_file)
        config_yaml = yaml.safe_load(open(file))
        for key, value in config_yaml.items():
            setattr(self, key, value)


DEFAULTS = Config()

try:
    if DEFAULTS.is_any_field_missing() and _stat("assertio.json"):
        DEFAULTS.from_json()
    if DEFAULTS.is_any_field_missing() and (
        _stat("assertio.yaml") or _stat("assertio.yml")
    ):
        DEFAULTS.from_yaml()
except FileNotFoundError as ConfigError:
    raise EnvironmentError from ConfigError
