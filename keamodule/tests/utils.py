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
        with pytest.raises(RuntimeError) as cm:
            cls()
        assert cm.value.args == ("cannot directly construct",)

    def assert_constructor_no_arguments(self, cls):
        with pytest.raises(TypeError) as cm:
            cls(1)
        assert cm.value.args == ("function takes exactly 0 arguments (1 given)",)
        with pytest.raises(TypeError) as cm:
            cls(x=1)
        assert cm.value.args == ("keyword arguments are not supported",)

    def assert_constructor_one_arg_no_keywords(self, cls):
        with pytest.raises(TypeError) as cm:
            cls()
        assert cm.value.args == ("function takes exactly 1 argument (0 given)",)
        with pytest.raises(TypeError) as cm:
            cls(1, 2)
        assert cm.value.args == ("function takes exactly 1 argument (2 given)",)
        with pytest.raises(TypeError) as cm:
            cls(x=1)
        assert cm.value.args == ("keyword arguments are not supported",)

    def assert_constructor_two_args_no_keywords(self, cls):
        with pytest.raises(TypeError) as cm:
            cls()
        assert cm.value.args == ("function takes exactly 2 arguments (0 given)",)
        with pytest.raises(TypeError) as cm:
            cls(1)
        assert cm.value.args == ("function takes exactly 2 arguments (1 given)",)
        with pytest.raises(TypeError) as cm:
            cls(1, 2, 3)
        assert cm.value.args == ("function takes exactly 2 arguments (3 given)",)
        with pytest.raises(TypeError) as cm:
            cls(x=1)
        assert cm.value.args == ("keyword arguments are not supported",)

    def assert_method_no_arguments(self, method):
        with pytest.raises(TypeError, match=r"takes no arguments \(1 given\)"):
            method(1)
        with pytest.raises(TypeError, match="takes no keyword arguments"):
            method(x=1)

    def assert_method_one_arg_no_keywords(self, method):
        with pytest.raises(TypeError) as cm:
            method()
        assert cm.value.args == ("function takes exactly 1 argument (0 given)",)
        with pytest.raises(TypeError) as cm:
            method(1, 2)
        assert cm.value.args == ("function takes exactly 1 argument (2 given)",)
        with pytest.raises(TypeError) as cm:
            method(x=1)
        msg = "%s() takes no keyword arguments" % method.__name__
        assert (msg,) == cm.value.args

    def assert_method_two_args_no_keywords(self, method):
        with pytest.raises(TypeError) as cm:
            method()
        assert cm.value.args == ("function takes exactly 2 arguments (0 given)",)
        with pytest.raises(TypeError) as cm:
            method(1)
        assert cm.value.args == ("function takes exactly 2 arguments (1 given)",)
        with pytest.raises(TypeError) as cm:
            method(1, 2, 3)
        assert cm.value.args == ("function takes exactly 2 arguments (3 given)",)
        with pytest.raises(TypeError) as cm:
            method(x=1)
        msg = "%s() takes no keyword arguments" % method.__name__
        assert (msg,) == cm.value.args
