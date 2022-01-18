# -*- coding: utf-8 -*-
import time
import random


value = input("Enter your yes or no question: ")


r = random.randint(1, 6)
print('Calculating...')
time.sleep(5)
print('your question was ' + value)

if r == 1:
    print("My answer is: no")
    
elif r == 2:
    print("My answer is: yes")
    
elif r == 3:
    print("My answer is: maybe")
    
elif r == 4:
    print("my answer is: Ask again later")
    
elif r == 5:
    print("My answer is: most likely")
    
else:
    print("My answer is: unlikely")
    
