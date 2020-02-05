# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:38:07 2019

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

#import ImageTk and Image for using images
from PIL import ImageTk, Image

global WindowX            

global WindowY

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

#Spinbox variables
global spinTemp
spinTemp = 0.0
global spinBrake
spinBrake = 0
global spinGas
spinGas = 0
global spinSpeed
spinSpeed = 0
global spinBattery
spinBattery = 100


global degree_sign
degree_sign= u'\N{DEGREE SIGN}'

class MainMidWindow:
    def __init__(self, window, sensorData):
#        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = -20
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.arrow_dir = 1
        self.text = []
        
        
        heat_img = Image.open("Heat_Symbol.jpg")
        heat_img = heat_img.resize((75, 75), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(heat_img)

        
        self.sensorData = sensorData
        
        # PointerLengths for the rpm arrow
        self.L_N = 0.2
        self.L_E = 3
        self.L_S = 0.2
        self.L_W = 4
        self.L_W_temp = 2
        
        
        # ALL attributes of class here
        self.rect = []   # no rectangle yet

        self.state = 0
        self.speedArrow = 0
        self.line = 0
        
        # Temperature variables
        self.temp = 0
        self.text_temp = 0
        self.temp_dir = 1
        
        # Speed meter variales
        self.speedMeter = 0
        self.tempMeter = 0

        self.coord = 275,90,565,390
        
        # Brake bar
        self.brakeBar = 0

        self.centerx = 840/2           #center window x-axis is width divided by 2  
        self.centery = 420/2         #center window y-axis is height divided by 2
        self.MainMidWindow = Canvas(self.window, width= 840, height=420, borderwidth = 0.0, highlightthickness=0, bg='black') #make a plane to place objects inside of with height 420 and width 840
        self.MainMidWindow.pack(fill = BOTH, expand = 1)       #.pack() function used to place the object in the window.
        
        #Create a label for temperature and the variable to be displayed in the label.
        self.temperature = StringVar()
        self.tempLabel = Label(self.MainMidWindow, padx =10, textvariable=self.temperature, bg = 'black', fg = 'black')
        self.tempLabel.config(font=("Courier 20 bold"))
        
        #Battery label
        self.battery = StringVar()
        self.batteryLabel = Label(self.MainMidWindow, textvariable=self.battery, bg = 'red', fg = 'black')
        self.batteryLabel.config(font=("Courier 20 bold"))
        self.batteryLabel.place(relx=0.05, rely=0.07)
        
        #Create a label and button for time and the variable to be displayed in the label.
        self.t = StringVar()
        self.t.set("00:00:00")
        self.timeLabel = Label(self.MainMidWindow,textvariable=self.t, bg = 'black', fg = 'white') 
        self.timeLabel.config(font=("Courier 30 bold"))                              
        self.timeLabel.place(relx=0.7, rely=0.05)
        
        self.tempImg = Label(self.MainMidWindow, image = self.image, borderwidth = 0, highlightthickness = 0)
        self.temp_C = Label(self.MainMidWindow, text = "C", borderwidth = 0, highlightthickness = 0, bg = 'black', fg = 'white', font=("italic",20, "bold"))
        self.temp_H = Label(self.MainMidWindow, text = "H", borderwidth = 0, highlightthickness = 0, bg = 'black' , fg = 'white', font=("italic",20,"bold"))
#        self.temp_C.configure(size=20)                             
        self.temp_C.place(relx=0.065, rely=0.43)
        self.temp_H.place(relx=0.23, rely=0.33)

        
#TEST   #Create a button to start the timer in the top right of the screen with a black background so it cannot be seen. This button can also be activated by pressing the "t" button on your keyboard.
#TEST   self.bt1 = Button(self.MainMidWindow,text="", width = 5, command=self.startB, font=("Courier 12 bold"), bg = 'black',fg = 'white', bd=0)
#TEST   self.bt1.place(x=780,y=0)
        
        #Sensor simulator
        #Create a spinbox with activation button to simulate different temperatures    
        #Speed
#TEST   self.spinSpeed = StringVar()
#TEST   self.spinBoxSpeed = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
#TEST   self.spinBoxSpeed.place(relx=0.05,y=250)
#TEST   self.sensorButtonSpeed = Button(self.MainMidWindow, text = 'Speed', command = self.Update_speed, bg = 'snow', height = 1)
#TEST   self.sensorButtonSpeed.place(relx=0.12, y=250)
        
        
#        #The following commented code has been moved to BotMidWindow
#        #Brake pedal position
#        self.spinBrake = StringVar()
#        self.spinBoxBrake = Spinbox(self.MainMidWindow, from_=0, to=120, width = 5, bg = 'snow')
#        self.spinBoxBrake.place(relx=0.05,y=200)
#        
#        self.sensorButtonBrake = Button(self.MainMidWindow, text = 'Brake', command = self.Update_brake, bg = 'snow', height = 1)
#        self.sensorButtonBrake.place(relx=0.12, y=200)
#        
#        #Gas pedal position
#        self.spinGas = StringVar()
#        self.spinBoxGas = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
#        self.spinBoxGas.place(relx=0.05,y=150)
#        
#        self.sensorButtonGas = Button(self.MainMidWindow, text = 'Gas', command = self.Update_gas, bg = 'snow', height = 1)
#        self.sensorButtonGas.place(relx=0.12, y=150)
#        
        #Temperature
#TEST   self.spinTemp = StringVar()
#TEST   self.spinBoxTemp = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
#TEST   self.spinBoxTemp.place(relx=0.05,y=350)
        
#TEST   self.sensorButtonTemp = Button(self.MainMidWindow, text = 'Temp', command = self.Update_temp, bg = 'snow', height = 1)
#TEST   self.sensorButtonTemp.place(relx=0.12, y=350)
        
        #Battery
#TEST   self.spinBattery = StringVar()
#TEST   self.spinBoxBattery = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
#TEST   self.spinBoxBattery.place(relx=0.05,y=300)
        
#TEST   self.sensorButtonBattery = Button(self.MainMidWindow, text = 'Battery', command = self.Update_battery, bg = 'snow', height = 1)
#TEST   self.sensorButtonBattery.place(relx=0.12, y=300)

    
    def Update_val(self, result):
        
        self.sensorData = result
        #Current window size variables 
        WindowY = self.window.winfo_height()
        WindowX = self.window.winfo_width()        

        self.MainMidWindow.delete("all")    

        #Make text under the rpm meter (middle moving arrow)
        self.text.append(self.MainMidWindow.create_text(WindowX/2, WindowY/1.5, text = '{} {}'.format(int(self.sensorData[3]), "km/h"), font=("Purisan", 20), fill="snow")) 
        #Make the text under the break bar (red bar)
#        self.text.append(self.MainMidWindow.create_text(WindowX/9.33, WindowY/1.5, text =  '{} {}'.format(int(spinBrake), "%") , font=("Purisan", 20), fill="snow"))
        #Make text under gas meter(green bar)
#        self.text.append(self.MainMidWindow.create_text(WindowX/1.12, WindowY/1.5, text = '{} {}'.format(int(spinGas),"%"), font=("Purisan", 20), fill="snow"))
 
        #Update rectangles for gas and brake
#        self.rect.append(self.MainMidWindow.create_rectangle(WindowX/(840/60), WindowY/(840/(275*1.83)), WindowX/(840/120), WindowY/(840/((275-(spinBrake))*1.83)), fill='red3'))
#       self.my_rectangle = self.round_rectangle(40, 250-((220-self.angle-20)/220)*200, 140, 250 , radius=20, fill="red3")
#        self.rect.append(self.MainMidWindow.create_rectangle(WindowX/(840/720), WindowY/(840/(275*1.83)), WindowX/(840/780), WindowY/(840/((275-(spinGas))*1.83)), fill='green2'))
       

        #Battery display
        #Outside battery colors
        self.my_rectangle = self.round_rectangle(WindowX/(840/35), WindowY/(840/40), WindowX/(840/255), WindowY/(840/115), radius=20, fill="white")
        self.my_rectangle = self.round_rectangle(WindowX/(840/190), WindowY/(840/52), WindowX/(840/265), WindowY/(840/103), radius=20, fill="white")

        #Battery label value and color
        self.battery.set(str(int(result[2])) + "%")
        if(int(self.sensorData[2])>75):    
            self.batteryLabel.config(bg = 'green3')
            self.my_rectangle = self.round_rectangle(WindowX/(840/42), WindowY/(840/47), WindowX/(840/248), WindowY/(840/108), radius=10, fill="green3")

        if(int(self.sensorData[2])>50 and int(self.sensorData[2])<=75):
            self.batteryLabel.config(bg = 'gold')
            self.my_rectangle = self.round_rectangle(WindowX/(840/42), WindowY/(840/47), WindowX/(840/200), WindowY/(840/108), radius=10, fill="gold")

        if(int(self.sensorData[2])>25 and int(self.sensorData[2])<=50):
            self.batteryLabel.config(bg = 'dark orange')
            self.my_rectangle = self.round_rectangle(WindowX/(840/42), WindowY/(840/47), WindowX/(840/150), WindowY/(840/108), radius=10, fill="dark orange")
            
        if(int(self.sensorData[2])>=0) and int(self.sensorData[2])<=25:
            self.batteryLabel.config(bg = 'red')
            self.my_rectangle = self.round_rectangle(WindowX/(840/42), WindowY/(840/47), WindowX/(840/100), WindowY/(840/108), radius=10, fill="red")
        
        #Create speedmeter display
        self.speedMeter = self.make_speedmeter([WindowX/(840/200), WindowY/(840/190), WindowX/(840/650), WindowY/(840/650)], -120, 121, 8, 40)    
        self.tempMeter = self.make_speedmeter([WindowX/(840/20), WindowY/(840/200), WindowX/(840/250), WindowY/(840/450)], -120, 71, 5, 70)
        
        
        zero = self.MainMidWindow.create_text(WindowX/(840/270), WindowY/(840/510), fill="white", font="times 25", text= "0")
        twenty = self.MainMidWindow.create_text(WindowX/(840/260), WindowY/(840/390), fill="white", font="times 25", text= "20")
        fourty =self.MainMidWindow.create_text(WindowX/(840/310), WindowY/(840/280), fill="white", font="times 25", text= "40")
        sixty = self.MainMidWindow.create_text(WindowX/(840/425), WindowY/(840/240), fill="white", font="times 25", text= "60")
        eighty = self.MainMidWindow.create_text(WindowX/(840/530), WindowY/(840/280), fill="white", font="times 25", text= "80")
        hundred = self.MainMidWindow.create_text(WindowX/(840/580), WindowY/(840/390), fill="white", font="times 25", text= "100")
        hundredtwenty = self.MainMidWindow.create_text(WindowX/(840/560), WindowY/(840/510), fill="white", font="times 25", text= "120")

        # Draw new arrow
        # Create an object with coordinates [x1,y1,x2,y2,x3,y3]
        self.speedArrow = self.MainMidWindow.create_polygon(
            [      [ WindowX/2 + self.L_S * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[3]*2.083 + 55)) , WindowY/4 + self.L_S * self.size* (WindowY/840) * math.sin(math.radians(self.sensorData[3]*2.083 + 55)) + WindowY/(840/200) ],
                   [ WindowX/2 + self.L_W * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[3]*2.083 + 145)), WindowY/4 + self.L_W * self.size * (WindowY/840) * math.sin(math.radians(self.sensorData[3]*2.083 + 145)) + WindowY/(840/200) ] ,  
                   [ WindowX/2 + self.L_N * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[3]*2.083 + 235)), WindowY/4 + self.L_N  * self.size * (WindowY/840) * math.sin(math.radians(self.sensorData[3]*2.083 + 235)) + WindowY/(840/200) ]
            ] , fill='red'        ) 
    
        self.temperatureArrow = self.MainMidWindow.create_polygon(
            [      [ WindowX/6 + self.L_S * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[4]*2.083 + 50)) - WindowX/(840/10), WindowY/8 + self.L_S * self.size* (WindowY/840) * math.sin(math.radians(self.sensorData[4]*2.083 + 50)) + WindowY/(840/210) ],
                   [ WindowX/6 + self.L_W_temp * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[4]*2.083 + 140)) - WindowX/(840/10), WindowY/8 + self.L_W_temp * self.size * (WindowY/840) * math.sin(math.radians(self.sensorData[4]*2.083 + 140)) + WindowY/(840/210) ] ,  
                   [ WindowX/6 + self.L_N * self.size * (WindowX/840) * math.cos(math.radians(self.sensorData[4]*2.083 + 230)) - WindowX/(840/10), WindowY/8 + self.L_N  * self.size * (WindowY/840) * math.sin(math.radians(self.sensorData[4]*2.083 + 230)) + WindowY/(840/210) ]
            ] , fill='red'        )
        
        #create line to display how far the steering wheel is turned    
