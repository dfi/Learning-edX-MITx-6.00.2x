#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:08:55 2017

@author: sss
"""
# Unit 2, Lecture 6, Random walks, Exercise 2

import random

mylist_one = []
for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist_one.append(number)
print('my list one:', mylist_one)

mylist_two = []
for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist_two:
            mylist_two.append(number)
print('my list two:', mylist_two)

random.seed()

mylist_three = []
random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist_three.append(number)
print('my list three:', mylist_three)

random.seed()