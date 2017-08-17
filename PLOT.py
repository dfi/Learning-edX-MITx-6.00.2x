#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:02:19 2017

@author: sss
"""
import pylab

MySamples = []
MyLinear = []
MyQuadratic = []
MyCubic = []
MyExponential = []

for i in range(30):
    MySamples.append(i)
    MyLinear.append(i)
    MyQuadratic.append(i ** 2)
    MyCubic.append(i ** 3)
    MyExponential.append(1.5 ** i)

#pylab.figure('lin')
#pylab.xlabel('sample points')
#pylab.ylabel('linear function')
#pylab.plot(MySamples, MyLinear)
#pylab.figure('quad')
#pylab.plot(MySamples, MyQuadratic)
#pylab.figure('cube')
#pylab.plot(MySamples, MyCubic)
#pylab.figure('expo')
#pylab.plot(MySamples, MyExponential)
#pylab.figure('quad') # reopen the figure to add x label and y label.
#pylab.xlabel('quad x points')
#pylab.ylabel('quadratic function')
#
#pylab.figure('lin')
#pylab.clf()
#pylab.ylim(0, 1000)
#pylab.plot(MySamples, MyLinear)
#pylab.figure('quad')
#pylab.clf()
#pylab.ylim(0, 1000)
#pylab.plot(MySamples, MyQuadratic)
#pylab.figure('cube')
#pylab.clf()
#pylab.plot(MySamples, MyCubic)
#pylab.figure('expo')
#pylab.clf()
#pylab.plot(MySamples, MyExponential)
#
#pylab.figure('lin')
#pylab.title('My Linear')
#pylab.figure('quad')
#pylab.title('My Quadratic')
#pylab.figure('cube')
#pylab.title('My Cubic')
#pylab.figure('expo')
#pylab.title('My Exponential')

# Comparison of plot
# overlaying plots
pylab.figure('lin quad')
pylab.clf()
pylab.subplot(121)
pylab.ylim(0, 900)
pylab.plot(MySamples, MyLinear, 'r-', label='linear', linewidth=2.0)
pylab.legend(loc='best')
pylab.subplot(122)
pylab.ylim(0, 900)
pylab.plot(MySamples, MyQuadratic, 'g^', label='quadratic', linewidth=3.0)
pylab.legend(loc='upper left')

pylab.figure('cube exp')
pylab.clf()
pylab.subplot(211)
pylab.ylim(0, 140000)
pylab.plot(MySamples, MyCubic, 'bo', label='cubic', linewidth=4.0)
pylab.subplot(212)
pylab.ylim(0, 140000)
pylab.plot(MySamples, MyExponential, 'r^', label='exponential', linewidth=5.0)
pylab.legend(loc='best')

pylab.figure('lin quad')
pylab.title('Linear vs. Quadratic')
pylab.figure('cube exp')
pylab.title('Cubic vs. Exponential')

# changing scales
pylab.figure('cube exp log')
pylab.clf()
pylab.plot(MySamples, MyCubic, 'g--', label='cubic', linewidth=2.0)
pylab.plot(MySamples, MyExponential, 'r', label='exponential', linewidth=4.0)
pylab.yscale('log')
pylab.legend(loc='upper left')
pylab.title('Cubic vs. Exponential')
