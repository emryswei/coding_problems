#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:08:21 2019

@author: tracy

Hi, here's your problem today. This problem was recently asked by Apple:

Create a class that initializes with a list of numbers and 

has one method called sum. sum should take in two parameters, start_idx 

and end_idx and return the sum of the list from start_idx (inclusive) to end_idx` (exclusive).

You should optimize for the sum method.
"""

class ListFastSum:
  def __init__(self, nums):
    self.nums = nums

  def sum(self, start_idx, end_idx):
    # Fill this in.
    if len(self.nums) < start_idx or len(self.nums) < end_idx:
        return "list length is not enough"
    else:
        result = 0
        for i in range(self.nums[start_idx], self.nums[end_idx]):
            result += i
        return result

print(ListFastSum([1,2,3,4,5,6,7,8,9,10]).sum(2,5))
            
#a = [1,2,3,4,5]
#for i in range(a[1], a[4]):
#    print(i)
    
    