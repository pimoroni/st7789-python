import pytest


def test_setup(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24)
    del display


def test_backlight(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24, backlight=19)
    display.set_backlight(1)


def test_reset(gpiodevice, gpiod, spidev, numpy, st7789):
    display = st7789.ST7789(port=0, cs=0, dc=24, rst=19)
    display.reset()


def test_unsupported_rotation_320_x_240_90(gpiodevice, gpiod, spidev, numpy, st7789):
    with pytest.raises(ValueError):
        display = st7789.ST7789(port=0, cs=0, dc=24, width=320, height=240, rotation=90)
        del display


def test_unsupported_rotation_320_x_240_270(gpiodevice, gpiod, spidev, numpy, st7789):
    with pytest.raises(ValueError):
        display = st7789.ST7789(
            port=0, cs=0, dc=24, width=320, height=240, rotation=270
        )
        del display
