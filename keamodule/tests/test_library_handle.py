import kea
import pytest
import utils


class TestLibraryHandle_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_one_arg_no_keywords(kea.LibraryHandle)

    def test_ok(self):
        m = kea.CalloutManager()
        h = kea.LibraryHandle(m)
        # LibraryHandle has pointer to CalloutManager, not shared_ptr
        assert m.use_count == 1
        assert isinstance(h, kea.LibraryHandle)


class TestLibraryHandle_registerCommandCallout(utils.BaseTestCase):
    def test_badarg_count(self):
        h = kea.LibraryHandle(kea.CalloutManager())
        self.assert_method_two_args_no_keywords(h.registerCommandCallout)

    def test_nadarg_type(self):
        h = kea.LibraryHandle(kea.CalloutManager())
        with pytest.raises(TypeError) as cm:
            h.registerCommandCallout(1, 42)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            h.registerCommandCallout("foo", 42)
        assert cm.value.args == ("callout must be callable",)

    def test_ok(self):
        def foo():
            pass

        h = kea.LibraryHandle(kea.CalloutManager())
        with pytest.raises(RuntimeError) as cm:
            h.registerCommandCallout("foo", foo)
        assert cm.value.args == ("only supported in embedded mode",)
