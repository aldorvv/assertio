from sys import argv

from features.tests import INSTALLED_RUNNERS


if argv[1] == "all":
    for runner in INSTALLED_RUNNERS:
        runner().start()

else:
    for runner in INSTALLED_RUNNERS:
        if runner.__name__ == argv[1]:
            runner().start()
