# Code user interface made in quarter two 


## Getting Started

The main program is Main_File_FC. Main_File_FC will create a window that displays current driving speed, cooling fluid temperature, accelerator pedal position, brake pedal position, steering wheel position and cooling fluid flow speed. Main_File_FC uses the classes MainMidWindow and BotMidWindow from MainMidWindow.py and BotMidWindow.py. The files found in the folder Test_code_smaller_parts are files used to test and understand certain parts in Main_File_FC.

### Prerequisites

You will need the display made by the formula cruisers, a Raspberry Pi (RPi) and a Python Integrated Development Environment (IDE). If you want to test your code without working on the Raspberry Pi, you will have to download an IDE onto your computer for example spyder, PyCharm or Atom. Otherwise use the python IDE on the Raspberry Pi.


### Installing

The IDE that was used to test out the written code was Spyder. Information about installation and how to use it can be found on their website [(Spyder)](https://www.spyder-ide.org/).

## Running tests

In the folder Test_code_smaller_parts, four files can be found that each were used to test a different part of the main code.
To run these files or your own tests, upload the code to the Raspberry Pi by copy + paste or by using a USB and run the code from the command prompt or a python shell.

* Saving data onto Excel

The file FCexcelTest shows a small example of storing data into an excel file from python. The Excel document will have two columns named "Operator" and "Number". Everytime the file is run the excel file should get the numbers 1-5 added to the first column and one extra 23 in the second column.

```from tkinter import *
import pandas as pd

def submit_fields():
    path = 'FCtest.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Operator']
    SeriesB = df1['Number']
    A = pd.Series(entry1)
    B = pd.Series(entry2)
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    df2 = pd.DataFrame({"Operator":SeriesA, "Number":SeriesB})
    df2.to_excel(path, index=False)

master = Tk()

Label(master, text="Operator").grid(row=0)
Label(master, text="Number").grid(row=1)
i = 0
entry2 = 23 

while i < 5:
    i = i+1    
    entry1 = i 
    submit_fields()


mainloop()
```
</br>

* Saving data onto USB

The file PythonWriteUSB shows a small example of saving data into a file on a USB. The file has to already exist and should be saved as a ".csv" (comma-seperated values) file. The code below will save data into 6 columns and the number of rows will be equal to the data that was already in the file with an adition of ten rows. The first column will have the title "time" and the others have "sensor (1-5)".

```
import os
import time 
from time import sleep
from datetime import datetime

file = open("E:/test2.csv", "a")
i=0
if os.stat("E:/test2.csv").st_size == 0:
        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
while True:
    i=i+1
    now = datetime.now()
    file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n")
    file.flush()
    time.sleep(1)
    if (i>=10):
        break
file.close()
```

* Making a speed meter

The file clock_test is code taken from an example someone else made [(Clock Code)](https://gist.github.com/Inndy/c2580aa5f5016755d076). The code to make a clock has been used to create a speed display. The code below wil make a circle arc from -30 degrees up to 210 degrees (start = -30, extent = 240). with the for loop "for i in range(-108, 109, 6):" a thin line is created every 6 degrees and a thick line is created every 36 degrees.

```
import time
import math
from tkinter import *

root = Tk()
root.title("Painter")


canvas = Canvas(root, width = 400, height = 300, bg = "#eeeeee")
canvas.grid(row = 2, column = 0, columnspan = 2)

coord = 10, 10, 290, 290

coord2 = 10, 10, 10, 290
coord3 = 290, 290, 10, 290
coord1 = 10, 10, 100, 100

def now():
    time_now = time.localtime()
    return time_now.tm_hour, time_now.tm_min, time_now.tm_sec

def center_rectangle(center, w, h):

    return (center[0] - w / 2, center[1] - h / 2,
            center[0] + w / 2, center[1] + h / 2)

def calc_point(angle, width, height):
    return (width * math.cos((- 90 + angle) * math.pi / 180),
            height * math.sin((- 90 + angle) * math.pi / 180))

def offset_point(base, offset):

    return (base[0] + offset[0], base[1] + offset[1])

def draw_tick(canvas, center, w, h, angle, r1, r2, width, color):
    p1 = calc_point(angle, w / 2 * r1, h / 2 * r1)
    p2 = calc_point(angle, w / 2 * r2, h / 2 * r2)
    p1 = offset_point(center, p1)
    p2 = offset_point(center, p2)
    canvas.create_line(p1 + p2, width = width, fill = color)

def draw_pointer(canvas, center, w, h, angle, rate, width, color):
    offset_x, offset_y = calc_point(angle, w / 2 * rate, h / 2 * rate)
    point = offset_point(center, (offset_x, offset_y))
    
    canvas.create_line(center + point, width = width, fill = color)

def draw_clock(canvas, coord, time):
    h, m, s = time
    h %= 12
    width, height = abs(coord[0] - coord[2]), abs(coord[1] - coord[3])
    center = (coord[0] + coord[2]) // 2, (coord[1] + coord[3]) // 2
    canvas.create_arc(coord, start = -30, extent = 240, fill = "black", outline = "")

    for i in range(-108, 109, 6):
        w = 3 if i % 36 == 0 else 1
        draw_tick(canvas, center, width, height, i, 0.88, 0.97, w, 'gray')
    canvas.create_text(43,185, fill="white", font="times 18", text= "0")
    canvas.create_text(50,115, fill="white", font="times 18", text= "20")
    canvas.create_text(90,60, fill="white", font="times 18", text= "40")
    canvas.create_text(150,40, fill="white", font="times 18", text= "60")
    canvas.create_text(210,60, fill="white", font="times 18", text= "80")
    canvas.create_text(245,115, fill="white", font="times 18", text= "100")
    canvas.create_text(245,185, fill="white", font="times 18", text= "120")


c2 = Canvas(root, width = 300, height = 300, bg = "#eeeeee")
c2.grid(row = 3, column = 0, columnspan = 2)

def update_clock():
    coord = 10, 10, 290, 290
    c2.delete(ALL)
    draw_clock(c2, coord, now())
    root.after(1000, update_clock)

update_clock()
root.mainloop()
```

* SPI communication with C3

The file SPI communication FC is adjusted code from this [SPI tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all). This code will send information to the C3 and then it will ask for a return message. The sent message is "msg" and the returned value is stored in "result".

```
import time
import spidev

bus = 0

device = 1

spi = spidev.SpiDev()

spi.open(bus, device)

spi.max_speed_hz = 250000
spi.mode = 0

msg = 2
result = spi.xfer2(msg)
print(result)
time.sleep(5)

spi.close()
```

## Main code

Some of the functions found throughout the different files have two funtions that do the same with a slightly different name. However one of them only takes "self" as an argument and the other also takes "event" as an argument. This is because they can be activated using a physical button and a button on screen. Physical buttons come with an extra parameter (event). This is why for tsting purposes a seperate function has been made. For example MainMidWindow has start and startB. If any code is unclear, further explanation can usually be found in the comments in the file itself.

* Main_File_FC

First of all, a SPI connection is made and a connection to a specific bus and device is defined.
```
bus = 0
device = 1
spi = spidev.SpiDev()

spi.open(bus, device)

```
Then the mode and clockspeed are set.
```
spi.max_speed_hz = 250000
spi.mode = 0

```
To send and receive data one line of code is used. The received variable(s) are stored in "result" and the transvered variable towards the C3 microcontroller is "msg". The function to send and receive is spi.xfer2. For different functions "spidev opions" can be looked up [(online)](http://tightdev.net/SpiDev_Doc.pdf).
```
sensorData = spi.xfer2(msg)

```
As soon as the data has been collected from the C3, it is then stored onto a USB. The data is stored into a .csv file so all different sensor data can easily be distinguished from each other by commas. First, the file that will contain the data, has to be opened. After this is done, the file is checked if it is empty or not. If it is empty it will fill the first row with the text in the brackets of "file.write". Each word that is after a comma is put into a seperate column. Once this has been completed, the current time is put into the variable "now". The time wil always be put into the first column and then the sensor data will be put behind it. This is so strange sensor values can more easily be coupled to where and when it happened.
```
file = open("E:/test2.csv", "a")
if os.stat("E:/test2.csv").st_size == 0:
        file.write("Time,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
now = datetime.now()
file.write(str(now)+","+str(i)+","+str(-i)+","+str(i-10)+","+str(i+5)+","+str(i*i)+"\n")
file.flush()
file.close()  

```

To be able to make a graphical user interface that contains objects, a window has to be made. This is what happens in the main file with the use of Tkinter. 
```
master = Tk()

```

The main file defines how big the user interface window will be.
```
winsize = str(windowX) + 'x' + str(windowY) + '+-10+0'

master.geometry(winsize)
```
It then calls a function "display" from the class "Layout" after 100 miliseconds and loops this till the main window is closed. This function activates everything within BotMidWindow and MainMidWindow. With the function .after, a function is called after a certain amount of miliseconds. 

```
Lay = bw.Layout(result, master) #Lay becomes an object of the class "Layout" from the document "BotMidWindow.py"
master.after(100, Lay.display) #Call the function "display" from class "Layout" after 100 miliseconds
master.mainloop() #Loop forever
```

* MainMidWindow

MainMidWindow contains the software for the top part of the window. The top part of the screen is used to display the most important information and the most urgent messages. It displays the current speed, the cooling fluid temperature, the time that has passed, how much battery energy is left and the gas/brake paddle positions. A timer is displayed so the driver knows how much time has passed since the race started. This combined with the battery energy level and the temperature level will tell if the driver is asking too much from the car or not.

In "def __init__" all the variables are defined and the buttons, labels and boxes are created.
To place objects in the window, a canvas has to be made and placed in the window. This is done using the code below. The canvas function has a lot of different parameters. The first field is the window the canvas is created in, then the size, border and background are defined.  
```
self.MainMidWindow = Canvas(self.window, width= 840, height=420, borderwidth = 0.0, highlightthickness=0, bg='black' ) 
self.MainMidWindow.pack(fill = BOTH, expand = 1)
```

Labels are created to display the time and the temperature. The parameters used are what window the label is placed into, x offset, variable that will be shown in the label, background and foreground. With the following code a label is created, setup and placed at a relative point on the screen:
```
self.battery = StringVar()
self.batteryLabel = Label(self.MainMidWindow, textvariable=self.battery, bg = 'red', fg = 'black')
self.batteryLabel.config(font=("Courier 20 bold"))
self.batteryLabel.place(relx=0.05, rely=0.07)
```

Function Update_val is the main function that is called. This function updates all the values in the canvas. First of all it checks what the window's width and height are so the whole screen can be scaled if needed (for example going from a 7 inch screen to a 5 inch screen).
```
WindowY = self.window.winfo_height()
WindowX = self.window.winfo_width()
```

After that is done it it removes all objects so it has fresh room to place updated objects on.
```
self.MainMidWindow.delete("all")    
```

It then places a text under the speed meter to display how fast the car is going.
```
self.text.append(self.MainMidWindow.create_text(WindowX/2, WindowY/1.5, text =  '{} {}'.format(int(result[3]), "km/h") , font=("Purisan", 20), fill="snow"))
```

To display the how full the battery still is, a battery icon has been made in the top left of the screen. The inside color of the battery has four stages. The percentage is constantly updated but the color will be "red" for 0-25% battery, "dark orange" for 25-50%, "gold" for 50-75% and "green3" for 75-100%. Changing the % value shown is done in the first line below and the if statements are for each of the different colors.

```
self.my_rectangle = self.round_rectangle(WindowX/(840/35), WindowY/(840/40), WindowX/(840/255), WindowY/(840/115), radius=20, fill="white")
self.my_rectangle = self.round_rectangle(WindowX/(840/190), WindowY/(840/52), WindowX/(840/265), WindowY/(840/103), radius=20, fill="white")

self.battery.set(str(int(self.sensorData[2])) + "%")
if(int(self.sensorData[2])>75 and int(self.sensorData[2])<=100):    
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
```

The speed and temperatur displays have to be created. This is done using the clock code that can be found under the header "running tests" shown at the start of this document. In the Update_val function it calls the functions tested in the clock code. 
```
self.speedMeter = self.make_speedmeter([WindowX/(840/200), WindowY/(840/190), WindowX/(840/650), WindowY/(840/650)])    
self.tempMeter = self.make_speedmeter([WindowX/(840/20), WindowY/(840/200), WindowX/(840/250), WindowY/(840/450)], -120, 71, 5, 70)

```

After the speed and temperature displays have been created, the arrows pointing towards the speed and temperature have to be made and updated. This can only be done after the speed and temperature displays have been made otherwise the arrows will be behind the displays and cannot be seen anymore. This is done using:

```

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
 
```

The lenth and width of the arrow is determined in the initialisation of the class "def init(self, window)" with: 

```
self.L_N = 0.2
self.L_E = 3
self.L_S = 0.2
self.L_W = 4
```

When the temperature is above a certain value an image to show that the temperature is too high shows.

```
(code in def __init__)
heat_img = Image.open("Heat_Symbol.jpg")
heat_img = heat_img.resize((75, 75), Image.ANTIALIAS)
self.image = ImageTk.PhotoImage(heat_img)

(codee in Update_val)
if (float(self.sensorData[4]) >= 50): 
self.tempImg.place(relx = 0.11, rely = 0.4)            
```

To check if the button that starts the timer has already been pressed before, a start function has been made. 
```
def startB(self,event):
        global countcheck
        countcheck = countcheck + 1
        global count
        count = 0
        if (countcheck == 1):
            self.timer()
```

After the button check is done, the timer has to be started and updated every second. Self.MainMidWindow.after(960,self.timer). This calls the same function after 1000 miliseconds. Depending on how fast or slow your whole program runs, you will have to adjust the 1000 miliseconds part of this last statement to change the time after which it recalls the function.

```
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
                    self.MainMidWindow.after(1000,self.timer)
```
To reset the timer the function reset has been made.
```
def resetB(self):
        global countcheck
        if (countcheck >= 1):
            global count
            countcheck = 0
            count = 1
            self.t.set('00:00:00')
```

Function round_rectangle is used to make rounded rectangles. Currently it is only being used in the battery but it could be used to make  other objects more visually pleasing too.
```
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
```
The last part of the code are the functions for the creation of the timer. More information can be found under running tests and the test file.


* BotMidWindow

BotMidWindow contains the software for the bottom half of the screen. This part of the screen is used for testing and preperation. It also contains the class Layout. This class is used to connnect all other classes and display everything. Class Layout also controls the buttons at the side of the window. BotMidWindow mostly has functions that look much like the functions in MainMidWindow. It has one function that is very different and that is funciton_choose. This function selects what to do when a button on the side of the screen is pressed (choice 1-7 for 7 buttons).

```
def function_choose(self):        
    self.update_val()
    self.color_update()
        
    if(self.choice != self.old_choice):
        self.screen_clear()
        self.old_choice = self.choice
       
    if self.BotCanvas == 0:
        self.screen_clear()

    if(self.choice != self.old_choice):
        self.screen_clear()
        self.old_choice = self.choice

    if(self.choice == 1): 
        self.screen_clear() 
        self.rotate_Poly()  
                  
    elif(self.choice == 2): 
        self.screen_clear() 
        self.rect = self.BotCanvas.create_rectangle(100, 100, 200, 200, fill='red')
    
    elif(self.choice == 3):
        self.screen_clear()
        self.rect = self.BotCanvas.create_rectangle(200, 200, 200 + (self.angle//10)%1000 , 300, fill='blue')
   
    elif(self.choice == 4): 
        self.screen_clear() 
        self.rect = self.BotCanvas.create_rectangle(300, 300, 400, 400, fill=self.color)

    elif(self.choice == 5):
        self.screen_clear() 
        self.rect = self.BotCanvas.create_rectangle(200, 200, 200 + (self.angle//10)%1000 , 300, fill=self.color)

    elif(self.choice == 6): 
        self.screen_clear() 
        self.temp_gradient()

    elif(self.choice == 7): 
        self.screen_clear() 
```
Funtion update_val is usd to update the values of the gas/brake paddle bars.
```
def update_val(self):
    WindowY = self.window.winfo_height()
    WindowX = self.window.winfo_width()

    self.BotCanvas.delete("all")

    self.BotCanvas.create_text(WindowX/3.5, WindowY/2, text =  '{} {}'.format(int(self.result[0]), "%") , font=("Purisan", 20), fill="snow")
    self.BotCanvas.create_text(WindowX/3.5, WindowY/4, text = '{} {}'.format(int(self.result[1]), "%"), font=("Purisan", 20), fill="snow") 
    self.BotCanvas.create_rectangle(WindowX/2.5, WindowY/6, WindowX/2.5+self.result[0], WindowY/3, fill='red3')
    self.BotCanvas.create_rectangle(WindowX/2.5, WindowY/2.5, WindowX/2.5+self.result[1], WindowY/1.75, fill='green2')

    self.angle += 1
    self.color_update()
    
```
Class Layout binds all the buttons to the right functions.
```
self.master.bind('1', self.left1b_)
self.master.bind('2', self.left2b_) #bind button "2" to function left2b_
self.master.bind('3', self.left3b_) #bind button "3" to function left3b_
self.master.bind('4', self.right1b_) #bind button "4" to function right1b_ 
self.master.bind('5', self.right2b_) #bind button "5" to function right2b_
self.master.bind('6', self.right3b_) #bind button "6" to function right3b_
self.master.bind('7', self.right4b_) #bind button "7" to function right4b_
self.master.bind('a', self.accelerate) #bind button "a" to function accelerate
self.master.bind('d', self.decelerate) #bind button "d" to function decelerate
self.master.bind('t', self.MainMidWindow.start)
```
Fuction display places all the buttons created in layout onto the window and then calls function screen_Updater.
```
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
```
The function screen_Updater checks if any of the buttons was pressed and calls function update_val from the MainMidWindow, to update all the values on the main window.
```
        
def screen_Updater(self):
    self.BotMidWindow.function_choose()
    self.MainMidWindow.Update_val(3) #Make sure gas and brake simulation is not affected.
    self.master.after(10, self.screen_Updater)

```

Under screen_Updater are the functions that all the buttons refer to. Each of these functions changes what value funtion_choose gets.
```
def left1_(self):
    self.BotMidWindow.choice = 1 #if this left1_ function is called set choice in function_choose to be 1    
```

## Previous versions
The previous versions can still be found in the commented lines. Updates to previous iterations consist of changing the look of the temperature display, replacing input boxes with an array that contains all the sensor values and making the screen scalable.

## Possible changes for next iterations

Currently all objects on the screen are removed. To increase the frames per second only the changing objects on the screen have to be removed or replaced. The bottom part of the screen is currently being used for test data. This can be changed so that the buttons display the test data in a pop-up window. When the test data has been seen the window can be closed and the main screen will be fully on the screen again. Currently the file is not started automatically. This has to be changed to automatic startup on boot.

## Deployment
This code can be copied/downloaded onto your own computer and then run from your Python IDE.

Testing this code on a Raspberry Pi can be done by copying the code onto a USB and then be putting it onto a Raspberry Pi. Make sure Main_File_FC, MainMidWindow and BotMidWindow are in the same directory, otherwise Main_File_FC cannot use the classes in MainMidWindow and BotMidWindow.

## Built With
* [Raspberry Pi](https://www.raspberrypi.org/) - The used controller
* [Spyder](https://www.spyder-ide.org/) - The used IDE

## Contributing

If any changes need to be made, please first make a copy and then change what needs to be changed in there (fork the document/folder).
Please read [CONTRIBUTING.md](https://github.com/KevinEwoudLee/HU3-UI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Authors

* **Luigi Dania** - Version 1 developer(Q1) - [Luigi_Dania](https://betafactory.atlassian.net/wiki/people/5d6cf3deb605d80dc0149265)
* **Kevin Lee** - Version 2 developer (Q2) - [Kevin_Lee](https://betafactory.atlassian.net/wiki/spaces/~959975090/overview)

## Usefull links

In addition to the comments in the software code itself here are some and useful videos and web tutorials:
* Tkinter was used to make the GUI. Information about Tkinter: 

https://core-electronics.com.au/tutorials/raspberry-pi-workshop-for-beginners.html#ch5

https://effbot.org/tkinterbook/pack.htm

https://codereview.stackexchange.com/questions/191477/binding-a-keyboard-key-to-a-tkinter-button

* For saving information in Excel: 

https://www.youtube.com/watch?v=w36yng8BTUU

 * Writing data to USB:

http://cms.digi.com/resources/documentation/digidocs/90001537/references/r_how_to_use_usb_flash_drive.htm?TocPath=Digi%20Hardware%20Access%7C_____14

* SPI communication:

https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
