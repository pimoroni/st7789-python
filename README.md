# Python ST7789

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/st7789-python/test.yml?branch=main)](https://github.com/pimoroni/st7789-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/st7789-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/st7789-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/st7789.svg)](https://pypi.python.org/pypi/st7789)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7789.svg)](https://pypi.python.org/pypi/st7789)

Python library to control an ST7789 TFT LCD display

Designed specifically to work with a ST7789 based 240x240 pixel TFT SPI display. (Specifically the [1.3" SPI LCD from Pimoroni](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout)).

![Animated GIF showing the ST7789 SPI LCD displaying Deploy/Rainbows in alternating frames](https://raw.githubusercontent.com/pimoroni/st7789-python/master/square-lcd-breakout-1.gif)

# Installation

Make sure you have the following dependencies:

````
sudo apt-get update
sudo apt-get install python-rpi.gpio python-spidev python-pip python-pil python-numpy
````

Install this library by running:

````
sudo pip install st7789
````

You might also need to enable I2C and SPI in raspi-config. See example of usage in the examples folder.


# Licensing & History

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries, and modified to work with the ST7735 by Clement Skau.

To create this ST7789 driver, it has been hard-forked from st7735-python which was originally modified by Pimoroni to include support for their 160x80 SPI LCD breakout.

## Modifications include:

* PIL/Pillow has been removed from the underlying display driver to separate concerns- you should create your own PIL image and display it using `display(image)`
* `width`, `height`, `rotation`, `invert`, `offset_left` and `offset_top` parameters can be passed into `__init__` for alternate displays
* `Adafruit_GPIO` has been replaced with `RPi.GPIO` and `spidev` to closely align with our other software (IE: Raspberry Pi only)
* Test fixtures have been added to keep this library stable

Pimoroni invests time and resources forking and modifying this open source code, please support Pimoroni and open-source software by purchasing products from us, too!

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Modified from 'Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.' written by Clement Skau.

MIT license, all text above must be included in any redistribution
