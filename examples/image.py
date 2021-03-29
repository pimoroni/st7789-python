#!/usr/bin/env python3
import sys

from PIL import Image
import ST7789 as ST7789

print("""
image.py - Display an image on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.

""")

if len(sys.argv) < 2:
    print("""Usage: {} <image_file> <display_type>

Where <display_type> is one of:
  * square - 240x240 1.3" Square LCD
  * round  - 240x240 1.3" Round LCD (applies an offset)
""".format(sys.argv[0]))
    sys.exit(1)

image_file = sys.argv[1]

try:
    display_type = sys.argv[2]
except IndexError:
    display_type = "square"

# Create ST7789 LCD display class.
disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=40 if display_type == "round" else 0
)

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

# Load an image.
print('Loading image: {}...'.format(image_file))
image = Image.open(image_file)

# Resize the image
image = image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')

disp.display(image)
