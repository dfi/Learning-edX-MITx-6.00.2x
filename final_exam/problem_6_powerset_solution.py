#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:52:49 2017

@author: sss
"""

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import numpy
    
    def int_to_bin_ndarray(i, full_length):
        s = bin(i)[2:]
        s = "0" * (full_length - len(s)) + s
        result = []
        for i in s:
            result.append(int(i))
        return numpy.array(result)

    N = len(choices)
    results = []
    for i in range(2**N):
        r = int_to_bin_ndarray(i, N)
        if sum(r * choices) <= total:
            results.append(r)
    results.sort(key=(lambda x: (sum(x*choices), -sum(x))), reverse=True)
    return results[0]
        
if __name__ == "__main__":
    print(find_combination([4, 6, 3, 5, 2], 10))
        