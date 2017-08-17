#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 07:33:38 2017

@author: sss
"""
import random
import pylab

# Unit 3, Lecture 7 - Inferential Statistics, Exercise 3
def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the length of the strings, or
        NaN if L is empty.
    """
    if len(L) == 0:
        return float('nan')
    mean = sum(len(s) for s in L) / float(len(L))
    sum_of_quantity = sum((len(s)-mean)**2 for s in L)
    std = (sum_of_quantity / len(L)) ** 0.5
    return round(std, 4)

# Exercise 4.3
# Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.
def covOfNumList(L):
    """
    L: a list of numbers
    returns: float, the standard deviation of the list of numbers, of NaN if
        L is empty.
    """
    if len(L) == 0:
        return float('nan')
    mean = sum(L) / float(len(L))
    print('mean:', mean)
    if mean == 0:
        return float('nan')
    std = (sum((i-mean)**2 for i in L) / len(L)) ** 0.5
    return round(std/mean, 3)

# Generating Normal Distribution
def genNormalDistribution(the_range, mean, std_dev):
    dist = []
    for i in range(the_range):
        dist.append(random.gauss(mean, std_dev))
    pylab.hist(dist, std_dev)
