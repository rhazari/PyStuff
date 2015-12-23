# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sum(array):
    if(0 == len(array)):
        return
    result = array[0]
    for x in array[1:]:
        result += x
    return result
        
print sum(["aa","bb","cc"])
print sum([1,4,5,6])
print sum([])
print sum(["hello", "world"])     
        

    