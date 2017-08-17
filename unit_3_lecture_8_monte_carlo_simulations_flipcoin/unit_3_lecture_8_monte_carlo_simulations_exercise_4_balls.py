#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:25:38 2017

@author: sss
"""


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """   
    
    def getMeanAndStd(X):
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        std = (tot/len(X))**0.5
        return mean, std

    def drawThreeBalls(numDrawns):
        import random
        three_balls_of_same_color_drawns = 0
        for d in range(numDrawns):
            bucket = ["r", "r", "r", "g", "g", "g"]
            three_balls = []
            for i in range(3):
                pick = random.choice(bucket)
                three_balls.append(pick)
                bucket.remove(pick)
            if len(set(three_balls)) == 1:
                three_balls_of_same_color_drawns += 1
        return three_balls_of_same_color_drawns / numDrawns

    def getEst(numDrawns, numTrials):
        estimates = []
        for t in range(numTrials):
            guess = drawThreeBalls(numDrawns)
            estimates.append(guess)
        curEst, sDev = getMeanAndStd(estimates)
        return curEst, sDev
    
    def noReplacementSimulationWithPrecision(precision, numTrials):
        numDrawns = 100
        sDev = precision
        while sDev >= precision / 1.96:
            curEst, sDev = getEst(numDrawns, numTrials)
            numDrawns *= 2
        return curEst

    return noReplacementSimulationWithPrecision(0.05, numTrials)
    
