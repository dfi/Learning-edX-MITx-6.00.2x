#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:45:44 2017

@author: sss
"""

class Point:
    pass

blank = Point()
blank.x = 3.0
blank.y = 4.0


class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def growRect(box, dwidth, dheight):
    box.width += dwidth
    box.height += dheight
    
def growRect_copy(box, dwidth, dheight):
    import copy
    newbox = copy.copy(box)
    newbox.width += dwidth
    newbox.height += dheight
    return newbox

def growRect_deepcopy(box, dwidth, dheight):
    import copy
    newbox = copy.deepcopy(box)
    newbox.width += dwidth
    newbox.height += dheight
    return newbox