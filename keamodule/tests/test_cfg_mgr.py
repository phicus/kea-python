import kea
import pytest


@pytest.fixture()
def cfg_mgr():
    """Fixture to create a single instance of CfgMgr."""
    return kea.CfgMgr.instance()


@pytest.mark.parametrize(("args", "kwargs"), [((42,), {}), ((), {"foo": 42})])
def test_cfg_mgr_no_arguments_allowed(args, kwargs):
    """Test to ensure that CfgMgr raises TypeError with incorrect arguments."""
    with pytest.raises(TypeError, match=r"takes no arguments"):
        kea.CfgMgr(*args, **kwargs)


def test_cfg_mgr_is_singleton(cfg_mgr):
    """Test to ensure that CfgMgr follows singleton pattern."""
    assert isinstance(cfg_mgr, kea.CfgMgr), "The instance is not of type CfgMgr"
    assert cfg_mgr is kea.CfgMgr(), "CfgMgr is not a singleton"


def test_cfg_mgr_instance_is_singleton(cfg_mgr):
    """Test to ensure that CfgMgr static method instance follows singleton pattern."""
    instance = kea.CfgMgr.instance()
    assert isinstance(instance, kea.CfgMgr), "The instance is not of type CfgMgr"
    assert instance is kea.CfgMgr.instance(), "CfgMgr.instance() is not a singleton"
    assert instance is cfg_mgr, "CfgMgr and CfgMgr.instance() are not the same"


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
def test_cfg_mgr_method_invalid_args(cfg_mgr, method_name, args, kwargs, error_message):
    """Test to ensure HostMgr method methods raise TypeError with incorrect arguments."""
    method = getattr(cfg_mgr, method_name)
    with pytest.raises(TypeError, match=error_message):
        method(*args, **kwargs)


def test_cfg_mgr_get_data_dir_returns_string(cfg_mgr):
    """Test to ensure that HostMgr method getDataDir returns a string."""
    data_dir = cfg_mgr.getDataDir()
    assert isinstance(data_dir, str), "HostMgr method getDataDir does not return a string"
    assert len(data_dir) > 0, "HostMgr method getDataDir returns an empty string"
    assert "\x00" not in data_dir, "HostMgr method getDataDir contains null character"


def test_cfg_mgr_set_data_dir_updates_directory(cfg_mgr):
    """Test to ensure that HostMgr method setDataDir sets the data directory."""
    new_data_dir = "/new/data/dir"
    cfg_mgr.setDataDir(new_data_dir)
    assert cfg_mgr.getDataDir() == new_data_dir, "HostMgr method setDataDir does not set the data directory"


def test_cfg_mgr_get_current_cfg_returns_srv_config(cfg_mgr):
    """Test to ensure that HostMgr method getCurrentCfg returns a SrvConfig object."""
    current_config = cfg_mgr.getCurrentCfg()
    assert isinstance(current_config, kea.SrvConfig), "HostMgr method getCurrentCfg does not return a SrvConfig object"


def test_cfg_mgr_get_staging_cfg_returns_srv_config(cfg_mgr):
    """Test to ensure that HostMgr method getStagingCfg returns a SrvConfig object."""
    staging_config = cfg_mgr.getStagingCfg()
    assert isinstance(staging_config, kea.SrvConfig)
