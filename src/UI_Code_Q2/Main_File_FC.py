###
#import libraries

#import * is import all
from tkinter import * 

#math used for calculations
import math

#time used for keeping track of the time
import time
from time import sleep

#import os and datetime, used for saving data on excel and writing it to USB
import os
from datetime import datetime

#import classes from other documents (they have to be in the same directory)
import MainMidWindow as mw #import MainMidWindow.py and name it "mw"
import BotMidWindow as bw #import BotMidWindow.py and name it "bw"


# spidev used for SPI communication
#import spidev
#import RPi.GPIO as GPIO
###


#==============================================Global Variables==============================
global WindowX            
windowX = 1200

global WindowY
windowY = 840  
#============================================================================================



#def mydebug(s):
#    print(s)
                                     
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup( 4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set pin 4 to be an input pin and set initial value to be pulled low (off) switch 1 (top left)
#GPIO.setup( 17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 2
#GPIO.setup( 27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 3 (bottom left)
#GPIO.setup( 22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 4 (top right)
#GPIO.setup( 5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 5
#GPIO.setup( 13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 6
#GPIO.setup( 6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch  (bottom right)
#GPIO.setup(... , GPIO.IN,) #input for SPI connection
#GPIO.setup(... , GPIO.OUT) #output for SPI connection
#GPIO.setup(... , GPIO.OUT) #clock signal pin
 




### SPI code ###
## We only have SPI bus 0 available to us on the Pi
#bus = 0
#
##Device is the chip select pin. Set to 0 or 1, depending on the connections
#device = 1
#
## Enable SPI
#spi = spidev.SpiDev()
#
## Open a connection to a specific bus and device (chip select pin)
#spi.open(bus, device)
#
## Set SPI speed and mode
#spi.max_speed_hz = 500000
#spi.mode = 0
#
## Clear display
#msg = 2
#result = spi.xfer2(msg)
#
#spi.close()
###



## Write data to excel sheet on USB ##
#file = open("E:/test2.csv", "a")
#i=0
#if os.stat("E:/test2.csv").st_size == 0:
#        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
#while True:
#        i=i+1
#        now = datetime.now()
#        file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n")
#        file.flush()
##        time.sleep(1)
##        if (i>=10):
##            break
#file.close()  
##



winsize = str(windowX) + 'x' + str(windowY) #Make a variable named "winsize" with the x and y size as a string.
global master #Make the variable master a global variable
master = Tk() #Make a Tkinter window and call it "master"

master.geometry(winsize) #Give the coordinates stored in winsize to the window so the window is a window of "windowX" pixels wide and "windowY" pixels high
    
Lay = bw.Layout(master) #Lay becomes an object of the class "Layout" from the document "BotMidWindow.py"

master.after(100, Lay.display) #Call the function "display" from class "Layout" after 100 miliseconds
master.mainloop() #Loop forever
    

#sensor data to show: R/G light display "save to leave/ unsafe to leave"

