# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 11:48:00 2015

@author: raihan.hazarika
"""

def group(arr,val):
    if(0 == len(arr)%val):
        size = len(arr)/val
    else:
        size = len(arr)/val + 1
    array = []
    for n in xrange(size):
        tmp = arr[n*3:n*3+val]
        array.append(tmp)
    return array
            
            
print group([1,2,3,4,5,6,7,8,9],3)
print group([1,2,3,4,5,6,7,8,9],4)

#Sample use of Zip
names = ["a", "b", "c"]
values = [1, 2, 3]
for name, value in zip(names, values):
    print name, value