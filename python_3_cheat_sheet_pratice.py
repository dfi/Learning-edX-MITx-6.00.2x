#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:22:31 2017

@author: sss
"""

list_one = [1, 2, 3, 4, 5, 6]
a, *b = list_one
*c, d = list_one

#a, b, c, d, e, f, *g = list_one


x = None
del x

print(int(15) == int('15') == int("15") == int('''15'''))
