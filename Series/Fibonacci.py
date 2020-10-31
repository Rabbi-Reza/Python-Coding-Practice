#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:05:40 2020

@author: nirzhor
"""

inpu = int(input("How many terms you want ? "))

n1,n2 = 0,1
count = 0

if inpu <= 0:
    print(" Enter a positive value")
    
elif inpu == 1:
    print("Fibonacci series upto ", inpu, " terms : ")
    print(n1)
    
else:
    print("Fibonacci series upto ", inpu, " terms : ")
    
    while ( count < inpu ):
        print(n1)
        nth = n1 + n2
        
        n1 = n2
        n2 = nth
        count += 1