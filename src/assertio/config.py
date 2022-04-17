"""Config functions."""
import os
import json

from dataclasses import dataclass, field
from inspect import getmembers, isroutine
from pathlib import Path

import yaml


def _stat(filename: str) -> Path:
    """Return a file if it exists."""
    file = Path.cwd().joinpath(filename)
    if file.exists():
        return file

@dataclass
class Config:
    """Configuration namespace."""

    base_url: str = field(default=os.getenv("ASSERTIO_BASE_URL", ""))
    logfile: str = field(default=os.getenv("ASSERTIO_LOGFILE", "assertio.log"))
    payloads_dir: str = field(
        default=os.getenv("ASSERTIO_PAYLOADS_DIR", "features/payloads")
    )

    def is_any_field_missing(self) -> bool:
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