#        self.line = self.MainMidWindow.create_line( WindowX/(840/(330+self.angle)), WindowY/(840/50) , WindowX/(840/(330+self.angle)), WindowY/(840/90), fill = "red" )
             
        #If the temperature is under half of its max temperature display the color from blue to white
        #Temperature value has to be between 0 and 255 and a whole number otherwise the color of the label won't work
        if (float(self.sensorData[4]) >= 50): 
            
#            self.temperature.set(str(self.sensorData[4]) + " C" + degree_sign)
#            self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (75+int(round(self.sensorData[4]*2)), 75+int(round(self.sensorData[4]*2)), 255))
#            self.tempLabel.place(relx=0.43, rely=0.7)

        #If the temperature is over half of its max temperature display the color from white to red
        #Temperature value has to be between 0 and 255 and a whole number otherwise the color of the label won't work
#        else:
#            self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (255, 255+180-int(round(self.sensorData[4])*2), 255+180-int(round(self.sensorData[4])*2)))
#            self.tempLabel.place(relx=0.18, rely=0.7)
#            self.temperature.set("Warning "+ str(self.sensorData[4]) + " C" + degree_sign)
            self.tempImg.place(relx = 0.11, rely = 0.4)

        
        
#    #function to adjust the temperature label        
#    def Update_temp(self):
#        self.delete_temp()
#        global spinTemp
#        spinTemp = float(self.spinBoxTemp.get()) #Get the value of the spinbox and save it as a float
#        
#    def Update_brake(self):
#        global spinBrake #To alter the value of the global variable it has to be specified you are using the global variable first
#        spinBrake = float(self.spinBoxBrake.get())
#        
#    def Update_gas(self):
#        global spinGas #To alter the value of the global variable it has to be specified you are using the global variable first
#        spinGas = float(self.spinBoxGas.get())
#        
#    def Update_speed(self):
#        global spinSpeed #To alter the value of the global variable it has to be specified you are using the global variable first
#        spinSpeed = float(self.spinBoxSpeed.get())
#        
#    def Update_battery(self):
#        global spinBattery
#        spinBattery = float(self.spinBoxBattery.get())
               
