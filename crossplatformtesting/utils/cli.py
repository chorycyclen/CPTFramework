import argparse
from crossplatformtesting import VERSION


class CLIHandler:
    def __init__(self, args=None, namespace=None):
        self._wrapped = self.parse_cli_args(args, namespace)

    @staticmethod
    def parse_cli_args(args=None, namespace=None):
        parser = argparse.ArgumentParser(prog='Cross Platform Testing', description='Cross Platform Testing Framework')
        parser.add_argument('--version', '-v', action='version', version='%(prog)s version "{}"'.format(VERSION))
        parser.add_argument('--settings', nargs='?', help='设置模块')
        parser.add_argument('--include', '-i', nargs='*', help='匹配的用例标签')
        parser.add_argument('--suites', '-s', nargs='+', help='测试套件目录')
        return parser.parse_args(args, namespace)


if __name__ == '__main__':
    handler = CLIHandler(['-h'])
    print(handler._wrapped.include)
