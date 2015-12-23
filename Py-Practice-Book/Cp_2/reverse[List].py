# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 11:08:11 2015

@author: raihan.hazarika
"""

def reverse(arr):
    size = len(arr)
    if(0 == size or 1 == size):
        return
    for n in range(size/2):
        tmp = arr[n]
        arr[n] = arr[size-n-1]
        arr[size-n-1] = tmp
    return arr

array = [1,3,5,6,8]
print reverse([1,3,5,6,8])
