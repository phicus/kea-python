import sys
import unittest

import kea
import pytest


class Logger:
    def error(self, msg):
        sys.stderr.write(msg + "\n")


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        kea.logger = Logger()

    def assert_cannot_construct(self, cls):
        with pytest.raises(RuntimeError, match=r"cannot directly construct"):
            cls()

    def assert_constructor_no_arguments(self, cls):
        with pytest.raises(TypeError, match=r"function takes exactly 0 arguments \(1 given\)"):
            cls(1)
        with pytest.raises(TypeError, match=r"keyword arguments are not supported"):
            cls(x=1)

    def assert_constructor_one_arg_no_keywords(self, cls):
        with pytest.raises(TypeError, match=r"function takes exactly 1 argument \(0 given\)"):
            cls()
        with pytest.raises(TypeError, match=r"function takes exactly 1 argument \(2 given\)"):
            cls(1, 2)
        with pytest.raises(TypeError, match=r"keyword arguments are not supported"):
            cls(x=1)

    def assert_constructor_two_args_no_keywords(self, cls):
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(0 given\)"):
            cls()
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(1 given\)"):
            cls(1)
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(3 given\)"):
            cls(1, 2, 3)
        with pytest.raises(TypeError, match=r"keyword arguments are not supported"):
            cls(x=1)

    def assert_method_no_arguments(self, method):
        with pytest.raises(TypeError, match=r"takes no arguments \(1 given\)"):
            method(1)
        with pytest.raises(TypeError, match=r"takes no keyword arguments"):
            method(x=1)

    def assert_method_one_arg_no_keywords(self, method):
        with pytest.raises(TypeError, match=r"function takes exactly 1 argument \(0 given\)"):
            method()
        with pytest.raises(TypeError, match=r"function takes exactly 1 argument \(2 given\)"):
            method(1, 2)
        with pytest.raises(TypeError, match=r"takes no keyword arguments"):
            method(x=1)

    def assert_method_two_args_no_keywords(self, method):
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(0 given\)"):
            method()
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(1 given\)"):
            method(1)
        with pytest.raises(TypeError, match=r"function takes exactly 2 arguments \(3 given\)"):
            method(1, 2, 3)
        with pytest.raises(TypeError, match=r"takes no keyword arguments"):
            method(x=1)
