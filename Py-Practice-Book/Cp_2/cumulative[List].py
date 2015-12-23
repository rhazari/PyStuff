# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 11:28:04 2015

@author: raihan.hazarika
"""

def cumulative_product(arr):
    size = len(arr)
    if(0 or 1 == size):
        return arr
    for n in xrange(1,size):
        arr[n] = arr[n]*arr[n-1]
    return arr
    
def cumulative_sum(arr):
    size = len(arr)
    if(0 or 1 == size):
        return arr
    for n in xrange(1,size):
        arr[n] = arr[n]+arr[n-1]
    return arr
    
print cumulative_product([1,3,5,7,9])
print cumulative_product([4, 3, 2, 1])
print cumulative_product([])
print cumulative_product([5])

print cumulative_sum([1,3,5,7,9])
print cumulative_sum([4, 3, 2, 1])
print cumulative_sum([])
print cumulative_sum([5])