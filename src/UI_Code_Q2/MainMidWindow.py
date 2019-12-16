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

global WindowX            
windowX = 1200

global WindowY
windowY = 840  

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

global degree_sign
degree_sign= u'\N{DEGREE SIGN}'

class MainMidWindow:
    def __init__(self, window):
#        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = -20
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.arrow_dir = 1
        self.text = []
        
        #PointerLengths for the rpm arrow
        self.L_N = 0.1
        self.L_E = 3
        self.L_S = 0.1
        self.L_W = 2.5
        
        
        # ALL attributes of class here
        self.rect = []   # no rectangle yet

        self.state = 0
        self.pol = 0
        self.line = 0
        self.temp = 0
        self.text_temp = 0
        self.temp_dir = 1
        self.coord = 275,90,565,390

        self.centerx = 840/2           #center window x-axis is width divided by 2  
        self.centery = 420/2           #center window y-axis is height divided by 2
        self.MainMidWindow = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg='black', highlightthickness=0) #make a plane to place objects inside of with height 420 and width 840
        self.MainMidWindow.pack_propagate(0)
        self.MainMidWindow.pack(fill = BOTH, expand = 1)       #.pack() function used to place the object in the window.
        self.TempMainMidWindow = Canvas(self.MainMidWindow, width= 150, height=400,borderwidth = 0.0, bg=FormulaOrange1, highlightthickness = 0) #make a plane inside the MainMidWindoww frame.
        self.TempMainMidWindow.pack(side= BOTTOM)
        
        #Create a label for temperature and the variable to be displayed in the label.
        self.temperature = StringVar()
        self.temperature.set("0")
        self.tempLabel = Label(self.MainMidWindow, padx =10 , textvariable=self.temperature, bg = 'black', fg = 'black')
        self.tempLabel.config(font=("Courier 20 bold"))
        self.tempLabel.place(x=380,y=340)
        
        #Create a label and button for time and the variable to be displayed in the label.
        self.t = StringVar()
        self.t.set("00:00:00")
        self.timeLabel = Label(self.MainMidWindow,textvariable=self.t, bg = 'black', fg = 'white') 
        self.timeLabel.config(font=("Courier 20 bold"))                              
        self.bt1 = Button(self.MainMidWindow,text="", width = 5, command=self.startB, font=("Courier 12 bold"), bg = 'black',fg = 'white', bd=0)
        self.bt1.place(x=780,y=0)
        self.timeLabel.place(x=550,y=25)
        
        #Sensor simulator
        #Create a spinbox with activation button to simulate different temperatures
        self.spin = StringVar()
        self.spinBox = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
        self.spinBox.place(x=200,y=100)
        
        self.sensorButton = Button(self.MainMidWindow, text = 'Load', command = self.useSensor, bg = 'snow', height = 1)
        self.sensorButton.place(x=200, y=150)
        
#        self.sensorData = Label(self.MainMidWindow, padx =10 , textvariable=self.spin, bg = 'black', fg = 'white')
#        self.sensorData.config(font=("Courier 20 bold"))
#        self.sensorData.place(x=360,y=340)

    #
    def useSensor(self):
        self.spin = float(self.spinBox.get()) #Get the value of the spinbox and save it as a float
        #If the temperature is under half of its max temperature display the color from blue to white
        #Temperature value has to be between 0 and 255 and a whole number otherwise the color of the label won't work
        if (float(self.spin) < 90): 
#            self.temperature.set(str(self.spinBox.get()))
            self.temperature.set(str(self.spinBox.get())+" C"+degree_sign)
            self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (75+int(round(self.spin*2)), 75+int(round(self.spin*2)), 255))
            self.tempLabel.place(x=380,y=340)

        #If the temperature is over half of its max temperature display the color from white to red
        #Temperature value has to be between 0 and 255 and a whole number otherwise the color of the label won't work
        else:
            self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (255, 255+180-int(round(self.spin)*2), 255+180-int(round(self.spin)*2)))
            self.tempLabel.place(x=210,y=340)
            self.temperature.set(" Warning "+ str(self.spin) +" C"+degree_sign)
        

    #Animated Polygon, Animated Polygon currently not updating        
    def delete_Poly(self):
