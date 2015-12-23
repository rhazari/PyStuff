# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 11:28:44 2015

@author: raihan.hazarika
"""

import sys

#The origianl text
print "Original Text"
f = open(sys.argv[1])
print f.read()


#The text in reverse
print "\nText in reverse"
size = len(open(sys.argv[1]).readlines())
arr = []
fp = open(sys.argv[1])
for _ in xrange(size):
    arr.append(fp.readline().strip())
    
for m in xrange(size):
    print arr[size-m-1]