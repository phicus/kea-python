import sys

import kea
import pytest
import utils


class TestCalloutHandle_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_one_arg_no_keywords(kea.CalloutHandle)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            kea.CalloutHandle(1)
        assert cm.value.args == ("argument 1 must be kea.CalloutManager, not int",)

    def test_ok(self):
        m = kea.CalloutManager()
        h = kea.CalloutHandle(m)
        assert m.use_count == 2
        del h
        assert m.use_count == 1


class TestCalloutHandle_getArgument(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_one_arg_no_keywords(h.getArgument)

    def test_badarg_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError, match="argument 1 must be str, not int"):
            h.getArgument(3)

    def test_badarg_value(self):
        handle = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(ValueError, match="unknown argument"):
            handle.getArgument("foo")

    def test_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.getArgument("query4")
        assert cm.value.args == ("unable to find argument with name query4",)


class TestCalloutHandle_setArgument(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_two_args_no_keywords(h.setArgument)

    def test_badarg_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument(3, 4)
        assert cm.value.args == ("argument 1 must be str, not int",)

    def test_badarg_value(self):
        handle = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(ValueError, match="unknown argument"):
            handle.setArgument("foo", 3)

    def test_lease4_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        x = kea.Lease4()
        x.addr = "1.2.3.4"
        assert x.use_count == 1
        assert h.setArgument("lease4", x) is None
        assert x.use_count == 2
        assert h.getArgument("lease4").addr == "1.2.3.4"

    def test_lease4_bad_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument("lease4", 3)
        assert cm.value.args == ("expected Lease4 object",)

    def test_query4_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        x = kea.Pkt4(kea.DHCPACK, 42)
        assert x.use_count == 1
        assert h.setArgument("query4", x) is None
        assert x.use_count == 2
        assert h.getArgument("query4").getType() == kea.DHCPACK

    def test_query4_bad_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument("query4", 3)
        assert cm.value.args == ("expected Pkt4 object",)

    def test_response4_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        x = kea.Pkt4(kea.DHCPACK, 42)
        assert x.use_count == 1
        assert h.setArgument("response4", x) is None
        assert x.use_count == 2
        assert h.getArgument("response4").getType() == kea.DHCPACK

    def test_response4_bad_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument("response4", 3)
        assert cm.value.args == ("expected Pkt4 object",)

    def test_command_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        assert h.setArgument("command", {"foo": 42}) is None
        assert {"foo": 42} == h.getArgument("command")

    def test_command_bad_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument("command", self)
        assert cm.value.args == ("unhandled type TestCalloutHandle_setArgument",)

    def test_response_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        assert h.setArgument("response", [1, "two", None]) is None
        assert [1, "two", None] == h.getArgument("response")

    def test_response_bad_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setArgument("response", self)
        assert cm.value.args == ("unhandled type TestCalloutHandle_setArgument",)


class TestCalloutHandle_setContext(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_two_args_no_keywords(h.setContext)

    def test_badarg_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.setContext(1, 2)
        assert cm.value.args == ("argument 1 must be str, not int",)

    def test_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        foo = utils.Logger()
        assert h.setContext("foo", foo) is None
        assert sys.getrefcount(foo) == 3


class TestCalloutHandle_getContext(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_one_arg_no_keywords(h.getContext)

    def test_badarg_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.getContext(1)
        assert cm.value.args == ("argument 1 must be str, not int",)

    def test_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        foo = utils.Logger()
        h.setContext("foo", foo)
        bar = h.getContext("foo")
        assert foo is bar

    def test_notset(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.getContext("foo")
        assert cm.value.args == ("unable to find callout context associated with the current" " library index (-1)",)


class TestCalloutHandle_deleteContext(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_one_arg_no_keywords(h.deleteContext)

    def test_badarg_type(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.deleteContext(1)
        assert cm.value.args == ("argument 1 must be str, not int",)

    def test_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        foo = utils.Logger()
        h.setContext("foo", foo)
        assert sys.getrefcount(foo) == 3
        assert h.deleteContext("foo") is None
        assert sys.getrefcount(foo) == 2

    def test_notset(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        assert h.deleteContext("foo") is None


class TestCalloutHandle_getStatus(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        self.assert_method_no_arguments(h.getStatus)

    def test_ok(self):
        h = kea.CalloutHandle(kea.CalloutManager())
        assert h.getStatus() == kea.NEXT_STEP_CONTINUE


class TestCalloutHandle_setStatus(utils.BaseTestCase):
    def setUp(self):
        self.handle = kea.CalloutHandle(kea.CalloutManager())

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.handle.setStatus)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="object cannot be interpreted as an integer"):
            self.handle.setStatus("foo")

    def test_ok(self):
        assert self.handle.setStatus(kea.NEXT_STEP_SKIP) is None
        assert self.handle.getStatus() == kea.NEXT_STEP_SKIP