#        mydebug(f"WinMid.delete_Poly()")
        if self.pol > 0: # avoid list of arrows now for simplicity
            self.MainMidWindow.delete(self.pol)
            self.pol = 0
    
    def delete_rect(self):
        if len(self.rect)  > 0: # avoid list of rects now for simplicity
            for i in self.rect:
                self.MainMidWindow.delete(i)
            self.rect = []

    def delete_text(self):
        if len(self.text) > 0:
            for i in self.text:
                self.MainMidWindow.delete(i)
            self.text = []

########## timer functions
    #Check if it is the first time the button is pressed so there are no errors
    def startB(self):
        global countcheck
        countcheck = countcheck + 1
        if (countcheck == 1):
            self.timer()
            
    #Check if it is the first time the button is pressed so there are no errors
    def start(self,event):
        global countcheck
        countcheck = countcheck + 1
        if (countcheck == 1):
            self.timer()
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
                    self.MainMidWindow.after(960,self.timer)

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
    
    
    def Update_val(self, num):
#        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle}")
        if(num == 0):
            if(self.angle != 200):
                self.angle += self.arrow_dir # .. was 1 (too small to see something)
        if(num == 1):
            if(self.angle != -20):
                self.angle -= self.arrow_dir # .. was 1 (too small to see something)

        if(self.angle > 200 or self.angle <-20 ):
            self.arrow_dir = -self.arrow_dir

        # delete old arrow, delete Old Rectngles, delete old line and old text
        self.delete_Poly()                
        self.delete_rect()
        self.delete_text()
        if(self.line != 0):
            self.MainMidWindow.delete(self.line)
        
        self.MainMidWindow.delete("all")    
        self.TempMainMidWindow.delete("all")

        #make the text for the break bar (red bar)
            
        self.text.append(self.MainMidWindow.create_text(90, 305, text =  '{} {}'.format(int(((220-self.angle-20)/220)*100), "%") , font=("Purisan", 20), fill="snow"))
        #make text for the rpm meter (middle moving arrow)
        self.text.append(self.MainMidWindow.create_text(420, 305, text = '{} {}'.format(int(((self.angle+20)/220)*4000), "rpm"), font=("Purisan", 20), fill="snow")) 
        #make text for gas meter(green bar)
        self.text.append(self.MainMidWindow.create_text(750, 305, text = '{} {}'.format(int(((self.angle+20)/220)*100),"%"), font=("Purisan", 20), fill="snow"))
        
        
        
        #update rectangles
        self.rect.append(self.MainMidWindow.create_rectangle(40, 250, 140, 250-((220-self.angle-20)/220)*200, fill='red3'))
#       self.my_rectangle = self.round_rectangle(40, 250-((220-self.angle-20)/220)*200, 140, 250 , radius=20, fill="red3")

        self.rect.append(self.MainMidWindow.create_rectangle(700, 250, 800, 250-((self.angle+20)/220)*200, fill='green2'))       

        self.make_speedmeter(self.coord)

        # draw new arrow
        self.pol = self.MainMidWindow.create_polygon(
            [      [ self.centerx + self.L_E  * self.size * math.cos(math.radians(self.angle))  *0 ,  self.centery + self.L_E * self.size * math.sin(math.radians(self.angle)) *0 + 25 ], #bottom put to 0 to make it an arrow
                   [ self.centerx + self.L_S  * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.L_S * self.size*  math.sin(math.radians(self.angle + 90)) + 25 ],
                   [ self.centerx + self.L_W  * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.L_W * self.size * math.sin(math.radians(self.angle + 180)) + 25 ] ,  
                   [ self.centerx + self.L_N *  self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.L_N  * self.size * math.sin(math.radians(self.angle + 270)) + 25 ]
            ] , fill='red'        ) 
        
        #create line to display how far the steering wheel is turned    
        self.line = self.MainMidWindow.create_line( 770 * math.cos(math.radians(self.angle)), 50 , 770 * math.cos(math.radians(self.angle)), 100 , 771 * math.cos(math.radians(self.angle)), 50 , 771 * math.cos(math.radians(self.angle)), 100 )
        
        #update the color in the box under the rpm meter based on the angle of the rpm meter 
        self.temp = self.text.append(self.TempMainMidWindow.create_text(75,37.5, text = '{}'.format(int(self.angle+20)), font=("Purisan", 20), fill="black"))
        self.del_temp()
        self.temp_gradient(self.angle)
        
