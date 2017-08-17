#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:09:19 2017

@author: sss
"""

import random, pylab

random.seed(0)

xVals = []
yVals = []
wVals = []

for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
    
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)

xVals = xVals + xVals 
zVals = xVals + yVals
tVals = xVals + yVals + wVals

#pylab.plot(xVals)
#pylab.plot(yVals)
#pylab.plot(tVals)
#pylab.plot(xVals, zVals, '+')
#pylab.plot(xVals, sorted(yVals))
pylab.plot(sorted(xVals), yVals)