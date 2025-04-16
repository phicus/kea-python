import kea


def pytest_sessionstart(session):
    # Initialize the kea logger
    kea._loggerInit("pytest")
