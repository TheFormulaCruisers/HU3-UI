# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:44:55 2019

@author: kevin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:34:48 2019

@author: kevin
"""

from tkinter import *
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
#    entry1.delete(0, END)
#    entry2.delete(0, END)

master = Tk()

Label(master, text="Operator").grid(row=0)
Label(master, text="Number").grid(row=1)
i = 0
entry2 = 23 #Entry(master)

while i < 5:
    i = i+1    
    entry1 = i #Entry(master)
    submit_fields()


#entry1.grid(row=0, column=1)
#entry2.grid(row=1, column=1)


#Button(master, text='Quit', command=master.quit).grid(row=3,column=0, pady=4)
#Button(master, text='Submit', command=submit_fields).grid(row=3,column=1, pady=4)

mainloop()