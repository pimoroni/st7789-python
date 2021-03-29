#!/usr/bin/env python3
import sys
import math
import time
import colorsys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789

print("""
round.py - Shiny shiny round LCD!

If you're using Breakout Garden, plug a 1.3" ROUND LCD
(SPI) breakout into the front slot.

Usage: {} <style>

Where style is one of:

 * dots - swirly swooshy dots
 * lines - 3D depth effect lines

""".format(sys.argv[0]))

try:
    style = sys.argv[1]
except IndexError:
    style = "dots"

# Create ST7789 LCD display class.
disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    rotation=90,
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=40
)

# Initialize display.
disp.begin()

RADIUS = disp.width // 2

img = Image.new('RGB', (disp.width, disp.height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)


while True:
    t = time.time()
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    angle = t % (math.pi * 2)

    prev_x = RADIUS
    prev_y = RADIUS

    steps = 100.0
    angle_step = 1.0

    if style == "lines":
        steps *= 5
        angle_step = 0.1

    for step in range(int(steps)):
        angle += angle_step

        distance = RADIUS / steps * step
        distance += step * 0.2

        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb((t / 10.0) + distance / 120.0, 1.0, 1.0)]

        x = RADIUS + int(distance * math.cos(angle))
        y = RADIUS + int(distance * math.sin(angle))

        l = ((math.sin(t + angle) + 1) / 2.0) * 10
        if style == "lines":
            draw.line((prev_x + l, prev_y + l, x - l, y - l), fill=(r, g, b))
        else:
            l += 1
            draw.ellipse((x - l, y - l, x + (l * 2), y + (l * 2)), fill=(r, g, b))

        prev_x = x
        prev_y = y

    disp.display(img)
