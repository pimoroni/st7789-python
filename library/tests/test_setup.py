def test_setup(GPIO, spidev, numpy):
    import ST7789
    display = ST7789.ST7789(port=0, cs=0, dc=24)
    del display
