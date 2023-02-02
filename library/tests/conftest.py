import sys
import mock
import pytest

@pytest.fixture(scope='function', autouse=False)
def GPIO():
    """Mock OPi.GPIO module."""

    GPIO = mock.MagicMock()
    # Fudge for Python < 37 (possibly earlier)
    sys.modules['OPi'] = mock.Mock()
    sys.modules['OPi'].GPIO = GPIO
    sys.modules['OPi.GPIO'] = GPIO
    yield GPIO
    del sys.modules['OPi']
    del sys.modules['OPi.GPIO']


@pytest.fixture(scope='function', autouse=False)
def spidev():
    """Mock Spidev module."""

    spidev = mock.MagicMock()

    sys.modules['spidev'] = spidev
    yield spidev
    del sys.modules['spidev']
