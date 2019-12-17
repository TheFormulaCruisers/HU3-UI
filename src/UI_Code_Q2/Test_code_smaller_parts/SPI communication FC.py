# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:21:46 2019

@author: kevin
"""

# spitest.py
# A brief demonstration of the Raspberry Pi SPI interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun Serial 7 Segment display:
# https://www.sparkfun.com/products/11629

#SPI SS-16
#SPI MOSI – 20
#SPI SCLK – 21 


import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 1

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Clear display
msg = 2
result = spi.xfer2(msg)
print(result)
time.sleep(5)

spi.close()