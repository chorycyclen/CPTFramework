# CPT Framework Foundation
import unittest

import functools


def class_setup_logger(function):
    @functools.wraps(function)
    def make_log(*args, **kwargs):
        print('setUp Start')
        result = function(*args, **kwargs)
        print('setUp End')
        return result

    return make_log


def class_teardown_logger(function):
    @functools.wraps(function)
    def make_log(*args, **kwargs):
        print('tearDown Start')
        result = function(*args, **kwargs)
        print('tearDown End')
        return result

    return make_log


class CaseMeta(type):
    """Metaclass for TestCase"""

    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if key == 'setUp':
                attrs[key] = class_setup_logger(value)
            if key == 'tearDown':
                attrs[key] = class_teardown_logger(value)
        return type.__new__(cls, name, bases, attrs)


class TestCase(unittest.TestCase, metaclass=CaseMeta):
    """单元测试基类"""

    def default_tearDown(self):
        """
        如果没有定义 tearDown_[用例方法名]
        的方法时，默认执行的tearDown方法
        """

    def default_setUp(self):
        """
        如果没有定义 setUp_[用例方法名]
        的方法时，默认执行的tearDown方法
        """

    def setUp(self):
        setup = getattr(self, "setUp_{}".format(self._testMethodName), self.default_setUp)
        setup()

    def tearDown(self):
        tear_down = getattr(self, "tearDown_{}".format(self._testMethodName), self.default_tearDown)
        tear_down()
