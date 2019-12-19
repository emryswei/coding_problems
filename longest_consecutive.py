#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:23:47 2019

@author: tracy

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

返回最长的连续1的长度（转换成二进制）
      11101111   (x)
    & 11011110   (x << 1)
    ----------
      11001110   (x & (x << 1)) 
        ^    ^
        |    |
   trailing 1 removed

"""

def longestConsecutive(x):
    count = 0
    while x!=0:
        x = (x & (x<<1))
        count += 1
    return count

print(longestConsecutive(14))
print(longestConsecutive(100))
print(longestConsecutive(222))

    
    