#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:19:23 2017

@author: sss
"""

#==============================================================================
# import random
# 
# balls = ["red"] * 4 + ["green"] * 4
# 
# def three_balls_of_same_color(balls, numTrials):
#     same_color_count = 0
#     for t in range(numTrials):
#         three_balls = random.sample(balls, 3)
#         if len(set(three_balls)) == 1:
#             same_color_count += 1
#     return same_color_count / numTrials
#==============================================================================


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    import random
    balls = ["red"] * 4 + ["green"] * 4
    same_color_count = 0
    for t in range(numTrials):
        three_balls = random.sample(balls, 3)
        if len(set(three_balls)) == 1:
            same_color_count += 1
    return same_color_count / numTrials