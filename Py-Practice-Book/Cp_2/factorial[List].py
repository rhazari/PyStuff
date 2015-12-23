# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 10:17:11 2015

@author: raihan.hazarika
"""

def factorial_r(num):
    if(0 == num):
        return 1
    else:
        return num*factorial_r(num-1)
    

def factorial_a(num):
    result = 1
    for x in xrange(1,num+1):
        result *= x
    return result

def factorial_dp(num):
    arr = [1,1]
    for n in xrange(2,num+1):
        arr[1] = n*arr[0]
        arr[0] = arr[1]
    return arr[0]

print factorial_r(5)
print factorial_a(6)
print factorial_dp(6)