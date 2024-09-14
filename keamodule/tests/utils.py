from __future__ import annotations

import operator
import re
import sys
import unittest
from typing import Optional

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


def check_kea_version(operator_and_version: str) -> Optional[bool]:
    """
    Compare the current KEA version with the target version using the specified comparison operator.

    Args:
        operator_and_version (Optional[str]): The comparison operator and target version in
        the format "<operator><version>". If the operator is omitted, "==" is assumed.
        Valid operators are "==", "!=", "<", "<=", ">", ">=", "^", and "~". If None,
        no comparison is performed.

    Returns:
        Optional[bool]: True if the comparison is satisfied, False if not
    """

    pattern = re.compile(r"^(==|!=|<=|>=|<|>|~|\^)?(.+)$")
    match = pattern.match(operator_and_version)

    if not match:
        raise ValueError("Input must be in the format '<operator><version>'")

    comparison_operator, target_version = match.groups()

    comparison_operators = {
        "=": operator.eq,
        "==": operator.eq,
        "!": operator.ne,
        "<": operator.lt,
        "<=": operator.le,
        ">": operator.gt,
        ">=": operator.ge,
        "^": lambda a, b: a.major == b.major and a.minor == b.minor,  # Same major and minor version
        "~": lambda a, b: a.major == b.major,  # Same major version
    }

    comparison_operator = operator.eq if not comparison_operator else comparison_operators[comparison_operator]

    from packaging.version import Version

    current_version = Version(kea.KEA_VERSION)
    target_version_obj = Version(target_version)
    return comparison_operator(current_version, target_version_obj)
