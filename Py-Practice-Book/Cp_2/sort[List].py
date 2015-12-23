# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 13:51:42 2015

@author: raihan.hazarika
"""

def lensort(arr):
    arr.sort(key=lambda x : len(x))
    return arr
    
print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

def sort_m(arr):
    arr.sort(key=lambda x : x[1])
    return arr
    
print sort_m([[2, 3], [4, 6], [6, 1]])