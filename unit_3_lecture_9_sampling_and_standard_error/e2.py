#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:10:16 2017

@author: sss
"""

def loadFile():
    inFile = open("julytemps.txt")
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        print(fields)
        if len(fields) != 3 or\
           "Boston" == fields[0] or\
           "Day" == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

"""
           1101011001000101000001
    1001010010101100100010100000100
    """