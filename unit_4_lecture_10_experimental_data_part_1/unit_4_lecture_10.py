#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 23:02:05 2017

@author: sss
"""

import pylab
import random
import numpy

#L1 = [1, 2, 3, 4]
#
#p_array = pylab.array(L1)
#
#L2 = p_array * 9.8

#==============================================================================
# xVals = []
# gausses = []
# for i in range(100):
#     xVals.append(i)
#     gausses.append(random.gauss(3, 2))
#     
# pylab.plot(gausses, xVals)
#==============================================================================
    

#def rSquare(measured, estimated):
#    """measured: one dimensional array of measured values
#       estimate: one dimensional array of predicted values"""
#    SEE = ((estimated - measured)**2).sum()
#    mMean = measured.sum()/float(len(measured))
#    MV = ((mMean - measured)**2).sum()
#    return 1 - SEE/MV

def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))

# Fitting a Quadratic to a Perfect Line
xVals = (0, 1, 2, 3)
yVals = xVals
pylab.plot(xVals, yVals, label="Actual values")
a,b,c = pylab.polyfit(xVals, yVals, 2)
print("a =", round(a, 4), 
      "b =", round(b, 4), 
      "c =", round(c, 4))
estYVals = pylab.polyval((a,b,c), xVals)
pylab.plot(xVals, estYVals, "r--", label="Predictive values")
print("R-squared =", rSquared(yVals, estYVals))

# Predict Another Point Using Same Model
xVals = xVals + (20,)
yVals = xVals
pylab.plot(xVals, yVals, label="Actual values")
estYVals = pylab.polyval((a,b,c), xVals)
pylab.plot(xVals, estYVals, "r--", label="Predictive values")
print("R-squared =", rSquared(yVals, estYVals))

# Simulate a Small Measurement Error
xVals = (0,1,2,3)
yVals = (0,1,2,3.1)
pylab.plot(xVals, yVals, label="Actual values")
model = pylab.polyfit(xVals, yVals, 2)
print("model", model)
estYVals = pylab.polyval(model, xVals)
pylab.plot(xVals, estYVals, "r--", label="Predicted values")
print("R-squared =", rSquared(yVals, estYVals))

# Predict Another Point Using Same Model
xVals = xVals + (20,)
yVals = xVals
estYVals = pylab.polyval(model, xVals)
print("R-squared =", rSquared(yVals, estYVals))
pylab.figure()
pylab.plot(xVals, estYVals)