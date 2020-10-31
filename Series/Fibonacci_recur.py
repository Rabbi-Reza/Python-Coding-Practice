#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:15:24 2020

@author: nirzhor
"""

 
def Fibonacci(n):
    if n <= 0:
       # print("Incorrect input")
        return "Incorrect input"
        
    # First Fibonacci number is 0
    # if n==1:
    #     return 0
    
    # Second Fibonacci number is 1
    # elif n==2:
    #     return 1

    if n in [1,2]:
        return n-1

    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


num = int(input("How many terms you want ? "))

for i in range(1,num+1):
    print(Fibonacci(i))
     
