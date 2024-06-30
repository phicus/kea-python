import kea
import pytest
import utils


class TestHostMgr_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_cannot_construct(kea.HostMgr)


class TestHostMgr_instance(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_method_no_arguments(kea.HostMgr.instance)

    def test_ok(self):
        m = kea.HostMgr.instance()
        assert isinstance(m, kea.HostMgr)


class TestHostMgr_add(utils.BaseTestCase):
    def test_badarg_count(self):
        m = kea.HostMgr.instance()
        with pytest.raises(TypeError):
            m.add(1)
        with pytest.raises(TypeError):
            m.add(1, 2)

    def test_badarg_type(self):
        m = kea.HostMgr.instance()
        with pytest.raises(TypeError) as cm:
            m.add("foo")
        assert cm.value.args == ("argument 1 must be kea.Host, not str",)
