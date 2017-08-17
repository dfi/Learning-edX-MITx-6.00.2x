#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:35:14 2017

@author: sss
"""

#import numpy
#import operator

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
    import numpy, operator
    
    def int_to_bin_with_length(i, length):
        s = bin(i)[2:]
        s = "0" * (length - len(s)) + s
        return s

    def int_str_to_ndarray(s):
        result = []
        for i in s:
            result.append(int(i))
        return numpy.array(result)

    original_order_dict = {}
    for index, item in enumerate(choices):
        original_order_dict[index] = item
    new_dict_list = sorted(original_order_dict.items(), 
                           key=operator.itemgetter(1), 
                           reverse=True)
    
    sorted_choices = [i[1] for i in new_dict_list]

    result_list = [0] * len(choices)
    result = numpy.array(result_list)
    while sum(result * sorted_choices) < total:
        v = int(''.join(map(str, result_list)), 2) + 1
        s = int_to_bin_with_length(v, len(choices))
        result_list = list(s)
        temp = int_str_to_ndarray(s)
        print("temp:", temp)
        print("sorted_choices:", sorted_choices)
        if (len(result_list) > len(choices) or
            sum(temp * sorted_choices) > total):
            break
        result = temp
        
    inds = numpy.array([i[0] for i in new_dict_list]).argsort()
    return result[inds]



#def int_to_bin(i):
#     s = bin(i)[2:]
#     if len(s) % 4 != 0:
#         s = "0" * (4 - (len(s) % 4)) + s
#     return s
#
#def int_to_bin_ndarray(i):
#    s = bin(i)[2:]
#    if len(s) % 4 != 0:
#        s = "0" * (4 - (len(s) % 4)) + s
#    result = []
#    for i in s:
#        result.append(int(i))
#    return numpy.array(result)



#if __name__ == "__main__":
#    print(find_combination([1,1,3,5,3], 5))


#L = [1,2,3,4,5,1,3,10,9,11,12]


#==============================================================================
# # https://en.wikipedia.org/wiki/Subset_sum_problem
# initialize a list S to contain one element 0.
#  for each i from 1 to N do
#    let T be a list consisting of xi + y, for all y in S
#    let U be the union of T and S
#    sort U
#    make S empty 
#    let y be the smallest element of U 
#    add y to S 
#    for each element z of U in increasing order do
#       //trim the list by eliminating numbers close to one another
#       //and throw out elements greater than s
#      if y + cs/N < z ≤ s, set y = z and add z to S 
#  if S contains a number between (1 − c)s and s, output yes, otherwise no
#==============================================================================

#==============================================================================
# N = len(L)
# s = 200
# c = 0.01
# 
# S = [0]
# for i in range(N):
#     print("S:", S)
#     T = []
#     for y in S:
#         T.append(L[i] + y)
#     print("T:", T)
#     U = list(set().union(T, S))
#     print("U:", U)
#     U.sort()
#     print("U:", U)
#     S = []
#     y = U[0]
#     S.append(y)
#     for z in U:
#         if (y + c*s/len(L)) < z <= s:
#             U[0] = z
#             S.append(z)
#     print("S:", S)
#     print("------")
# 
# for i in S:
#     if (1-c)*s < i <= s:
#         print("Yes")
#         break
# else:
#     print("No")
#==============================================================================

        
    
    
    