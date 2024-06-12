def test_240_240(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24, width=240, height=240, rotation=0)
    assert display.width == 240
    assert display.height == 240


def test_240_135(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24, width=240, height=135, rotation=0)
    assert display.width == 240
    assert display.height == 135


def test_320_240(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24, width=320, height=240, rotation=0)
    assert display.width == 320
    assert display.height == 240
