#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 02:08:19 2017

@author: sss
"""

from math import factorial as fact

# e

e = 0

for n in range(100):
    e = e + 1/fact(n)
    

print(e)