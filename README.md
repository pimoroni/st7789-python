# Python ST7789

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/st7789-python/test.yml?branch=main)](https://github.com/pimoroni/st7789-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/st7789-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/st7789-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/st7789.svg)](https://pypi.python.org/pypi/st7789)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7789.svg)](https://pypi.python.org/pypi/st7789)

Python library to control an ST7789 TFT LCD display

Designed specifically to work with a ST7789 based 240x240 pixel TFT SPI display. (Specifically the [1.3" SPI LCD from Pimoroni](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout)).

![Animated GIF showing the ST7789 SPI LCD displaying Deploy/Rainbows in alternating frames](https://raw.githubusercontent.com/pimoroni/st7789-python/master/square-lcd-breakout-1.gif)

## Installing

We'd recommend using this library with Raspberry Pi OS Bookworm or later. It requires Python ≥3.7.

## Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get you up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the commands exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
git clone https://github.com/pimoroni/st7789-python
cd st7789-python
./install.sh
```

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

## Development

If you want to contribute, or like living on the edge of your seat by having the latest code, you can install the development version like so:

``` bash
git clone https://github.com/pimoroni/st7789-python
cd st7789-python
./install.sh --unstable
```

## Install stable library from PyPi and configure manually

* Set up a virtual environment: `python3 -m venv --system-site-packages $HOME/.virtualenvs/pimoroni`
* Switch to the virtual environment: `source ~/.virtualenvs/pimoroni/bin/activate`
* Install the library: `pip install st7789`

This will not make any configuration changes, so you may also need to enable:

* spi: `sudo raspi-config nonint do_spi 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

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