########## timer functions
            
    #Check if it is the first time the button is pressed so there are no errors
    def start(self,event):
        global countcheck
        countcheck = countcheck + 1
        global count
        count = 0
        if (countcheck == 1):
            self.timer()
            
    #Check if it is the first time the button is pressed so there are no errors
    def startB(self):
        global countcheck
        countcheck = countcheck + 1
        global count
        count = 0
        if(countcheck == 1):
            self.timer()            
    
    def resetB(self):
        global countcheck
        if (countcheck >= 1):
            global count
            countcheck = 0
            count = 1
            self.t.set('00:00:00')
            
    #Function to start the timer and add one second every 960 ms (this can be changed if it is too fast/slow)  
    def timer(self):
            if(count==0):
                self.d = str(self.t.get())
                h,m,s = map(int,self.d.split(":"))
                
                h = int(h)
                m=int(m)
                s= int(s)
                if(s<59):
                    s+=1
                elif(s==59):
                    s=0
                    if(m<59):
                        m+=1
                    elif(m==59):
                        h+=1
                if(h<10):
                    h = str(0)+str(h)
                else:
                    h= str(h)
                if(m<10):
                    m = str(0)+str(m)
                else:
                    m = str(m)
                if(s<10):
                    s=str(0)+str(s)
                else:
                    s=str(s)
                self.d=h+":"+m+":"+s
                         
                self.t.set(self.d)
                if(count==0):
                    self.MainMidWindow.after(1000,self.timer) # After pressing reset once the timer has started and the pressing the start button before the 970 miliseconds has finished it wil start two times causing the timer to go up by 2 at a time.

