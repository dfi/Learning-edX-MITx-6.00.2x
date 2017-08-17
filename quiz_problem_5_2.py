#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:38:26 2017

@author: sss
"""

import itertools

def max_sub_set_sum(L):
    return max(iter_powerset(L), key=lambda x: sum(x))

def iter_powerset(iterable):
    s = list(iterable)
    result = itertools.chain.from_iterable(itertools.combinations(s,r) \
                                           for r in range(len(s)+1))
    return list(result)

L = [1, 3, 2, -2, 6, -5, 7, 3]


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L 
    """   
    def all_contig_sub_sets(L):
        result = []
        for sub_set_len in range(1, len(L)+1):
            for i in range(len(L)-sub_set_len+1):
                result.append(L[i:i+sub_set_len])
        return result
    
    return sum(max(all_contig_sub_sets(L), key=lambda x: sum(x)))

