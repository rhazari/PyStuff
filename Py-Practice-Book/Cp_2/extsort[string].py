# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 01:01:19 2015

@author: Raihan
"""

def extsort(arr):
    arr.sort(key=lambda x:x.split('.')[1])
    return arr
    
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])