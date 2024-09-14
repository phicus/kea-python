import kea
import pytest
import utils


class TestLease4_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_no_arguments(kea.Lease4)

    def test_ok(self):
        x = kea.Lease4()
        assert x.use_count == 1


class TestLease4_addr(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.addr == "0.0.0.0"
        x.addr = "192.168.0.1"
        assert x.addr == "192.168.0.1"

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.addr = "bogus"
        assert cm.value.args == ("Failed to convert string to address 'bogus': Invalid argument",)
        with pytest.raises(TypeError) as cm:
            x.addr = 0
        assert cm.value.args == ("The addr attribute value must be a str",)


class TestLease4_valid_lft(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.valid_lft == 0
        x.valid_lft = 3600
        assert x.valid_lft == 3600

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.valid_lft = "bogus"
        assert cm.value.args == ("The valid_lft attribute value must be an int",)


class TestLease4_cltt(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.cltt == 0
        x.cltt = 3600
        assert x.cltt == 3600

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.cltt = "bogus"
        assert cm.value.args == ("The cltt attribute value must be an int",)


class TestLease4_subnet_id(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.subnet_id == 0
        x.subnet_id = 5
        assert x.subnet_id == 5

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.subnet_id = "bogus"
        assert cm.value.args == ("The subnet_id attribute value must be an int",)


class TestLease4_hostname(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.hostname is None
        x.hostname = "example.org"
        assert x.hostname == "example.org"
        x.hostname = None
        assert x.hostname is None

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.hostname = 3
        assert cm.value.args == ("The hostname attribute value must be a str",)


class TestLease4_fqdn_fwd(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert False is x.fqdn_fwd
        x.fqdn_fwd = True
        assert True is x.fqdn_fwd
        x.fqdn_fwd = False
        assert False is x.fqdn_fwd

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.fqdn_fwd = "bogus"
        assert cm.value.args == ("The fqdn_fwd attribute value must be a bool",)


class TestLease4_fqdn_rev(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert False is x.fqdn_rev
        x.fqdn_rev = True
        assert True is x.fqdn_rev
        x.fqdn_rev = False
        assert False is x.fqdn_rev

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.fqdn_rev = "bogus"
        assert cm.value.args == ("The fqdn_rev attribute value must be a bool",)


class TestLease4_hwaddr(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.hwaddr is None
        x.hwaddr = "01:02:03:04:05:06"
        assert x.hwaddr == "01:02:03:04:05:06"

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.hwaddr = "bogus"
        assert cm.value.args == ("invalid format of the decoded string 'bogus'",)


class TestLease4_client_id(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.client_id is None
        x.client_id = "01:02:03:04:05:06"
        assert x.client_id == "01:02:03:04:05:06"

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.client_id = "bogus"
        assert cm.value.args == ("'bogus' is not a valid string of hexadecimal digits",)


class TestLease4_state(utils.BaseTestCase):
    def test_getset(self):
        x = kea.Lease4()
        assert x.state == 0
        x.state = 5
        assert x.state == 5

    def test_bad_type(self):
        x = kea.Lease4()
        with pytest.raises(TypeError) as cm:
            x.state = "bogus"
        assert cm.value.args == ("The state attribute value must be an int",)


class TestLease4_setContext(utils.BaseTestCase):
    def test_badarg_count(self):
        x = kea.Lease4()
        self.assert_method_one_arg_no_keywords(x.setContext)

    def test_ok(self):
        x = kea.Lease4()
        assert x is x.setContext("foo")
        assert x is x.setContext(2)
        assert x is x.setContext(True)
        assert x is x.setContext([1, "foo"])
        assert x is x.setContext({"foo": "bar"})
        assert x is x.setContext(None)


class TestLease4_getContext(utils.BaseTestCase):
    def test_badarg_count(self):
        x = kea.Lease4()
        self.assert_method_no_arguments(x.getContext)

    def test_ok(self):
        x = kea.Lease4()
        assert x.getContext() is None
        x.setContext(None)
        assert x.getContext() is None
        x.setContext("foo")
        assert x.getContext() == "foo"
        x.setContext(2)
        assert x.getContext() == 2
        x.setContext(True)
        assert True is x.getContext()
        x.setContext([1, "foo"])
        assert [1, "foo"] == x.getContext()
        x.setContext({"foo": "bar"})
        assert {"foo": "bar"} == x.getContext()


class TestLease4_toElement(utils.BaseTestCase):
    def test_badarg_count(self):
        x = kea.Lease4()
        self.assert_method_no_arguments(x.toElement)

    def test_empty(self):
        x = kea.Lease4()
        with pytest.raises(RuntimeError) as cm:
            assert {} == x.toElement()
        assert isinstance(cm.value, RuntimeError)
        assert cm.value.args == ("hwaddr must not be empty",)

    def test_ok(self):
        x = kea.Lease4()
        x.hwaddr = "01:02:03:04:05:06"
        assert {
            "cltt": 0,
            "fqdn-fwd": False,
            "fqdn-rev": False,
            "hostname": "",
            "hw-address": "01:02:03:04:05:06",
            "ip-address": "0.0.0.0",
            "state": 0,
            "subnet-id": 0,
            "valid-lft": 0,
        } == x.toElement()
        x.cltt = 3600
        x.fqdn_fwd = x.fqdn_rev = True
        x.hostname = "example.com"
        x.addr = "192.168.0.1"
        x.state = 3
        x.subnet_id = 4
        x.valid_lft = 1800
        x.client_id = "02:03:04:05:06:07"
        assert {
            "client-id": "02:03:04:05:06:07",
            "cltt": 3600,
            "fqdn-fwd": True,
            "fqdn-rev": True,
            "hostname": "example.com",
            "hw-address": "01:02:03:04:05:06",
            "ip-address": "192.168.0.1",
            "state": 3,
            "subnet-id": 4,
            "valid-lft": 1800,
        } == x.toElement()
