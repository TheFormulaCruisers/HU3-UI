# test the buttons of the c3 with this code

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup( 4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set pin 4 to be an input pin and set initial value to be pulled low (off) switch 1 (top left)
GPIO.setup( 17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 2
GPIO.setup( 27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 3 (bottom left)
GPIO.setup( 22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 4 (top right)
GPIO.setup( 5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 5
GPIO.setup( 13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch 6
GPIO.setup( 6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Switch  (bottom right)


def button_test():
    a,b,c,d,e,f,g = 0
    
    if GPIO.input(4) == GPIO.HIGH():
        print(1)
    if GPIO.input(17) == GPIO.HIGH():
        print(2)
    if GPIO.input(27) == GPIO.HIGH():
        print(3)
    if GPIO.input(22) == GPIO.HIGH():
        print(4)
    if GPIO.input(5) == GPIO.HIGH():
        print(5)
    if GPIO.input(13) == GPIO.HIGH():
        print(6)
    if GPIO.input(6) == GPIO.HIGH():
        print(7)
        

button_test()