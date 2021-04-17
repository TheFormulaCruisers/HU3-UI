###
#import libraries

#import * is import all
from tkinter import * 

#math used for calculations
import RPi.GPIO as GPIO

import math

#time used for keeping track of the time
import time
from time import sleep

#import os and datetime, used for saving data on excel and writing it to USB
import os
from datetime import datetime

#import classes from other documents (they have to be in the same directory)
import MainMidWindow as mw #import MainMidWindow.py and name it "mw". Any functions from these files can be called by typing mw.function
import BotMidWindow as bw #import BotMidWindow.py and name it "bw". Any functions from these files can be called by typing bw.function


# spidev used for SPI communication
#import spidev
#import RPi.GPIO as GPIO
###


#==============================================Global Variables==============================
global WindowX            
windowX = 1200 # Define the x value of the display window

global WindowY
windowY = 840  # Define the y value of the display window
#============================================================================================



#def mydebug(s):
#    print(s)
                                     
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup( 4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set pin 4 to be an input pin and set initial value to be pulled low (off) switch 1 (top left)
GPIO.setup( 17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 2
GPIO.setup( 27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 3 (bottom left)
GPIO.setup( 22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 4 (top right)
GPIO.setup( 5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 5
GPIO.setup( 13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 6
GPIO.setup( 6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch  (bottom right)
#GPIO.setup(... , GPIO.IN,) #input for SPI connection
#GPIO.setup(... , GPIO.OUT) #output for SPI connection
#GPIO.setup(... , GPIO.OUT) #clock signal pin
 




### SPI code ###
## We only have SPI bus 0 available to us on the Pi
#bus = 0
#
## Device is the chip select pin. Set to 0 or 1, depending on the connections
#device = 1
#
## Enable SPI
#spi = spidev.SpiDev()
#
## Open a connection to a specific bus and device (chip select pin)
#spi.open(bus, device)
#
## Set SPI speed and mode
#spi.max_speed_hz = 250000 # Faster is too fast for the C3
#spi.mode = 0 # Set the mode to 0, this has to be the samee on the C3
#
## Clear display2
#msg = 2
#sensorData = spi.xfer2(msg)
#
#spi.close()
###



## Write data to excel sheet on USB ##
#file = open("E:/test2.csv", "a") # Open the file that is wanted to store the data in
#i=0
#if os.stat("E:/test2.csv").st_size == 0: # Check if the opened file is empty 
#        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n") # If it is fill the first row with the text Time and Sensor1-5 into six columns
#while True:
#        i=i+1
#        now = datetime.now() # Get the current time
#        file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n") # Write the time, i, -i, i-10, i+5 and i*i to the opened file
#        file.flush()
##        time.sleep(1)
##        if (i>=10):
##            break222
#file.close()  
##

sensorData = [100,100,0,0,0] # Test values for SPI list

global master #Make the variable master a global variable
master = Tk() #Make a Tkinter window and call it "master"

winsize = str(windowX) + 'x' + str(windowY) + '+-10+0'  #Make a variable named "winsize" with the x and y size as a string.2

master.geometry(winsize) #Give the coordinates stored in winsize to the window so the window is a window of "windowX" pixels wide and "windowY" pixels high and places it in the top left of the screen.
    
Lay = bw.Layout(sensorData, master) #Lay becomes an object of the class "Layout" from the document "BotMidWindow.py"

#sensorData = [x+1 for x in sensorData]
print(sensorData)

master.after(100, Lay.display) #Call the function "display" from class "Layout" after 100 miliseconds
master.mainloop() #Loop forever
    

#sensor data to show: R/G light display "save to leave/ unsafe to leave"

