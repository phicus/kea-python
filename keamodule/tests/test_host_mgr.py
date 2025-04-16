import kea
import pytest


@pytest.fixture()
def host_mgr():
    """Fixture to create a single instance of HostMgr."""
    return kea.HostMgr.instance()


@pytest.mark.parametrize(("args", "kwargs"), [((42,), {}), ((), {"foo": 42})])
def test_host_mgr_no_arguments_allowed(args, kwargs):
    """Test to ensure that HostMgr raises TypeError with incorrect arguments."""
    with pytest.raises(TypeError, match=r"takes no arguments"):
        kea.HostMgr(*args, **kwargs)


def test_host_mgr_is_singleton():
    """Test to check if the kea.HostMgr.instance() is of type kea.HostMgr."""
    instance = kea.HostMgr()
    assert isinstance(instance, kea.HostMgr), "The instance is not of type kea.HostMgr"
    assert instance is kea.HostMgr(), "HostMgr is not a singleton"


def test_host_mgr_instance_issingleton():
    """Test to ensure that HostMgr follows singleton pattern."""
    instance = kea.HostMgr.instance()
    assert instance is kea.HostMgr.instance(), "HostMgr.instance() is not a singleton"


@pytest.mark.parametrize(
    ("method_name", "args", "kwargs", "error_message"),
    [
        ("add", (), {}, r"function takes at least 1 argument \(0 given\)"),
        ("add", (), {"foo": 1}, r"takes no keyword arguments"),
        ("add", ("foo",), {}, r"argument 1 must be kea.Host, not str"),
        ("get", (), {}, r"function takes at least 2 arguments \(0 given\)"),
        ("get", (), {"foo": 1}, r"takes no keyword arguments"),
        ("get", ("foo", "foo"), {}, r"argument 1 must be int, not str"),
        ("get", (42, 42), {}, r"argument 2 must be str, not int"),
        ("get4", (), {}, r"function takes at least 2 arguments \(0 given\)"),
        ("get4", (), {"foo": 1}, r"takes no keyword arguments"),
        ("get4", ("foo", "foo"), {}, r"argument 1 must be int, not str"),
        ("get4", (42, 42), {}, r"argument 2 must be str, not int"),
        ("get4Any", (), {}, r"function takes at least 3 arguments \(0 given\)"),
        ("get4Any", (), {"foo": 1}, r"takes no keyword arguments"),
        ("get4Any", ("foo", "foo", "foo"), {}, r"argument 1 must be int, not str"),
        ("get4Any", (42, 42, "foo"), {}, r"argument 2 must be str, not int"),
        ("get4Any", (42, "foo", 42), {}, r"argument 3 must be str, not int"),
        ("getAll4", (), {}, r"function takes at least 1 argument \(0 given\)"),
        ("getAll4", (), {"foo": 1}, r"takes no keyword arguments"),
        ("getAll4", ("foo",), {}, r"argument 1 must be int, not str"),
        ("getPage4", (), {}, r"function takes exactly 4 arguments \(0 given\)"),
        ("getPage4", (), {"foo": 1}, r"takes no keyword arguments"),
        ("getPage4", ("foo", 0, 0, 10), {}, r"argument 1 must be int, not str"),
        ("getPage4", (1, "foo", 0, 10), {}, r"argument 2 must be int, not str"),
        ("getPage4", (1, 0, "foo", 10), {}, r"argument 3 must be int, not str"),
        ("getPage4", (1, 0, 0, "foo"), {}, r"argument 4 must be int, not str"),
        ("del_", (), {}, r"function takes at least 2 arguments \(0 given\)"),
        ("del_", (), {"foo": 1}, r"takes no keyword arguments"),
        ("del_", ("foo", "foo"), {}, r"argument 1 must be int, not str"),
        ("del_", (1, 42), {}, r"argument 2 must be str, not int"),
        ("del4", (), {}, r"function takes at least 3 arguments \(0 given\)"),
        ("del4", (), {"foo": 1}, r"takes no keyword arguments"),
        ("del4", ("foo", "foo", "foo"), {}, r"argument 1 must be int, not str"),
        ("del4", (1, 42, "foo"), {}, r"argument 2 must be str, not int"),
        ("del4", (1, "foo", 42), {}, r"argument 3 must be str, not int"),
    ],
)
def test_host_mgr_method_invalid_args(host_mgr, method_name, args, kwargs, error_message):
    """Test to ensure methods raise TypeError with incorrect arguments."""
    method = getattr(host_mgr, method_name)
    with pytest.raises(TypeError, match=error_message):
        method(*args, **kwargs)


def test_host_mgr_add_get_del(host_mgr):
    """Test to ensure that add, get, and del methods work as expected."""
    subnet_id = 0
    target = kea.PRIMARY_SOURCE

    host = kea.Host("cafecafe42", "hw-address", subnet_id, "198.51.100.42")

    # Verify that the host list is initially empty
    assert not host_mgr.getAll4(subnet_id), "Hosts not empty"

    host_mgr.add(host, target)

    # Verify that the host has been added
    assert len(host_mgr.getAll4(subnet_id)) == 1, "Host not added"

    # Verify that the added host can be retrieved
    assert host_mgr.get(subnet_id, "198.51.100.42") is not None, "Host not found"
    assert host_mgr.get(subnet_id, "hw-address", "cafecafe42") is not None, "Host not found"
    assert host_mgr.get4(subnet_id, "198.51.100.42") is not None, "Host not found"
    assert host_mgr.get4Any(subnet_id, "hw-address", "cafecafe42") is not None, "Host not found"

    # Verify that fetching a non-existent host returns None
    assert host_mgr.get(subnet_id, "254.254.254.254") is None, "Host found when it shouldn't be"
    assert host_mgr.get(subnet_id, "hw-address", "deadbeef21") is None, "Host found when it shouldn't be"
    assert host_mgr.get4(subnet_id, "254.254.254.254") is None, "Host found when it shouldn't be"
    assert host_mgr.get4Any(subnet_id, "hw-address", "deadbeef21") is None, "Host found when it shouldn't be"

    assert host_mgr.del4(subnet_id, "hw-address", "cafecafe42", target), "Host not deleted"
    assert not host_mgr.del4(subnet_id, "hw-address", "deadbeef21", target), "Host deleted when it shouldn't be"

    # Verify that the host has been deleted
    assert host_mgr.get(subnet_id, "hw-address", "cafecafe42") is None, "Host not deleted"
    assert host_mgr.get(subnet_id, "198.51.100.42") is None, "Host not deleted"

    assert not host_mgr.getAll4(subnet_id), "Hosts not empty after deletion"
