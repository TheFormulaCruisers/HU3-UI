# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:55:05 2019

@author: Kevin Lee
"""
#import libraries
#import * is import all
from tkinter import * 
#math used for calculations
import math
#time used for keeping track of the time
import time
from time import sleep

#import os and datetime used for saving data on excel and writing it to USB
import os
from datetime import datetime

#import classes
import MainMidWindow as mw

#import spidev


# spidev used for SPI communication
#import spidev

#==============================================Global Variables================
global WindowX            
WindowX = 1200

global WindowY
WindowY = 840  

global FormulaOrange1
FormulaOrange1 =  '#ee6d24'

global FormulaBlue1
FormulaBlue1 =  '#12bfd7'

global FormulaBlack1
FormulaBlack1 = '#1d323e'

global count
count =0

global countcheck
countcheck = 0

global spinBrake
spinBrake = 0
global spinGas
spinGas = 0

global degree_sign
degree_sign= u'\N{DEGREE SIGN}' 

global closeVariable
closeVariable = 0 

global updatedResult
updatedResult = []

#==============================================================================   

# =============================================================================
 
class BotMidWindow:      
    def __init__(self, window, result, sensorWindow):
#        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        
    #Define variables
        
        self.window = window
        self.sensorWindow = sensorWindow
        self.window2 = 0
        self.angle  = 0
        self.counter = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        
        self.result = result
        
        self.centerx = 410
        self.centery = 210
        self.old_choice = 0
        self.color = '#000000'

        #PointerLengths
        self.arrow =  [1,1,6,1]
        
        # ALL attributes of class here
        self.rect = 0   # no rectangle yet
        self.index = 0  # no arrow yet
        self.BotCanvas = 0 # no canvas yet
        
        
        #PointerLengths
        self.screen_1 = [3,3,3,-1]
        
        #Setup variables for all temperature based functions
        self.temp = 0
        self.temp_dir = 1
        self.text_temp = 0  
        
        #Make a canvas in the bottom half of the screen to place other objects inside of and give it the name BotCanvas.
        self.BotCanvas = Canvas(self.window, width= 840, height=170,borderwidth = 0.0, bg='black', highlightthickness=0)
        self.BotCanvas.pack() #place the created canvas into the window.
        
        #Sensor simulator
        #Load button + spinbox
#TEST   self.spin = StringVar()
#TEST   self.spinBox = Spinbox(self.BotCanvas, from_=0, to=100, width = 5, bg = 'snow')
#TEST   self.spinBox.place(relx=0.05,rely=0.5)
        
        #Make a button for inputting "sensordata"
        #Make a button named "Load" in the Canvas named "Botcanvas", with background color "snow" and execute the function useSensor. 
#TEST   self.sensorButton = Button(self.BotCanvas, text = 'Load', command = self.useSensor, bg = 'snow', height = 1) 
#TEST   self.sensorButton.place(relx=0.12, rely=0.5) # Place the button 50 pixels to the right and 150 pixels down (top left is 0,0).
        
        #Make a label (a box to place text in).
        #Place the label in BotCanvas, with 10 pixels of empty room to the left and right of the text. Position it at coordinates (360,340) and give it font Courier with size 20 and make it bold.
#TEST    self.sensorData = Label(self.BotCanvas, padx =10 , textvariable=self.spin, bg = 'black', fg = 'white')
#TEST    self.sensorData.config(font=("Courier 20 bold"))
#TEST    self.sensorData.place(relx= 0.5, rely=0.1)
        
#TEST    #Brake pedal position
#        self.spinBrake = StringVar()
#        self.spinBoxBrake = Spinbox(self.BotCanvas, from_=0, to=120, width = 5, bg = 'snow')
#        self.spinBoxBrake.place(relx=0.05, rely=0.1)
        
#        self.sensorButtonBrake = Button(self.BotCanvas, text = 'Brake', command = self.Update_brake, bg = 'snow', height = 1)
#        self.sensorButtonBrake.place(relx=0.12, rely=0.1)
        
#TEST    #Gas pedal position 
#        self.spinGas = StringVar()
#        self.spinBoxGas = Spinbox(self.BotCanvas, from_=0, to=180, width = 5, bg = 'snow')
#        self.spinBoxGas.place(relx=0.05, rely=0.3)
        
#        self.sensorButtonGas = Button(self.BotCanvas, text = 'Gas', command = self.Update_gas, bg = 'snow', height = 1)
#        self.sensorButtonGas.place(relx=0.12, rely=0.3)

        
        
    #Function useSensor is used to update the value of self.spin to what is currently the value in the spinbox.
#    def useSensor(self):
#        self.spin.set(str(self.spinBox.get()))
    
#    def Update_brake(self):
#        global spinBrake #To alter the value of the global variable it has to be specified you are using the global variable first
#        spinBrake = float(self.spinBoxBrake.get())
        
#    def Update_gas(self):
#        global spinGas #To alter the value of the global variable it has to be specified you are using the global variable first
#        spinGas = float(self.spinBoxGas.get())
    
    #Animated Polygon, Animated Polygon currently not updating        
    def delete_Poly(self):
#        mydebug(f"WinMid.delete_Poly() self.index={self.index}")
        if self.index > 0: # avoid list of arrows now for simplicity
            self.BotCanvas.delete(self.index)
            self.index = 0

    #function to delete temperature value in the bottom middle window
    def del_temp(self):
        if(self.text_temp > 0):
            self.BotCanvas.delete(self.text_temp)
            self.text_temp = 0
    #Function to delete the rectangle in the bottom middle window        
    def delete_rect(self):
#        mydebug(f"WinMid.delete_rect()")
        if self.rect > 0: # avoid list of rects now for simplicity
            self.BotCanvas
            self.BotCanvas.delete(self.rect)
            self.rect = 0
      
    #Function to remove all objects on the bottom half of the screen and reset the background color.    
    def screen_clear(self):
#        mydebug(f"WinMid.screen_clear()")
        self.delete_rect()  #remove rectangular object
        self.delete_Poly()  #remove rotating object
        self.BotCanvas.configure(bg = 'black')   #reset background color to 'snow'
        self.del_temp() #remove temperature text from choice 6
    
    
         
    #Function to determine what to do when a button is pressed.
    def function_choose(self): 
        self.update_val()
#        mydebug(f"WinMid.function_choose() self.choice={self.choice} self.old_choice = {self.old_choice}")
        self.color_update()
        
        if(self.choice != self.old_choice):
#            mydebug(f"WinMid.function_choose() self.screen_clear()")
            self.screen_clear()
            self.old_choice = self.choice
       
        #option 0 which is the start screen. Make an empty window with a width,height,border and background color and place it in the bottom window
        if self.BotCanvas == 0:
            self.screen_clear()

        
        if(self.choice != self.old_choice):
            self.screen_clear()
            self.old_choice = self.choice

        if((self.choice == 1) or GPIO.input(4) == GPIO.HIGH):   ##if button 1 (top left) is pressed do functions below
            self.screen_clear() #empty bottom screen
            self.rotate_Poly()  #put object onto the screen
                        
                        
        elif((self.choice == 2) or GPIO.input(17) == GPIO.HIGH): #if button 2 (mid left) is pressed do functions below
            self.screen_clear() #empty bottom screen
            global closeVariable
            global updatedResult
            if (closeVariable == 0):
                self.window2 = sensorWindow(self.sensorWindow,updatedResult)  
                closeVariable = 1
            elif (closeVariable == 1):
                self.window2.Quit()
                closeVariable = 0
            self.choice = 0
            
        elif((self.choice == 3) or GPIO.input(27) == GPIO.HIGH): #if button 3 (bottom left) is pressed do functions below
            self.screen_clear() #empty Bottom screen
            self.rect = self.BotCanvas.create_rectangle(200, 200, 200 + (self.angle//10)%1000 , 300, fill='blue')
            
            
        elif((self.choice == 4) or GPIO.input(22) == GPIO.HIGH): #if button 4 (top right) is pressed do functions below
            self.screen_clear() #empty bottom screen
            self.rect = self.BotCanvas.create_rectangle(300, 300, 400, 400, fill=self.color)
         
        elif((self.choice == 5) or GPIO.input(5) == GPIO.HIGH): #if button 5 (top mid left) is pressed do functions below
            self.screen_clear() #empty bottom screen
            self.rect = self.BotCanvas.create_rectangle(200, 200, 200 + (self.angle//10)%1000 , 300, fill=self.color)

        
        elif((self.choice == 6) or GPIO.input(13) == GPIO.HIGH): #if button 6 (bottom mid left) is pressed do functions below
            self.screen_clear() #empty bottom screen
            self.temp_gradient()

        elif((self.choice == 7) or GPIO.input(6) == GPIO.HIGH): #if button 7 (bottom right) is pressed do functions below
            self.screen_clear() #empty bottom screen
            #add function for button 7 here      
            
        elif(closeVariable == 1):
            self.window2.Update_val(updatedResult)

#            print("Do Nothing") #if the option is not 1-7 print do nothing to stop errors (also for debugging)


    #function to adjust color
    def colorize(self,a,b,c):
        self.color = '#%02x%02x%02x' % (a, b, c)
#        print(self.color, b)

        
    # function to update the color in the bottom middle window        
    def temp_gradient(self):
        self.temp += self.temp_dir # .. was 1 (too small to see something)
        
        if(self.temp >= 250 or self.temp <=0 ):
            self.temp_dir = -self.temp_dir
            
            
        self.del_temp()   
        self.colorize(255, 255-self.temp, 0) #Color goes from yellow to red as temp goes up and down
#        mydebug(f"WinMid.temp_gradient() self.temp_gradient={self.angle}")
        self.BotCanvas.configure(bg = self.color) #Set the background color to the updated color                       
        self.text_temp = self.BotCanvas.create_text(420,240, text = int(self.temp/250*60) , fill="black", font = ("Purisa", 30)) #Make some text to display the temperature
    

    
    
    
    #function to rotate 
    def rotate_Poly(self):
#        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index}")

         # .. was 1 (too small to see something)
        
        # delete old arrow
        self.delete_Poly() 
        # draw new arrow
        self.index = self.BotCanvas.create_polygon(
            [       self.centerx + self.screen_1[0] * self.size * math.cos(math.radians(self.angle))      , self.centery + self.screen_1[0] * self.size* math.sin(math.radians(self.angle))  ,
                    self.centerx + self.screen_1[1] * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.screen_1[1] * self.size *math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.screen_1[2] * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.screen_1[2] * self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.screen_1[3] * self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.screen_1[3] * self.size * math.sin(math.radians(self.angle + 270))
            ], fill = 'purple')    
    
    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb 

    def color_update(self):
        self.color = self._from_rgb((0,0,((self.angle//10)%250)))
        
        
    def update_val(self):
        WindowY = self.window.winfo_height()
        WindowX = self.window.winfo_width()

        self.BotCanvas.delete("all")
        
        
        self.BotCanvas.create_text(WindowX/3.5, WindowY/4, text =  '{} {}'.format(int(self.result[0]), "%") , font=("Purisan", 20), fill="snow")
        self.BotCanvas.create_text(WindowX/3.5, WindowY/2, text = '{} {}'.format(int(self.result[1]), "%"), font=("Purisan", 20), fill="snow") 
#        #Make text under gas meter(green bar)
#        self.text.append(self.MainMidWindow.create_text(WindowX/1.12, WindowY/1.5, text = '{} {}'.format(int(spinGas),"%"), font=("Purisan", 20), fill="snow"))
        self.BotCanvas.create_rectangle(WindowX/2.5, WindowY/6, WindowX/2.5+self.result[0], WindowY/3, fill='red3')
#       self.my_rectangle = self.round_rectangle(40, 250-((220-self.angle-20)/220)*200, 140, 250 , radius=20, fill="red3")
        self.BotCanvas.create_rectangle(WindowX/2.5, WindowY/2.5, WindowX/2.5+self.result[1], WindowY/1.75, fill='green2')

#        self.rect.append(self.MainMidWindow.create_rectangle(WindowX/(840/720), WindowY/(840/(275*1.83)), WindowX/(840/780), WindowY/(840/((275-(spinGas))*1.83)), fill='green2'))

        
        self.angle += 1
        self.color_update()
    
# =============================================================================

# =============================================================================
#Code for layout and buttons
class Layout(Frame, BotMidWindow):

    def __init__(self, result, parent =  None, ):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"
        
        global updatedResult
        updatedResult = result
        self.result = result
        
        self.angle  = 0
        self.arrow_dir = 1
        self.text = []

        self.height_split = 0.333
        self.width_split = 0.15

        self.time_mark = time.time()
        
        self.mid1 = Frame(parent, bd=0, relief=FLAT, bg=FormulaBlack1, height = self.master.winfo_height(), width = self.master.winfo_width(), highlightthickness=0)
        self.mid2 = Frame(parent, bd=0, relief=FLAT, bg = 'black', height = 400, width = 420, highlightthickness=0)
        self.BotMidWindow = BotMidWindow(self.mid2, self.result , self.master)
        self.MainMidWindow = mw.MainMidWindow(self.mid1, self.result)
        
        #create buttons on the left side
        self.left1_button = Button(self, text = "Sensor1", command = self.left1_, bg = FormulaOrange1) #make a button with name "Sensor1", action when pressed: left1_ and button color "FormulaOrange1"
        self.left2_button = Button(self, text = "Sensor2", command = self.left2_, bg = FormulaOrange1) #make a button with name "Sensor2", action when pressed: left2_ and button color "FormulaOrange1"
        self.left3_button = Button(self, text = "Sensor3", command = self.left3_, bg = FormulaOrange1) #make a button with name "Sensor3", action when pressed: left3_ and button color "FormulaOrange1"

        #create buttons on the right side
        self.right1_button = Button(self, text = "Sensor4", command = self.MainMidWindow.startB, bg = FormulaBlue1) #make a button with name "Sensor4", action when pressed: right1_ and button color "FormulaBlue1"
        self.right2_button = Button(self, text = "Sensor5", command = self.MainMidWindow.resetB, bg = FormulaBlue1) #make a button with name "Sensor5", action when pressed: right2_ and button color "FormulaBlue1"
        self.right3_button = Button(self, text = "Sensor6", command = self.right3_, bg = FormulaBlue1) #make a button with name "Sensor6", action when pressed: right3_ and button color "FormulaBlue1"
        self.right4_button = Button(self, text = "Quit", command = self.right4_, bg = 'red2') #make a button with name "Sensor7", action when pressed: right4_ and button color "FormulaBlue1"

        #bind buttons on keyboard to functions
        self.master.bind('1', self.left1b_) #bind button "1" to function left1b_
        self.master.bind('2', self.left2b_) #bind button "2" to function left2b_
        self.master.bind('3', self.left3b_) #bind button "3" to function left3b_
        self.master.bind('4', self.right1b_) #bind button "4" to function right1b_ 
        self.master.bind('5', self.right2b_) #bind button "5" to function right2b_
        self.master.bind('6', self.right3b_) #bind button "6" to function right3b_
        self.master.bind('7', self.right4b_) #bind button "7" to function right4b_
        self.master.bind('a', self.accelerate) #bind button "a" to function accelerate
        self.master.bind('d', self.decelerate) #bind button "d" to function decelerate


        #Define BotMidWindow and MainMidWindow in this class

        
        #Has to be changed to the button next to the UI screen. This button starts the timer. 
        self.master.bind('t', self.MainMidWindow.start)

        #GPIO.add_event_detect(4,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

        
    
    def display(self):
        
        #place the buttons created to display sensor data on the right place with the right size (rel = relative size compared to window it is placed inside of, so relative x/y position and height/width)
        self.pack(fill = BOTH, expand  = 1)
        self.left1_button.place(relx = 0, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        self.left2_button.place(relx = 0, rely =  self.height_split, relwidth = self.width_split, relheight = self.height_split)
        self.left3_button.place(relx = 0, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)        
        self.right1_button.place(relx = 1-self.width_split, rely = 0, relwidth = self.width_split, relheight = self.height_split*0.75)
        self.right2_button.place(relx = 1- self.width_split, rely = self.height_split*0.75, relwidth = self.width_split, relheight = self.height_split*0.75)
        self.right3_button.place(relx = 1-self.width_split, rely = 2* self.height_split*0.75, relwidth = self.width_split, relheight = self.height_split*0.75)   
        self.right4_button.place(relx = 1-self.width_split, rely = 2.25* self.height_split, relwidth = self.width_split, relheight = self.height_split*0.75)   
        #Placement botmidwindow and mainmidwindow
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =1., relwidth= 1 - 2*self.width_split)
        self.mid2.place( relx = self.width_split, rely = 0.8,   relheight =0.2,  relwidth= 1 -  2*self.width_split)
        #Update the screen
        self.screen_Updater()


    #Call function to execute the object for the second window screen    
        
#    def test(self):
#        print("Test") 
        
#    def sensorWindow():
        
    
    def screen_Updater(self):
        global updatedResult
#        updatedResult = [x+1 for x in updatedResult]
        #updatedResult = spi.xfer2(msg)
        self.BotMidWindow.function_choose()
        self.MainMidWindow.Update_val(updatedResult) #Make sure gas and brake simulation is not affected.
#        print(int(time.time()*1000 - self.time_mark))
#        self.time_mark = time.time()*1000
        self.master.after(10, self.screen_Updater)

    #Function to simulate gas is being pressed
    def accelerate(self,event):
        self.MainMidWindow.Update_val(0)
    #Function to simulate break is being pressed
    def decelerate(self,event):
        self.MainMidWindow.Update_val(1)


    #functions for the working of clicking on the buttons
    def left1_(self):
        self.BotMidWindow.choice = 1 #if this left1_ function is called set choice in function_choose to be 1    

    def left1b_(self,event):
        self.BotMidWindow.choice = 1 #if this left1b_ function is called set choice in function_choose to be 1
        
    def left2_(self):
        self.BotMidWindow.choice = 2 #if this left2_ function is called set choice in function_choose to be 2    

    def left2b_(self,event):
        self.BotMidWindow.choice = 2 #if this left2b_ function is called set choice in function_choose to be 2
        
    def left3_(self):
        self.BotMidWindow.choice = 3 #if this left3_ function is called set choice in function_choose to be 3

    def left3b_(self,event):
        self.BotMidWindow.choice = 3 #if this left3b_ function is called set choice in function_choose to be 3

    def right1_(self):
        self.BotMidWindow.choice = 4 #if this right_1 function is called set choice in function_choose to be 4    

    def right1b_(self,event):
        self.BotMidWindow.choice = 4 #if this right1b_ function is called set choice in function_choose to be 4       
        
    def right2_(self):
        self.BotMidWindow.choice = 5 #if this right_2 function is called set choice in function_choose to be 5

    def right2b_(self,event):
        self.BotMidWindow.choice = 5 #if this right2b_ function is called set choice in function_choose to be 5       
           
    def right3_(self):
        self.BotMidWindow.choice = 6 #if this right_3 function is called set choice in function_choose to be 6

    def right3b_(self,event):
        self.BotMidWindow.choice = 6 #if this right3b_ function is called set choice in function_choose to be 6              
        
    def right4_(self):
        self.master.destroy()
        self.BotMidWindow.choice = 7 #if this right_4 function is called set choice in function_choose to be 7
       
    def right4b_(self,event):
        self.master.destroy()
        self.BotMidWindow.choice = 7 #if this right4b_ function is called set choice in function_choose to be 7

# =============================================================================


# =============================================================================

class sensorWindow():
    def __init__(self, window, result):
        self.master = window
        self.result = result
        self.window2 = Toplevel()
        self.Window2X = self.master.winfo_width()
        self.Window2Y = self.master.winfo_height()
#        self.window2.geometry(str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()) + '+-10+0')
        self.window2.geometry(str(self.Window2X) + "x" + str( self.Window2Y)  + '+-10+0')
        self.w2Canvas = Canvas(self.window2, width= self.Window2X, height= self.Window2Y, borderwidth = 0.0, highlightthickness=0, bg='black') #make a plane to place objects inside of with height 420 and width 840
        self.w2Canvas.pack(fill = BOTH, expand = 1)       #.pack() function used to place the object in the window.
        self.w2Canvas.create_rectangle(self.Window2X/2.5, self.Window2Y/6, self.Window2X/2.5+self.result[0], self.Window2Y/3.6, fill='red3')
        self.w2Canvas.create_rectangle(WindowX/2.5, WindowY/2.5, WindowX/2.5+self.result[1], WindowY/2, fill='green2')
               
        self.w2Canvas.create_text(WindowX/3.5, WindowY/4, text =  '{} {}'.format(int(self.result[0]), "%") , font=("Purisan", 20), fill="snow")
        self.w2Canvas.create_text(WindowX/3.5, WindowY/2, text = '{} {}'.format(int(self.result[1]), "%"), font=("Purisan", 20), fill="snow") 

        
        self.sensorWindowTitle = Label(self.window2, text= "Sensor values:", bg = 'black', fg= 'white')
        self.sensorWindowTitle.config(font=('Courier 20 bold'))
        self.sensorWindowTitle.place(relx=0.4, rely=0.1)

        self.window2.bind('l', self.Quit)
        
        quitButton = Button(self.w2Canvas, text = "Quit", command = self.Quit)
        quitButton.place(relx = 0.5, rely = 0.75)
        
#        Add labels to show sensor data with result[X] as variable 
        
    def Quit(self,*args):
        self.window2.destroy()
        global closeVariable
        closeVariable = 0
        
    def Update_val(self, result):
        self.result = result
        self.w2Canvas.delete("all")

        self.w2Canvas.create_rectangle(self.Window2X/2.5, self.Window2Y/6, self.Window2X/2.5+self.result[0]*2, self.Window2Y/3.6, fill='red3')
        self.w2Canvas.create_rectangle(self.Window2X/2.5, self.Window2Y/2.5, self.Window2X/2.5+self.result[1]*2, self.Window2Y/2, fill='green2')
               
        self.w2Canvas.create_text(self.Window2X/3.5, self.Window2Y/4, text =  '{} {}'.format(int(self.result[0]), "%") , font=("Purisan", 20), fill="snow")
        self.w2Canvas.create_text(self.Window2X/3.5, self.Window2Y/2, text = '{} {}'.format(int(self.result[1]), "%"), font=("Purisan", 20), fill="snow") 

        
# =============================================================================


        
