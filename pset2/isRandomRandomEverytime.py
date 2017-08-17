#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:15:37 2017

@author: sss
"""
import random

# is random random everytime?
class MyRandom():
    def __init__(self):
        self.rd = random.random()
    def __str__(self):
        return str(self.rd)