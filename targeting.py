# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:54:12 2023

@author: minmod
"""

import math

def getTargetPosition(time):
    
    x = 500 + 100*math.sin(time)
    y = 250 + 100*math.cos(time)
    
    return (x,y)

def calcBulletDirection():
    
    # logic of shooting
    # if getTargetPosition is know, calculate direction to shoot
    angle = 0.25*math.pi
    return (math.cos(angle), -math.sin(angle))