###########    
 
    #Function to make rounded rectangles (currently not used)            
    def round_rectangle(self,x1, y1, x2, y2, radius=25, **kwargs):

        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
    
        return self.MainMidWindow.create_polygon(points, **kwargs, smooth=True)

            
## Functions to display speed meter           
    def calc_point(self,angle, width, height):
        return (width * math.cos((- 90 + angle) * math.pi / 180),
                height * math.sin((- 90 + angle) * math.pi / 180))
    def offset_point(self, base, offset):
        """ 
        apply offset onto a base point
        base    a tuple or list -> (x, y)
        offset  a tuple or list -> (offset-x, offset-y)
        """
        return (base[0] + offset[0], base[1] + offset[1])
                
    def draw_tick(self, canvas, center, w, h, angle, r1, r2, width, color):
        p1 = self.calc_point(angle, w / 2 * r1, h / 2 * r1)
        p2 = self.calc_point(angle, w / 2 * r2, h / 2 * r2)
        p1 = self.offset_point(center, p1)
        p2 = self.offset_point(center, p2)
        canvas.create_line(p1 + p2, width = width, fill = color)
    
    def make_speedmeter(self, coord, begin, end, ticks, bigTick):
        width, height = abs(coord[0] - coord[2]), abs(coord[1] - coord[3])
        center = (coord[0] + coord[2]) // 2, (coord[1] + coord[3]) // 2
