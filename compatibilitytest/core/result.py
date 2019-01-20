# CPT Framework Foundation
import inspect
import re
import sys
from unittest import TestResult
from unittest import TextTestRunner

_real_stdout = sys.stdout
_real_stderr = sys.stderr
_ERROR_HOLDERS_FQN = ("unittest.suite._ErrorHolder", "unittest2.suite._ErrorHolder")


def get_class_fullname(something):
    if inspect.isclass(something):
        cls = something
    else:
        cls = something.__class__

    module = cls.__module__
    if module is None or module == str.__class__.__module__:
        return cls.__name__
    return module + '.' + cls.__name__


class CPTTestResult(TestResult):
    """测试结果类"""

    def __init__(self, stream=_real_stdout, descriptions=None, verbosity=None):
        super(CPTTestResult, self).__init__()
        #
        # # Some code may ask for self.failfast, see unittest2.case.TestCase.subTest
        # self.failfast = getattr(self, "failfast", False)
        #
        # self.test_started_datetime_map = {}
        # self.failed_tests = set()
        # self.subtest_failures = {}
        # # self.messages = TeamcityServiceMessages(_real_stdout)
        self.buffer = True
        self.current_test_id = None

    @staticmethod
    def get_test_id(test):
        if isinstance(test, str):
            return test

        test_class_fullname = get_class_fullname(test)
        test_id = test.id()

        if test_class_fullname in _ERROR_HOLDERS_FQN:
            # patch setUpModule (__main__) -> __main__.setUpModule
            return re.sub(r'^(.*) \((.*)\)$', r'\2.\1', test_id)

        # Force test_id for doctests
        if test_class_fullname != "doctest.DocTestCase":
            desc = test.shortDescription()
            test_method_name = getattr(test, "_testMethodName", "")
            if desc and desc != test_id and desc != test_method_name:
                return "%s (%s)" % (test_id, desc.replace('.', '_'))

        return test_id

    def _setupStdout(self):
        super(CPTTestResult, self)._setupStdout()
        # if getattr(self, 'buffer', None):
        print('\t\t_setupStdout')
        print('\t\t_previousTestClass: {}'.format(self._previousTestClass))
        print('\t\t_moduleSetUpFailed: {}'.format(self._moduleSetUpFailed))
        print('\t\tcurrent_test_id: {}'.format(self.current_test_id))
        # self._stderr_buffer = FlushingStringIO(self._dump_test_stderr)
        # self._stdout_buffer = FlushingStringIO(self._dump_test_stdout)
        # sys.stdout = self._stdout_buffer
        # sys.stderr = self._stderr_buffer

    def _restoreStdout(self):
        super(CPTTestResult, self)._restoreStdout()
        print('\t\t_previousTestClass: {}'.format(self._previousTestClass))
        print('\t\t_moduleSetUpFailed: {}'.format(self._moduleSetUpFailed))
        print('\t\tcurrent_test_id: {}'.format(self.current_test_id))
        print('\t\t_restoreStdout\n\n\n')

    def startTest(self, test):
        super(CPTTestResult, self).startTest(test)
        test_id = self.get_test_id(test)
        self.current_test_id = test_id

    def stopTest(self, test):
        super(CPTTestResult, self).stopTest(test)
        self.current_test_id = None


class CPTTestRunner(TextTestRunner):
    resultclass = CPTTestResult

    if sys.version_info < (2, 7):
        def _makeResult(self):
            result = CPTTestResult(self.stream, self.descriptions, self.verbosity)
            return result

    def run(self, test):
        # subtest_filter = None
        # if sys.version_info > (3, 3):  # No subtests in < 2.4
        #     def subtest_filter(current_test):
        #         return not getattr(current_test, "_subtest", None)
        # # noinspection PyBroadException
        # patch_unittest_diff(subtest_filter)
        # try:
        #     total_tests = test.countTestCases()
        #     TeamcityServiceMessages(_real_stdout).testCount(total_tests)
        # except Exception:
        #     pass

        return super(CPTTestRunner, self).run(test)
