import sys
import mock


def _mock():
    sys.modules['numpy'] = mock.Mock()
    sys.modules['spidev'] = mock.Mock()
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi.GPIO'] = mock.Mock()


def test_240_240():
    _mock()
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24, width=240, height=240, rotation=0)
    assert display.width == 240
    assert display.height == 240
