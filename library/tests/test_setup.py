import sys
import mock


def test_setup():
    sys.modules['numpy'] = mock.Mock()
    sys.modules['spidev'] = mock.Mock()
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi.GPIO'] = mock.Mock()

    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24)
    del display
