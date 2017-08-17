#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:20:47 2017

@author: sss
"""


def get_all_subsets(some_list):
    '''Returns all subsets of size 0 - len(some_list) for some_list'''
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

def sort_result_subsets(L):
    for sub_set in L:
        sub_set.sort()
    L.sort()
    L.sort(key=lambda x: len(x))
    return L

NUMBER = 3
def look_for_all_the_things(myList):
    '''Looks at all subsets of this list'''
    # Make subsets
    all_subsets = sort_result_subsets(get_all_subsets(myList))
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = sort_result_subsets(get_all_subsets(L))
for i in a:
    print(i)
print('len(a)', len(a))