#        self.MainMidWindow.create_arc(coord, start = 0.0, extent = 360, fill = "black", outline = "white")
        
#        self.draw_tick(self.MainMidWindow, center, width, height, end, 0.88, 0.97, 5, 'gray')        
        if(ticks == 5):
            for i in range(begin, end, ticks):
                if (i  == end-1):
                    
                    w = 5
                    self.draw_tick(self.MainMidWindow, center, width, height, i, 0.88, 0.97, w, 'red3')         
                elif (i == begin):
                    w = 5
                    self.draw_tick(self.MainMidWindow, center, width, height, i, 0.88, 0.97, w, 'white')        
                else:
                    w = 2
                    self.draw_tick(self.MainMidWindow, center, width, height, i, 0.88, 0.97, w, 'gray')        
        if(ticks == 8):
            for i in range(begin, end, ticks):
                w = 3 if i % 40 == 0 else 1
                self.draw_tick(self.MainMidWindow, center, width, height, i, 0.88, 0.97, w, 'gray')        

            
            
                
##

#    #Animated Polygon, Animated Polygon currently not updating        
#    def delete_Poly(self):
##        mydebug(f"WinMid.delete_Poly()")
#        if self.pol > 0: # avoid list of arrows now for simplicity
#            self.MainMidWindow.delete(self.pol)
#            self.pol = 0
#    
#    def delete_rect(self):
#        if len(self.rect)  > 0: # avoid list of rects now for simplicity
#            for i in self.rect:
#                self.MainMidWindow.delete(i)
#            self.rect = []
#
#    def delete_text(self):
#        if len(self.text) > 0:
#            for i in self.text:
#                self.MainMidWindow.delete(i)
#            self.text = []
#            
    #delete temperature text function in the top middle window
#    def delete_temp(self):
#        if(self.text_temp > 0):
#            self.text_temp = 0
  
    #function to adjust color
#    def colorize(self,a,b,c):
#        self.color = '#%02x%02x%02x' % (a, b, c)
#        print(self.color, b)
        

   