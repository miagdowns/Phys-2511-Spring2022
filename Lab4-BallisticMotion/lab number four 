#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 22:35:27 2022

@author: miadowns
"""

import numpy as np
import matplotlib.pyplot as plt

grav = 9.8
airDen = 1.2      
areaProj = 0.9   
     
v = float(input("What is the velocity? "))
angle = int(input("What is the value of Θ? "))
t = int(input("What is the value of time? (in seconds) "))
  
dragC = 0.5     
m = 20.0         
step = 0.01   

t = [0]
vx = [v*np.cos(angle*np.pi/180)] 
# turning them into degrees no more radians! 
vy = [v*np.sin(angle*np.pi/180)]
x = [0]
y = [0]

dragforce = 0.5*dragC*areaProj*(v**2)*airDen


ax = [-(dragforce*np.cos(angle/180*np.pi))/m]
ay = [-grav-(dragforce*np.sin(angle/180*np.pi)/m)]

print(ax,ay)

counter = 0
while(y[counter] >= 0):
    t.append(t[counter]+step)

    vx.append(vx[counter]+step*ax[counter])
    vy.append(vy[counter]+step*ay[counter])

    x.append(x[counter]+step*vx[counter])
    y.append(y[counter]+step*vy[counter])

    vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2)
    dragForce = 0.5*dragC*areaProj*(vel**2)*airDen

    angle = np.arctan(vy[counter]/vx[counter]) * (180 / np.pi)

    ax.append(-(dragForce*np.cos(angle/180*np.pi))/m)
    ay.append(-grav-(dragForce*np.sin(angle/180*np.pi)/m))

    counter=counter+1


plt.plot(x,y)
plt.ylabel("y (m)")
plt.xlabel("x (m)")

is_between = np.absolute(ax) in range (15-18)
if is_between in range (15-18):
    print ("you are in target range")
else:
    print("you are not in target range")
