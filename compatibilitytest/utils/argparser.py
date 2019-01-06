# CPT Framework Foundation
import argparse


class ArgParser:
    """commandline hander class"""

    def __init__(self, args=None, namespace=None):
        self._wrapped = self.parse_cli_args(args, namespace)

    @staticmethod
    def parse_cli_args(args=None, namespace=None):
        """
        parse and save commandline arguments
        """
        parser = argparse.ArgumentParser(
            prog='Cross Platform Testing', description='Cross Platform Testing Framework')
        from compatibilitytest import VERSION
        parser.add_argument('--version', '-v', action='version',
                            version='%(prog)s version "{}"'.format(VERSION))
        parser.add_argument('--settings', required=True, help='设置模块路径')
        parser.add_argument('--include', '-i', nargs='*', help='匹配的用例标签')
        parser.add_argument('--suites', '-s', nargs='+', help='测试套件目录')
        return parser.parse_args(args, namespace)

    def __getattr__(self, name):
        """Return the value of a setting."""
        val = getattr(self._wrapped, name)
        return val
