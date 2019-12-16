# Code User Interface made in Quarter two 

Main_file uses MainMidWindow and BotMidWindow. The other files are codes used to understand certain parts in Main_file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

In the folder Test_code_smaller_parts, four files can be found that were each used to test a different part of the main code.
To run these files or your own tests, upload the code to the Raspberry Pi using a USB and run the code using an IDE.

### Break down into end to end tests

* Excel test

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

* Save data onto USB

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

## Deployment

This code can be copied onto a USB and then be put onto a Raspberry Pi. Make sure Main_File_FC, MainMidWindow and BotMidWindow are in the same directory, otherwise Main_File_FC cannot use the classes in MainMidWindow and BotMidWindow.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/KevinEwoudLee/HU3-UI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Luigi Dania** - Version 1 developer(Q1) - [Luigi_Dania](https://betafactory.atlassian.net/wiki/people/5d6cf3deb605d80dc0149265)
* **Kevin Lee** - Version 2 developer (Q2) - [Kevin_Lee](https://betafactory.atlassian.net/wiki/spaces/~959975090/overview)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
