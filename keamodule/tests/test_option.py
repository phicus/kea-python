import codecs

import kea
import pytest
import utils


class TestOption_new(utils.BaseTestCase):
    def test_badarg_count(self):
        self.assert_constructor_one_arg_no_keywords(kea.Option)

    def test_badarg_type(self):
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            kea.Option("foo")
        # self.assertEqual(("an integer is required (got type str)",), cm.value.args)

    def test_ok(self):
        o = kea.Option(42)
        assert o.use_count == 1


class TestOption_getType(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getType)

    def test_ok(self):
        o = kea.Option(42)
        assert o.getType() == 42


class TestOption_getBytes(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getBytes)

    def test_ok(self):
        o = kea.Option(42)
        o.setBytes(b"123")
        assert o.getBytes() == b"123"


class TestOption_setBytes(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.setBytes)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError) as cm:
            o.setBytes("foo")
        assert cm.value.args == ("argument 1 must be bytes, not str",)

    def test_ok(self):
        o = kea.Option(42)
        assert o is o.setBytes(b"123")


class TestOption_getString(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getString)

    def test_ok(self):
        o = kea.Option(42)
        o.setString("Pokémon")
        assert o.getString() == "Pokémon"


class TestOption_setString(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.setString)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError) as cm:
            o.setString(1)
        assert cm.value.args == ("a bytes-like object is required, not 'int'",)

    def test_ok(self):
        o = kea.Option(42)
        assert o is o.setString("Pokémon")


class TestOption_getUint8(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getUint8)

    def test_ok(self):
        o = kea.Option(42)
        o.setUint8(0xFE)
        assert o.getUint8() == 254
        assert o.getBytes() == b"\xfe"


class TestOption_setUint8(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.setUint8)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            o.setUint8("foo")

    def test_ok(self):
        o = kea.Option(42)
        assert o is o.setUint8(254)


class TestOption_getUint16(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getUint16)

    def test_ok(self):
        o = kea.Option(42)
        o.setUint16(0xFEED)
        assert o.getUint16() == 65261
        assert o.getBytes() == b"\xfe\xed"


class TestOption_setUint16(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.setUint16)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            o.setUint16("foo")
        # self.assertEqual(("an integer is required (got type str)",), cm.value.args)

    def test_ok(self):
        o = kea.Option(42)
        assert o is o.setUint16(65261)


class TestOption_getUint32(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.getUint32)

    def test_ok(self):
        o = kea.Option(42)
        o.setUint32(0x01020304)
        assert o.getUint32() == 16909060
        assert o.getBytes() == b"\x01\x02\x03\x04"


class TestOption_setUint32(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.setUint32)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError) as cm:
            o.setUint32("foo")
        assert cm.value.args == ("argument 1 must be int, not str",)

    def test_ok(self):
        o = kea.Option(42)
        assert o is o.setUint32(16909060)


class TestOption_addOption(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.addOption)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError, match="argument 1 must be kea.Option"):
            o.addOption("foo")

    def test_ok(self):
        o = kea.Option(42)
        p = kea.Option(2).setUint8(0xEF)
        assert o is o.addOption(p)


class TestOption_getOption(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_one_arg_no_keywords(o.getOption)

    def test_badarg_type(self):
        o = kea.Option(42)
        with pytest.raises(TypeError, match="an integer is required|object cannot be interpreted as an integer"):
            o.getOption("foo")

    def test_ok(self):
        o = kea.Option(42).addOption(kea.Option(2).setUint8(0xEF))
        p = o.getOption(2)
        assert isinstance(p, kea.Option)
        assert p.getType() == 2
        assert p.getUint8() == 239


class TestOption_pack(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.pack)

    def test_ok(self):
        o = kea.Option(42).addOption(kea.Option(2).setUint8(0xEF))
        wire = o.pack()
        assert isinstance(wire, bytes)
        assert codecs.encode(wire, "hex") == b"2a030201ef"


class TestOption_toText(utils.BaseTestCase):
    def test_badarg_count(self):
        o = kea.Option(42)
        self.assert_method_no_arguments(o.toText)

    def test_empty(self):
        o = kea.Option(42)
        assert o.toText() == "type=042, len=000: "

    def test_uint8(self):
        o = kea.Option(42).setUint8(5)
        assert o.toText() == "type=042, len=001: 05"

    def test_nested(self):
        o = kea.Option(42).addOption(kea.Option(4).setUint16(5)).addOption(kea.Option(6).setString("hello"))
        assert (
            o.toText() == "type=042, len=011: ,\noptions:\n  type=004, len=002:"
            " 00:05\n  type=006, len=005: 68:65:6c:6c:6f"
        )
