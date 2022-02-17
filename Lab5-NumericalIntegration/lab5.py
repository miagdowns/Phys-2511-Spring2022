#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:03:10 2022

@author: miadowns
"""
import numpy as np
import matplotlib.pyplot as plt

f = lambda x : -.5*x+4
a = -5; b = 5; 
J = int(input("what is your delta x"))

x = np.linspace(a,b,J+1)
y = f(x)

X = np.linspace(a,b,J+1)
Y = f(X)

dx = (b-a)/J
x_left = np.linspace(a,b-dx,J)
x_midpoint = np.linspace(dx/2,b - dx/2,J)
x_right = np.linspace(a+dx,b,J)

print("Partition with",J,"subintervals.")
left_riemann_summ = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_summ)


right_riemann_summ = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_summ)

f = lambda x : -.29*x**2 -x +12.5
a = -5; b = 5; 
N = int(input("what is your delta x"))

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,N+1)
Y = f(X)

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(a+dx,b,N)

print("Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)


right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)

f = lambda x : 1+10*((x+1)*np.exp(-x**2))
a = -5; b = 5; 
R = int(input("what is your delta x"))

x = np.linspace(a,b,R+1)
y = f(x)

X = np.linspace(a,b,R+1)
Y = f(X)

dx = (b-a)/R
x_left = np.linspace(a,b-dx,R)
x_midpoint = np.linspace(dx/2,b - dx/2,R)
x_right = np.linspace(a+dx,b,R)

print("Partition with",R,"subintervals.")
left_riemann_summm = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_summm)


right_riemann_summm = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_summm)

eq1 = ((abs(40 - left_riemann_summ))/((40+left_riemann_summ)/2))*100
print ("left sum percent difference for first equation is", eq1)

eq2 = ((abs(100.83 - left_riemann_sum))/((100.83+left_riemann_sum)/2))*100
print ("left sum percent difference for second equation is", eq2)

eq3 = ((abs(27.72 - left_riemann_summm))/((27.72+left_riemann_summm)/2))*100
print ("left sum percent difference for first equation is", eq3)

x_coordinates = [J, N, R]
y_coordinates = [eq1, eq2, eq3]
plt.xlabel('delta x value')

plt.ylabel('percentage diference')

plt.scatter(x_coordinates, y_coordinates)


