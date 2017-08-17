#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:54:20 2017

@author: sss
"""

import random
import numpy
import math

#==============================================================================
# # estimate pi
# def throwNeedles(numNeedles):
#     inCircle = 0
#     for Needles in range(1, numNeedles + 1, 1):
#         x = random.random()
#         y = random.random()
#         if (x*x + y*y) ** 0.5 <= 1.0:
#             inCircle += 1
#     return 4 * (inCircle/float(numNeedles))
# 
# def getEst(numNeedles, numTrials):
#     estimates = []
#     for t in range(numTrials):
#         piGuess = throwNeedles(numNeedles)
#         estimates.append(piGuess)
#     sDev = numpy.std(estimates)
#     curEst = sum(estimates)/len(estimates)
#     print("Est. = " + str(curEst) +\
#           ", Std. dev. = " + str(round(sDev, 6))\
#           + ", Needles = " + str(numNeedles))
#     return (curEst, sDev)
# 
# def estPi(precision, numTrials):
#     numNeedles = 1000
#     sDev = precision
#     while sDev >= precision / 1.96:
#         curEst, sDev = getEst(numNeedles, numTrials)
#         numNeedles *= 2
#     return curEst
# 
# #random.seed(0)
# estPi(0.005, 100)
#==============================================================================


# estimate sin(pi)
def throwNeedlesForSinPi(numNeedles):
    inSin = 0
    for needles in range(1, numNeedles):
        x = random.uniform(0, math.pi)
        y = random.random()
        if y <= math.sin(x):
            inSin += 1
    return math.pi * inSin / float(numNeedles)

def getEstSinPi(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        sinPiGuess = throwNeedlesForSinPi(numNeedles)
        estimates.append(sinPiGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print("Est. = " + str(curEst) +\
          ", Std. dev. = " + str(round(sDev, 6))\
          + ", Needles = " + str(numNeedles))
    return (curEst, sDev)

def estSinPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 1.96:
        curEst, sDev = getEstSinPi(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

random.seed(0)
estSinPi(0.005, 100)

