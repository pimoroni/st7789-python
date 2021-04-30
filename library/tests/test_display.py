import pytest

def test_display_pil_image(GPIO, spidev):
    from PIL import Image
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24)

    image = Image.new("RGB", (display.width, display.width))
    display.display(image)


def test_display_numpy_array(GPIO, spidev):
    import numpy
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24)

    image = numpy.empty((display.width, display.height, 3))
    display.display(image)
