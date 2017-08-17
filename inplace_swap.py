#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:04:21 2017

@author: sss
"""

a = 1
b = 2

def inplace_swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
    

a, b = inplace_swap(a, b)
print(a, b)