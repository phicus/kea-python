import kea
import pytest


@pytest.fixture()
def host():
    """Fixture to create a single instance of Host"""
    return kea.Host("cafecafe42", "hw-address", 0, "198.51.100.42")


def test_Host_getHostId(host):
    # Call the getHostId function and check the result
    host_id = host.getHostId()
    assert isinstance(host_id, int), "Host ID should be an integer"


def test_Host_toElement(host):
    # Call the toElement function and check the result
    element = host.toElement()
    assert isinstance(element, dict), "Element should be a dictionary"
    assert element == {
        "boot-file-name": "",
        "client-classes": [],
        "hostname": "",
        "hw-address": "ca:fe:ca:fe:42",
        "ip-address": "198.51.100.42",
        "next-server": "0.0.0.0",
        "option-data": [],
        "server-hostname": "",
    }, "Element should match expected dictionary"


def test_Host_getIdentifier(host):
    # Call the getIdentifier function and check the result
    identifier = host.getIdentifier()
    assert isinstance(identifier, str), "Identifier should be a string"
    assert "hwaddr=CAFECAFE42" in identifier, "String representation should contain identifier"


def test_Host_use_count(host):
    # Call the use_count property and check the result
    use_count = host.use_count
    assert isinstance(use_count, int), "use_count should be an integer"


def test_Host_str(host):
    # Call the __str__ function and check the result
    str_representation = str(host)
    assert isinstance(str_representation, str), "String representation should be a string"
    assert "hwaddr=CAFECAFE42" in str_representation, "String representation should contain identifier"