#        if (self.angle < 90):
#            self.temperature.set(str(self.angle+20)+" C"+degree_sign)
#            self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (75+self.angle*2, 75+self.angle*2, 255))
#            self.tempLabel.place(x=380,y=340)
#
#            
#        else:
#            
#            self.tempLabel.config(font=("Courier 30 bold"   ),bg='#%02x%02x%02x' % (255, 255+180-self.angle*2, 255+180-self.angle*2))
#            self.tempLabel.place(x=210,y=340)
#            self.temperature.set(" Warning "+str(self.angle+20)+" C"+degree_sign)
            
             
## Functions to display speed meter           
    def calc_point(self,angle, width, height):
        return (width * math.cos((- 90 + angle) * math.pi / 180),
                height * math.sin((- 90 + angle) * math.pi / 180))
    def offset_point(self,base, offset):
        """ apply offset onto a base point
        base    a tuple or list -> (x, y)
        offset  a tuple or list -> (offset-x, offset-y)
        """
        return (base[0] + offset[0], base[1] + offset[1])
                
    def draw_tick(self,canvas, center, w, h, angle, r1, r2, width, color):
        p1 = self.calc_point(angle, w / 2 * r1, h / 2 * r1)
        p2 = self.calc_point(angle, w / 2 * r2, h / 2 * r2)
        p1 = self.offset_point(center, p1)
        p2 = self.offset_point(center, p2)
        canvas.create_line(p1 + p2, width = width, fill = color)
    
    def make_speedmeter(self, coord):
        width, height = abs(coord[0] - coord[2]), abs(coord[1] - coord[3])
        center = (coord[0] + coord[2]) // 2, (coord[1] + coord[3]) // 2
        self.MainMidWindow.create_arc(coord, start = -30, extent = 240, fill = "black", outline = "")
        for i in range(-108, 109, 6):
            w = 3 if i % 36 == 0 else 1
            self.draw_tick(self.MainMidWindow, center, width, height, i, 0.88, 0.97, w, 'gray')
            
        zero = self.MainMidWindow.create_text(315,275, fill="white", font="times 18", text= "0")
        twenty = self.MainMidWindow.create_text(320,205, fill="white", font="times 18", text= "20")
        fourty =self.MainMidWindow.create_text(360,150, fill="white", font="times 18", text= "40")
        sixty = self.MainMidWindow.create_text(420,130, fill="white", font="times 18", text= "60")
        eighty = self.MainMidWindow.create_text(480,150, fill="white", font="times 18", text= "80")
        hundred = self.MainMidWindow.create_text(515,205, fill="white", font="times 18", text= "100")
        hundredtwenty = self.MainMidWindow.create_text(515,275, fill="white", font="times 18", text= "120")        
##


    #delete temperature text function in the top middle window
    def del_temp(self):
        if(self.text_temp > 0):
            self.TempMainMidWindow.delete(self.text_temp)
            self.text_temp = 0
    # function to update the color in the box under the rpm meter based on the angle of the rpm meter
    def temp_gradient(self, num):
#        self.temp += self.temp_dir # .. was 1 (too small to see something)
        
        if(num >= 250 or num <=0 ):
            self.temp_dir = -self.temp_dir

        self.del_temp()   
        self.colorize(255, 220-num, 0)
#        mydebug(f"WinMid.temp_gradient() self.temp_gradient={self.angle}")
#        self.TempMainMidWindow.configure(bg = self.color)
#        self.tempLabel.config(bg = self.color)             
        self.text_temp = self.TempMainMidWindow.create_text(420,240, text = int(num/250*60) , fill="black", font = ("Purisa", 30))
  
    #function to adjust color
    def colorize(self,a,b,c):
        self.color = '#%02x%02x%02x' % (a, b, c)
#        print(self.color, b)
   