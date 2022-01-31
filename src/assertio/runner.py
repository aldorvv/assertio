class Runner:

    def start(self, *args):
        [getattr(self, func)(*args) for func in dir(self) if func.startswith("test")]
