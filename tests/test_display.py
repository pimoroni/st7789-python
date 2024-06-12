def test_display_pil_image(gpiodevice, gpiod, spidev, st7789):
    from PIL import Image

    display = st7789.ST7789(port=0, cs=0, dc=24)

    image = Image.new("RGB", (display.width, display.width))
    display.display(image)


def test_display_numpy_array(gpiodevice, gpiod, spidev, st7789):
    import numpy

    display = st7789.ST7789(port=0, cs=0, dc=24)

    image = numpy.empty((display.width, display.height, 3))
    display.display(image)
