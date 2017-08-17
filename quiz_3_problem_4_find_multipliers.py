#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:12:23 2017

@author: sss
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    NO_SOLUTION = "no solution"
    if len(L) == 0:
        return NO_SOLUTION
    elif len(L) == 1:
        return NO_SOLUTION if s%L[0] != 0 else s//L[0]
    else:
        try:
            return s//L[0] + greedySum(L[1:], s%L[0])
        except TypeError:
            return NO_SOLUTION