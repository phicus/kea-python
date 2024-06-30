import kea
import pytest
import utils


class TestLeaseMgr_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_no_arguments(kea.LeaseMgr)

    def test_ok(self):
        with pytest.raises(TypeError) as cm:
            kea.LeaseMgr()
        assert cm.value.args == ("no current lease manager is available",)
