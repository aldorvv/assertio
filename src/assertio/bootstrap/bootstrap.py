from argparse import ArgumentParser
from pathlib import Path
from pydoc import importfile


JSON_NAME = "assertio.json"
YAML_NAME = "assertio.yaml"

def _stat(filename: str) -> Path:
    """Return a file if it exists."""
    file = Path.cwd().joinpath(filename)
    if file.exists():
        return file


class _CLI:
    def __init__(self):
        _ = ArgumentParser()
        _.add_argument(
            "--run",
            default="all",
        )
        _.add_argument(
            "--settings",
            "-s",
            default=None
        )
        self._args = _.parse_args()

    def load_modules(self):
        modules = []
        for p in Path.cwd().joinpath("features/runners").glob("**/*.py"):
            modules.append(importfile(str(p)))
        return modules
    
    def get_runners_for(self, module):
        return [
            getattr(module, name) 
            for name in dir(module) 
            if name.endswith("Runner") and name != "Runner"
        ]

    def run_all(self):
        for module in self.load_modules():
            for runner in self.get_runners_for(module):
                runner().start()
    
    def run_one(self):
        for module in self.load_modules():
            for runner in self.get_runners_for(module):
                if self._args.run == runner.__name__:
                    runner().start()

    def bootstrap(self):
        if self._args.run == "all":
            self.run_all()
        else:
            self.run_one()

_CLI().bootstrap()