# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 14:32:26 2015

@author: raihan.hazarika
"""

def zipper(arr1, arr2):
    size = min(len(arr1), len(arr2))
    print [(arr1[x],arr2[y]) for x in xrange(size) for y in xrange(size) if x == y]
    
zipper([1, 2, 3], ["a", "b", "c"])



square = lambda x : x**2
def mapper(func,num):
    print [ func(x) for x in range(num+1) ]
    
mapper(square, 9)

def triplet(num):
    print [ (x,y,z) for x in range(num) for y in range(x,num) for z in range(y,num) if x+y == z ]

triplet(5)