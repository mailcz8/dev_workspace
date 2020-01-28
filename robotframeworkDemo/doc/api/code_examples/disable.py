"""Pre-run modifiers for disabling suite and test setups and teardowns."""

from robot.api import SuiteVisitor


class SuiteSetup(SuiteVisitor):

    def start_suite(self, suite):
        suite.keywords.setup = None


class SuiteTeardown(SuiteVisitor):

    def start_suite(self, suite):
        suite.keywords.teardown = None


class TestSetup(SuiteVisitor):

    def start_test(self, test):
        test.keywords.setup = None


class TestTeardown(SuiteVisitor):

    def start_test(self, test):
        test.keywords.teardown = None
