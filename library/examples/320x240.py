#!/usr/bin/env python3
from OrangePi import ST7789
from PIL import Image, ImageDraw

import time

SPI_PORT = 0
SPI_CS = 0
SPI_DC = 27    # PA0
SPI_RES = 17   # PA1
BACKLIGHT = 22 # PA3

# Screen dimensions
WIDTH = 320
HEIGHT = 240

buffer = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(buffer)

draw.rectangle((0, 0, 50, 50), (255, 0, 0))
draw.rectangle((320-50, 0, 320, 50), (0, 255, 0))
draw.rectangle((0, 240-50, 50, 240), (0, 0, 255))
draw.rectangle((320-50, 240-50, 320, 240), (255, 255, 0))

display = ST7789(
    port=SPI_PORT,
    cs=SPI_CS,
    dc=SPI_DC,
    rst=SPI_RES,
    backlight=BACKLIGHT,
    width=WIDTH,
    height=HEIGHT,
    rotation=180,
    spi_speed_hz=60 * 1000 * 1000
)

while True:
    display.display(buffer)
    time.sleep(1.0 / 60)