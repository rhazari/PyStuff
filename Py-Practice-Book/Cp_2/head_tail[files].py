# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 11:51:31 2015

@author: raihan.hazarika
"""

import sys

size = len(open(sys.argv[2]).readlines())

def head_tail(num_line=10):
    if(sys.argv[1] == "head"):
        fp = open(sys.argv[2])
        for _ in xrange(num_line):
            print fp.readline().strip()
    elif(sys.argv[1] == "tail"):
        fp = open(sys.argv[2])
        index = 0
        arr = []
        while(index < size):
            index += 1
            arr.append(fp.readline().strip())
        for m in range(size-num_line,size):
            print arr[m]
        
head_tail()