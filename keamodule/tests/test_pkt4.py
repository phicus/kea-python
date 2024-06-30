from ipaddress import IPv4Network

import kea
import pytest
import utils


# https://fossies.org/dox/kea-1.7.4/classisc_1_1dhcp_1_1Pkt4.html
class TestPkt4_new(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        # 1 or 2 args
        with pytest.raises(TypeError) as cm:
            kea.Pkt4()
        assert cm.value.args == ("function takes exactly 2 arguments (0 given)",)
        with pytest.raises(TypeError) as cm:
            kea.Pkt4(1, 2, 3)
        assert cm.value.args == ("function takes exactly 2 arguments (3 given)",)
        with pytest.raises(TypeError) as cm:
            kea.Pkt4(x=1)
        assert cm.value.args == ("keyword arguments are not supported",)

    def test_badarg_type(self):
        # 1 arg - bytes
        with pytest.raises(TypeError) as cm:
            kea.Pkt4(42)
        assert cm.value.args == ("argument 1 must be bytes, not int",)
        # 2 args - type, trans_id
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            kea.Pkt4("1", 42)
        with pytest.raises(TypeError) as cm:
            kea.Pkt4(1, "42")
        assert cm.value.args == ("argument 2 must be int, not str",)

    def test_ok(self):
        assert self.packet4.use_count == 1


class TestPkt4_getType(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getType)

    def test_ok(self):
        assert self.packet4.getType() == kea.DHCPREQUEST


class TestPkt4_setType(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setType)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            self.packet4.setType("foo")

    def test_ok(self):
        self.packet4.setType(kea.DHCPNAK)
        assert self.packet4.getType() == kea.DHCPNAK


class TestPkt4_getFlags(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getFlags)

    def test_ok(self):
        assert self.packet4.getFlags() == 0


class TestPkt4_setFlags(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setFlags)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            self.packet4.setFlags("foo")

    def test_ok(self):
        self.packet4.setFlags(0xBEEF)
        assert self.packet4.getFlags() == 48879


class TestPkt4_getLocalAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getLocalAddr)

    def test_ok(self):
        assert self.packet4.getLocalAddr() == "0.0.0.0"


class TestPkt4_setLocalAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setLocalAddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setLocalAddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setLocalAddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setLocalAddr("1.2.3.4")
        assert self.packet4.getLocalAddr() == "1.2.3.4"


class TestPkt4_getRemoteAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getRemoteAddr)

    def test_ok(self):
        assert self.packet4.getRemoteAddr() == "0.0.0.0"


class TestPkt4_setRemoteAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setRemoteAddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setRemoteAddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setRemoteAddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setRemoteAddr("1.2.3.4")
        assert self.packet4.getRemoteAddr() == "1.2.3.4"


class TestPkt4_getCiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getCiaddr)

    def test_ok(self):
        assert self.packet4.getCiaddr() == "0.0.0.0"


class TestPkt4_setCiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setCiaddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setCiaddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setCiaddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setCiaddr("1.2.3.4")
        assert self.packet4.getCiaddr() == "1.2.3.4"


class TestPkt4_getGiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getGiaddr)

    def test_ok(self):
        assert self.packet4.getGiaddr() == "0.0.0.0"


class TestPkt4_setGiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setGiaddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setGiaddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setGiaddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setGiaddr("1.2.3.4")
        assert self.packet4.getGiaddr() == "1.2.3.4"


class TestPkt4_getSiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getSiaddr)

    def test_ok(self):
        assert self.packet4.getSiaddr() == "0.0.0.0"


class TestPkt4_setSiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setSiaddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setSiaddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setSiaddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setSiaddr("1.2.3.4")
        assert self.packet4.getSiaddr() == "1.2.3.4"


class TestPkt4_getYiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getYiaddr)

    def test_ok(self):
        assert self.packet4.getYiaddr() == "0.0.0.0"


class TestPkt4_setYiaddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setYiaddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setYiaddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setYiaddr("foo")
        assert cm.value.args == ("Failed to convert string to address 'foo': Invalid argument",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setYiaddr("1.2.3.4")
        assert self.packet4.getYiaddr() == "1.2.3.4"


class TestPkt4_getHWAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.getHWAddr)

    def test_ok(self):
        assert self.packet4.getHWAddr() == ""


