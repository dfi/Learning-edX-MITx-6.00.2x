#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:48:16 2017

@author: sss
"""

# edx MITx 6.00.2x Problem 2-2
"""
What is the exact probability of 
rolling at least two 6's when rolling a die three times? 
"""

import random
#import fractions

def roll(numTrials):
    num_rolls = 3
    die = [1, 2, 3, 4, 5, 6]
    at_least_two_times_six = 0
    for t in range(numTrials):
        die_six = 0
        for r in range(num_rolls):
            if random.choice(die) == 6:
                die_six += 1
        if die_six >= 2:
            at_least_two_times_six += 1
    return at_least_two_times_six / numTrials