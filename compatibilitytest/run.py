# CPT Framework Foundation
from compatibilitytest.conf import Settings
from compatibilitytest.utils.argparser import ArgParser


class CPTFramework:
    def __init__(self):
        self._ap = ArgParser()
        self.settings = Settings(self._ap.settings)


def run():
    task = CPTFramework()


if __name__ == '__main__':
    run()