class TestPkt4_setHWAddr(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.setHWAddr)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.setHWAddr(1)
        assert cm.value.args == ("argument 1 must be str, not int",)
        with pytest.raises(TypeError) as cm:
            self.packet4.setHWAddr("foo")
        assert cm.value.args == ("invalid format of the decoded string 'foo'",)

    def test_ok(self):
        assert self.packet4 is self.packet4.setHWAddr("01:02:03:04:05:06")
        assert self.packet4.getHWAddr() == "01:02:03:04:05:06"


class TestPkt4_delOption(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.delOption)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            self.packet4.delOption("foo")

    def test_ok(self):
        assert not self.packet4.delOption(42)


class TestPkt4_addOption(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.addOption)

    def test_badarg_type(self):
        with pytest.raises(TypeError) as cm:
            self.packet4.addOption("foo")
        assert cm.value.args == ("argument 1 must be kea.Option, not str",)

    def test_empty_option_ok(self):
        option = kea.Option(25)
        assert self.packet4 is self.packet4.addOption(option)
        assert option.use_count == 2

    def test_bytes_option_ok(self):
        option = kea.Option(25)
        assert self.packet4 is self.packet4.addOption(option)
        assert option.use_count == 2

    def test_ok(self):
        option = kea.Option(kea.DHO_DHCP_AGENT_OPTIONS)
        assert option.use_count == 1
        assert self.packet4 is self.packet4.addOption(option)
        assert option.use_count == 2
        n = self.packet4.getOption(kea.DHO_DHCP_AGENT_OPTIONS)
        assert n.getType() == kea.DHO_DHCP_AGENT_OPTIONS


class TestPkt4_getOption(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_one_arg_no_keywords(self.packet4.getOption)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            self.packet4.getOption("foo")

    def test_ok(self):
        option = self.packet4.getOption(kea.DHO_DHCP_MESSAGE_TYPE)
        assert isinstance(option, kea.Option)
        assert bytes([kea.DHCPREQUEST]) == option.getBytes()


class TestPkt4_pack(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.pack)

    def test_ok(self):
        wire = self.packet4.pack()
        assert isinstance(wire, bytes)


class TestPkt4_unpack(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.unpack)

    def test_ok(self):
        wire = self.packet4.pack()
        self.packet4 = kea.Pkt4(wire)
        assert self.packet4.unpack() is None


class TestPkt4_toText(utils.BaseTestCase):
    def setUp(self):
        self.packet4 = kea.Pkt4(kea.DHCPREQUEST, 42)

    def test_badarg_count(self):
        self.assert_method_no_arguments(self.packet4.toText)

    def test_empty(self):
        assert (
            self.packet4.toText() == "local_address=0.0.0.0:67, remote_address=0.0.0.0:68,\n"
            "msg_type=DHCPREQUEST (3), trans_id=0x2a,\n"
            "options:\n"
            "  type=053, len=001: 3 (uint8)"
        )  # noqa: E501

    def test_filled(self):
        # 53
        self.packet4.setLocalAddr("1.2.3.4")
        self.packet4.setRemoteAddr("2.3.4.5")
        subnet = IPv4Network("10.0.0.0/20")
        self.packet4.addOption(kea.Option(kea.DHO_SUBNET_MASK).setBytes(subnet.netmask.packed))  # 1
        self.packet4.addOption(kea.Option(kea.DHO_ROUTERS).setBytes(subnet[1].packed))  # 3
        self.packet4.addOption(kea.Option(kea.DHO_DOMAIN_NAME).setString("test.org"))  # 15
        self.packet4.addOption(kea.Option(kea.DHO_DHCP_LEASE_TIME).setUint32(7200))  # 51
        self.packet4.addOption(kea.Option(kea.DHO_DHCP_RENEWAL_TIME).setUint32(1800))  # 58
        self.packet4.addOption(kea.Option(kea.DHO_DHCP_REBINDING_TIME).setUint32(3600))  # 59
        assert (
            self.packet4.toText() == "local_address=1.2.3.4:67, remote_address=2.3.4.5:68,\n"
            "msg_type=DHCPREQUEST (3), trans_id=0x2a,\n"
            "options:\n"
            "  type=001, len=004: ff:ff:f0:00\n"
            "  type=003, len=004: 0a:00:00:01\n"
            "  type=015, len=008: 74:65:73:74:2e:6f:72:67\n"
            "  type=051, len=004: 00:00:1c:20\n"
            "  type=053, len=001: 3 (uint8)\n"
            "  type=058, len=004: 00:00:07:08\n"
            "  type=059, len=004: 00:00:0e:10"
        )  # noqa: E501
