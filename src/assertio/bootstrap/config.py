"""Config functions."""
import os
import json

from dataclasses import dataclass, field
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

    def from_json(self, config_file: str = "assertio.json"):
        """Create config object from a json file."""
        file = _stat(config_file)
        if file is not None:
            config_json = json.load(open(file))
            for key, value in config_json.items():
                setattr(self, key, value)

    def from_yaml(self, config_file: str = "assertio.yaml"):
        """Create config object from a yaml file."""
        file = _stat(config_file)
        if file is not None:
            config_yaml = yaml.safe_load(open(file))
            for key, value in config_yaml.items():
                setattr(self, key, value)
