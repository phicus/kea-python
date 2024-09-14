import kea
import utils


class TestCalloutManager_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_no_arguments(kea.CalloutManager)

    def test_ok(self):
        m = kea.CalloutManager()
        assert m.use_count == 1
