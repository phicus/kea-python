import kea
import pytest
import utils


class TestSrvConfig_new(utils.BaseTestCase):
    def test_cannot_construct(self):
        with pytest.raises(RuntimeError) as cm:
            kea.SrvConfig()
        assert cm.value.args == ("cannot directly construct",)


class TestGetCurrentConfig(utils.BaseTestCase):
    def test_badarg_count(self):
        m = kea.CfgMgr()
        self.assert_method_no_arguments(m.getCurrentCfg)

    def test_ok(self):
        m = kea.CfgMgr()
        c = m.getCurrentCfg()
        assert c.use_count == 3
        d = m.getCurrentCfg()
        assert c.use_count == 4
        assert d.use_count == 4


class TestGetStagingConfig(utils.BaseTestCase):
    def test_badarg_count(self):
        m = kea.CfgMgr()
        self.assert_method_no_arguments(m.getStagingCfg)

    def test_ok(self):
        m = kea.CfgMgr()
        c = m.getStagingCfg()
        assert c.use_count == 2
        d = m.getStagingCfg()
        assert c.use_count == 3
        assert d.use_count == 3
        d = None
        assert c.use_count == 2


class TestSrvConfig_getCfgSubnets4(utils.BaseTestCase):
    def test_badarg_count(self):
        c = kea.CfgMgr().getStagingCfg()
        self.assert_method_no_arguments(c.getCfgSubnets4)

    def test_ok(self):
        c = kea.CfgMgr().getStagingCfg()
        n = c.getCfgSubnets4()
        assert n.use_count == 2


class TestSrvConfig_toElement(utils.BaseTestCase):
    def test_badarg_count(self):
        c = kea.CfgMgr().getStagingCfg()
        self.assert_method_no_arguments(c.toElement)

    def test_ok(self):
        c = kea.CfgMgr().getStagingCfg()
        e = c.toElement()
        assert isinstance(e, dict)
