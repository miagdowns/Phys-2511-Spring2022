#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:09:18 2022

@author: miadowns
"""

import random as ra 
import time 
ladder  = {3: 15, 7: 14, 15: 18, 20: 100, 25: 50, 31: 90, 40: 57, 50: 61, 62: 75, 71: 82, 75: 89, 86: 98}
snake = {2: 1, 9: 6, 16: 13, 21: 14, 33: 27, 36: 4, 38: 17, 46: 23, 51: 46, 61: 59, 77: 6, 84: 60, 88: 71, 94: 87, 99: 1}



pos1 = 0
pos2 = 0

def move(pos):
        dice = ra.randint(1,6)
        print("dice rolling...")
        time.sleep(3)   
        print(f"you rolled a: {dice}")
        pos = pos + dice 
        if pos in snake:
            print ("you got a snake bite!")
            pos = snake[pos]
            print(f"position is now: {pos}")
        elif pos in ladder:
            print ("you found a ladder!")
            pos = ladder[pos]
            print(f"position is now: {pos}")
        else:
            print(f"position is now: {pos}")
        return pos 
    
while True:
    x = input ("player one, press enter to roll dice")
    pos1 = move(pos1)
    if pos1 >= 100: 
        time.sleep(3)
        print("you won!")
        break
    y = input ("player two, press enter to roll dice")
    pos2 = move(pos2)
    if pos2 >= 100: 
        time.sleep(3)
        print("you won!")
        break
        
 