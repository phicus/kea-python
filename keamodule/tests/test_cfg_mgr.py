import kea
import utils


class TestCfgMgr_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_no_arguments(kea.CfgMgr)

    def test_ok(self):
        m = kea.CfgMgr()
        assert isinstance(m, kea.CfgMgr)


class TestCfgMgr_getCurrentCfg(utils.BaseTestCase):
    def test_badarg_count(self):
        m = kea.CfgMgr()
        self.assert_method_no_arguments(m.getCurrentCfg)

    def test_ok(self):
        m = kea.CfgMgr()
        c = m.getCurrentCfg()
        assert isinstance(c, kea.SrvConfig)


class TestCfgMgr_getStagingCfg(utils.BaseTestCase):
    def test_badarg_count(self):
        m = kea.CfgMgr()
        self.assert_method_no_arguments(m.getStagingCfg)

    def test_ok(self):
        m = kea.CfgMgr()
        c = m.getStagingCfg()
        assert isinstance(c, kea.SrvConfig)
