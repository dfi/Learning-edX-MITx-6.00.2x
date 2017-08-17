#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:25:43 2017

@author: sss
"""

# Unit 3, Lecture 8 - Monte Carlo Simulations
# Central Limit Therorem

import pylab
import random

#L = [1, 1, 1, 1, 2]
#pylab.hist(L)
#
#factor = pylab.array(len(L)*[1])/len(L)
#print(factor)
#pylab.figure()
#pylab.hist(L, weights = factor)

def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot/len(X)) ** 0.5
    return mean, std


def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5 * random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means),
               hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1, 1000000, 19, "1 die", "b", "*")
print("Mean of rolling 1 die =", str(mean) + ",", "Std =", std)
#mean, std = plotMeans(50, 1000000, 19, "Mean of 50 dice", "r", "//")
print("Mean of rolling 50 dice =", str(mean) + ",", "Std =", std)
pylab.title("Rolling Continuous Dice")
pylab.xlabel("Value")
pylab.ylabel("Probability")
pylab.legend()