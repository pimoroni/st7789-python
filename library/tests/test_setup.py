import pytest

def test_setup(GPIO, spidev):
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24)
    del display


def test_backlight(GPIO, spidev):
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24, backlight=19)
    display.set_backlight(1)


def test_reset(GPIO, spidev):
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24, rst=19)
    display.reset()


def test_unsupported_rotation_320_x_240_90(GPIO, spidev):
    import ST7789
    with pytest.raises(ValueError):
        display = ST7789.ST7789(port=0, cs=0, dc=24, width=320, height=240, rotation=90)
        del display


def test_unsupported_rotation_320_x_240_270(GPIO, spidev):
    import ST7789
    with pytest.raises(ValueError):
        display = ST7789.ST7789(port=0, cs=0, dc=24, width=320, height=240, rotation=270)
        del display