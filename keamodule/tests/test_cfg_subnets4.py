import kea
import pytest
import utils


class TestCfgSubnets4_new(utils.BaseTestCase):
    def test_cannot_construct(self):
        self.assert_cannot_construct(kea.CfgSubnets4)


class TestCfgSubnets4_getAll(utils.BaseTestCase):
    def test_badarg_count(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        self.assert_method_no_arguments(n.getAll)

    def test_ok(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        assert [] == n.getAll()
        assert n.use_count == 2
        o = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        assert o.use_count == 3
        o = None
        assert n.use_count == 2


class TestCfgSubnets4_getSubnet(utils.BaseTestCase):
    def test_badarg_count(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        self.assert_method_one_arg_no_keywords(n.getSubnet)

    def test_badarg_type(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        with pytest.raises(TypeError) as cm:
            n.getSubnet("foo")
        assert cm.value.args == ("argument 1 must be int, not str",)

    def test_ok(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        assert n.getSubnet(1) is None


class TestCfgSubnets4_selectSubnet(utils.BaseTestCase):
    def test_badarg_count(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        self.assert_method_one_arg_no_keywords(n.selectSubnet)

    def test_badarg_type(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        with pytest.raises(TypeError) as cm:
            n.selectSubnet(1)
        assert cm.value.args == ("argument 1 must be str, not int",)

    # def test_ok(self):
    #     n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
    #     self.assertIsNone(n.selectSubnet('192.168.0.1'))


class TestCfgSubnets4_toElement(utils.BaseTestCase):
    def test_badarg_type(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        self.assert_method_no_arguments(n.toElement)

    def test_ok(self):
        n = kea.CfgMgr().getCurrentCfg().getCfgSubnets4()
        assert [] == n.toElement()
