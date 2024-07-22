import kea
import pytest


@pytest.fixture()
def cfg_mgr():
    """Fixture to create a single instance of CfgMgr."""
    return kea.CfgMgr.instance()


def test_CfgMgr_singleton():
    """Test to ensure that CfgMgr follows singleton pattern."""
    instance = kea.CfgMgr.instance()
    assert isinstance(instance, kea.CfgMgr)


def test_CfgMgr_instance():
    """Test to ensure that instance method returns the same instance."""
    assert kea.CfgMgr.instance() is kea.CfgMgr.instance()


@pytest.mark.parametrize(
    ("method_name", "args", "kwargs", "error_message"),
    [
        ("instance", (1,), {}, r"takes no arguments"),
        ("instance", (), {"foo": 1}, r"takes no keyword arguments"),
        ("getDataDir", (1,), {}, r"takes no arguments"),
        ("getDataDir", (), {"foo": 1}, r"takes no keyword arguments"),
        ("setDataDir", (), {}, r"function takes at least 1 argument"),
        ("setDataDir", (1,), {}, r"argument 1 must be str, not int"),
        ("setDataDir", ("foo", "bar"), {}, r"an integer is required|object cannot be interpreted as an integer"),
        ("setDataDir", ("foo", 1, "bar"), {}, r"function takes at most 2 arguments"),
        ("setDataDir", (), {"foo": 1}, r"takes no keyword arguments"),
        ("getCurrentCfg", (1,), {}, r"takes no arguments"),
        ("getCurrentCfg", (), {"foo": 1}, r"takes no keyword arguments"),
        ("getStagingCfg", (1,), {}, r"takes no arguments"),
        ("getStagingCfg", (), {"foo": 1}, r"takes no keyword arguments"),
    ],
)
def test_CfgMgr_method_bad_args(cfg_mgr, method_name, args, kwargs, error_message):
    """Test to ensure methods raise TypeError with incorrect arguments."""
    method = getattr(cfg_mgr, method_name)
    with pytest.raises(TypeError, match=error_message):
        method(*args, **kwargs)


def test_CfgMgr_getDataDir(cfg_mgr):
    """Test to ensure that getDataDir returns a string."""
    data_dir = cfg_mgr.getDataDir()
    assert isinstance(data_dir, str)
    assert len(data_dir) > 0


def test_CfgMgr_setDataDir(cfg_mgr):
    """Test to ensure that setDataDir sets the data directory."""
    new_data_dir = "/new/data/dir"
    cfg_mgr.setDataDir(new_data_dir)
    assert cfg_mgr.getDataDir() == new_data_dir


def test_CfgMgr_getCurrentCfg(cfg_mgr):
    """Test to ensure that getCurrentCfg returns a SrvConfig object."""
    current_config = cfg_mgr.getCurrentCfg()
    assert isinstance(current_config, kea.SrvConfig)


def test_CfgMgr_getStagingCfg(cfg_mgr):
    """Test to ensure that getStagingCfg returns a SrvConfig object."""
    staging_config = cfg_mgr.getStagingCfg()
    assert isinstance(staging_config, kea.SrvConfig)
