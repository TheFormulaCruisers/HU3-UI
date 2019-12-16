# Code User Interface made in Quarter two 

Main_file uses MainMidWindow and BotMidWindow. The other files are codes used to understand certain parts in Main_file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need a python development environment if you want to test your code without working on the Raspberry Pi, for example spyder. Otherwise use the python IDE on the Raspberry Pi.


### Installing

To setup your own Raspberry Pi to work properly during your own tests, complete the following steps.

Setting up your Raspberry Pi

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

In the folder Test_code_smaller_parts, three files can be found that were each used to test a different part of the main code.
To run these files or your own tests, upload the code to the Raspberry Pi using a USB and run the code using an IDE.

### Break down into end to end tests

* Saving data onto Excel

FCexcelTest shows a small example of storing data onto an excel file from python. The excel document will have two columns named "Operator" and "Number". Everytime the file is run the excel file should get the numbers 1-5 added to the first column and an extra 23 in the second column.

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

PythonWriteUSB shows a small example of saving data into an excel file on a USB. The excel file has to already exist and should be saved as a .csv (comma-seperated values) file. The code below will save data in 6 columns. The first one will have the title "time" and the others have "sensor (1-5)".

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
    """ return (hour, minute, second) """
    time_now = time.localtime()
    return time_now.tm_hour, time_now.tm_min, time_now.tm_sec

def center_rectangle(center, w, h):
    """ calculate a new rectangle use a center point with width and height
    center  a tuple or list -> (x, y)
    w       width
    h       height
    """
    return (center[0] - w / 2, center[1] - h / 2,
            center[0] + w / 2, center[1] + h / 2)

def calc_point(angle, width, height):
    return (width * math.cos((- 90 + angle) * math.pi / 180),
            height * math.sin((- 90 + angle) * math.pi / 180))

def offset_point(base, offset):
    """ apply offset onto a base point
    base    a tuple or list -> (x, y)
    offset  a tuple or list -> (offset-x, offset-y)
    """
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

    # center -> (x0, y0)
    # point  -> (x1, y1)
    # center + point -> (x0, y0, x1, y1)
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
The main code has the following functions:

Further information can be found in comments in the file itself.

## Deployment

This code can be copied onto a USB and then be put onto a Raspberry Pi. Make sure Main_File_FC, MainMidWindow and BotMidWindow are in the same directory, otherwise Main_File_FC cannot use the classes in MainMidWindow and BotMidWindow.

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
