# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:40:00 2019

@author: kevin
"""

data = "Hello"
fh = open("E:/test1", 'a')
fh.write(data)
fh.write("\n")
fh.close()
fh = open("E:/test1", 'r')
print (fh.read())