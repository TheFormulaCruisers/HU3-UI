# Code user interface made in quarter two 


## Getting Started

The main program is Main_File_FC. Main_File_FC will create a window that displays current driving speed, cooling fluid temperature, accelerator paddle position, brake paddle position, steering wheel position and cooling fluid flow speed. Main_File_FC uses the classes MainMidWindow and BotMidWindow from MainMidWindow.py and BotMidWindow.py. The files found in Test_code_smaller_parts are software used to test and understand certain parts in Main_File_FC.

### Prerequisites

You will need the display made by the formula cruisers, a Raspberry Pi and a python development environment if you want to test your code without working on the Raspberry Pi for example spyder, PyCharm or Atom. Otherwise use the python IDE on the Raspberry Pi.


### Installing

The IDE at was used to test out the written code was Spyder. Information about installation and how to use it can be found on their website [(Spyder)](https://www.spyder-ide.org/).

## Running tests

In the folder Test_code_smaller_parts, four files can be found that each were used to test a different part of the main code.
To run these files or your own tests, upload the code to the Raspberry Pi using a USB and run the code using an IDE.

* Saving data onto Excel

FCexcelTest shows a small example of storing data onto an excel file from python. The Excel document will have two columns named "Operator" and "Number". Everytime the file is run the excel file should get the numbers 1-5 added to the first column and an extra 23 in the second column.

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

PythonWriteUSB shows a small example of saving data into an excel file on a USB. The excel file has to already exist and should be saved as a .csv (comma-seperated values) file. The code below will save data into 6 columns and the number of rows will be equal to the data that was already in the file with an adition of ten rows. The first column will have the title "time" and the others have "sensor (1-5)".

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

* Making a decently looking speed meter

Clock_test is code taken from an example someone else made [(Clock Code)](https://gist.github.com/Inndy/c2580aa5f5016755d076). The code to make a clock has been used to create a speed display. The code below wil make a circle arc from -30 degrees up to 210 degrees (start = -30, extent = 240). with the "for i in range(-108, 109, 6):" loop a line is created every 6 degrees and a thick line every 36 degrees.

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
## Main code

Some of the functions found throughout the different files have two funtions that do the same. This is because they can be activated using a physical button and a button on screen. Physical buttons come with an extra parameter (event). This is why a seperate function has to be made. For example MainMidWindow has start and startB. If any code is unclear, further explanation can always be found in the comments in the file itself.

* Main_File_FC

To be able to make a graphical user interface that contains objects, a window has to be made. This is what happens in the main file using Tkinter.
The main file defines how big the user interface will be, then calls a function from one of the classes and loops this forever.


* MainMidWindow

MainMidWindow contains the software for the top half of the window. The top half of the screen is used to display the most important information and the most urgent messages. It displays the current speed, the cooling fluid temperature, the time that has passed, how much battery energy is left and the gas/brake paddle positions. A timer is displayed so the driver knows how much time has passed since the race started. This combined with the batteries energy level and the temperature level will tell if the driver is asking too much from the car or not.

To place objects in the window, a canvas has to be made and placed in the window. This is done using:
```
self.MainMidWindow = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg='black', highlightthickness=0) 
self.MainMidWindow.pack_propagate(0)
```

Labels are created to display the time and the temperature. With the following code a label is created, setup and placed:
```
self.tempLabel = Label(self.MainMidWindow, padx =10 , textvariable=self.temperature, bg = 'black', fg = 'black')
self.tempLabel.config(font=("Courier 20 bold"))
self.tempLabel.place(x=380,y=340)
```

To check if the button that starts the timer has already been pressed before, a start function has been made. 
```
def start(self,event):
    global countcheck
    countcheck = countcheck + 1
    if (countcheck == 1):
        self.timer()
```

After the button check is done, the timer has to be started and updated every second. Self.MainMidWindow.after(960,self.timer). This calls the same function after 960 miliseconds. Depending on how fast or slow your whole program runs, you have to change the 960 part of this last statement to change the time after which it recalls the function.

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
                self.MainMidWindow.after(960,self.timer)
```

Function round_rectangle is used to make rounded rectangles. Currently it is not being used but it could be used to make objects more visually pleasing.

Function Update_val is the main function that is called. This function updates all the values in the canvas. First of all it checks if "gas" (if(num == 0):) or "brake" (if(num == 1):) is pressed and updates the angle (self.angle) and arrow direction (self.arrow_dir) accordingly. 
```
if(num == 0):
    if(self.angle != 200):
        self.angle += self.arrow_dir # .. was 1 (too small to see something)
if(num == 1):
    if(self.angle != -20):
        self.angle -= self.arrow_dir # .. was 1 (too small to see something)

if(self.angle > 200 or self.angle <-20 ):
    self.arrow_dir = -self.arrow_dir
```

After that is done it it removes all objects that have a chance on changing on the canvas so it is fresh to place updated objects onto it. This is done using the delete_(name) functions toghether with functions that come ready with Tkinter.
```
self.delete_Poly()                
self.delete_rect()
self.delete_text()
if(self.line != 0):
    self.MainMidWindow.delete(self.line)
self.MainMidWindow.delete("all")    
self.TempMainMidWindow.delete("all")
```

Then it calculates how full the gas/brake bars have to be, takes that value and makes that into a text and updates how full the gas/brake bars have to be.
```
self.text.append(self.MainMidWindow.create_text(90, 305, text =  '{} {}'.format(int(((220-self.angle-20)/220)*100), "%") , font=("Purisan", 20), fill="snow"))
self.text.append(self.MainMidWindow.create_text(420, 305, text = '{} {}'.format(int(((self.angle+20)/220)*4000), "rpm"), font=("Purisan", 20), fill="snow")) 
self.text.append(self.MainMidWindow.create_text(750, 305, text = '{} {}'.format(int(((self.angle+20)/220)*100),"%"), font=("Purisan", 20), fill="snow"))

self.rect.append(self.MainMidWindow.create_rectangle(40, 250, 140, 250-((220-self.angle-20)/220)*200, fill='red3'))
self.rect.append(self.MainMidWindow.create_rectangle(700, 250, 800, 250-((self.angle+20)/220)*200, fill='green2'))  
```
The speed display has to be created. This is done using the clock code that can be found under the header "running tests" shown at the start of the document. In the Update_val function it simple calls the functions tested in the clock code. 
```
self.make_speedmeter(self.coord)
```

After the speed display has been created, the arrow pointing towards the speed has to be updated and made. This can only be done after the speed display has been made otherwise the arrow will be behind the speed display and cannot be seen anymore. This is done using:

```
self.pol = self.MainMidWindow.create_polygon(
    [      [ self.centerx + self.L_E  * self.size * math.cos(math.radians(self.angle))  *0 ,  self.centery + self.L_E * self.size * math.sin(math.radians(self.angle)) *0 + 25 ], #bottom put to 0 to make it an arrow
           [ self.centerx + self.L_S  * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.L_S * self.size*  math.sin(math.radians(self.angle + 90)) + 25 ],
           [ self.centerx + self.L_W  * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.L_W * self.size * math.sin(math.radians(self.angle + 180)) + 25 ] ,  
           [ self.centerx + self.L_N *  self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.L_N  * self.size * math.sin(math.radians(self.angle + 270)) + 25 ]
    ] , fill='red'        ) 
```

The lenth and width of the arrow is determined in the initialisation of the class (def init(self, window)) with: 

```
self.L_N = 0.1
self.L_E = 3
self.L_S = 0.1
self.L_W = 2.5
```

To simulate sensordata multiple spinboxes with variables to store the number in have been made. Also a submit button is needed to use the filled in number. This can be done with:
```
        self.spinBreak = StringVar()
        self.spinBox = Spinbox(self.MainMidWindow, from_=0, to=180, width = 5, bg = 'snow')
        self.spinBox.place(x=150,y=200)
        
        self.sensorButton = Button(self.MainMidWindow, text = 'Load', command = self.useSensorData, bg = 'snow', height = 1)
        self.sensorButton.place(x=220, y=100)
```
The submit button takes the value that was put into the spinbox and then displays that number and a color to show if that temperature is fine or is too hot. This is done in the function useSensorData and looks like this:
```
        def useSensorData(self):
            self.spinTemp = float(self.spinBox.get())
            if (float(self.spinTemp) < 90): 
                self.temperature.set(str(self.spinBox.get())+" C"+degree_sign)
                self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (75+int(round(self.spinTemp*2)), 75+int(round(self.spinTemp*2)), 255))
                self.tempLabel.place(x=380,y=340)

            else:
                self.tempLabel.config(font=("Courier 30 bold"),bg='#%02x%02x%02x' % (255, 255+180-int(round(self.spinTemp)*2), 255+180-int(round(self.spinTemp)*2)))
                self.tempLabel.place(x=210,y=340)
                self.temperature.set(" Warning "+ str(self.spinTemp) +" C"+degree_sign)
```

* BotMidWindow

BotMidWindow contains the software for the bottom half of the screen. This part of the screen is used for testing and preperation. It also contains the class Layout. This class is used to connnect all other classes and display everything. Class Layout also controls the buttons at the side of the window. The class BotMidWindow currently only shows some tests but no usefull information. This has to be adjusted to sensor values that actually are meaningfull.


## Deployment
This code can be copied/downloaded onto your own computer and then run from your Python IDE.

Testing this code on a Raspberry Pi can be done by copying the code onto a USB and then be putting it onto a Raspberry Pi. Make sure Main_File_FC, MainMidWindow and BotMidWindow are in the same directory, otherwise Main_File_FC cannot use the classes in MainMidWindow and BotMidWindow.

## Built With
* [Raspberry Pi](https://www.raspberrypi.org/) - The controller used
* [Spyder](https://www.spyder-ide.org/) - The IDE used

## Contributing

If any changes need to be made, please first make a copy and change what needs to be changed in there (fork the document/folder).
Please read [CONTRIBUTING.md](https://github.com/KevinEwoudLee/HU3-UI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Luigi Dania** - Version 1 developer(Q1) - [Luigi_Dania](https://betafactory.atlassian.net/wiki/people/5d6cf3deb605d80dc0149265)
* **Kevin Lee** - Version 2 developer (Q2) - [Kevin_Lee](https://betafactory.atlassian.net/wiki/spaces/~959975090/overview)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
