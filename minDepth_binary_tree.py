#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:06:44 2019

@author: tracy

Find Minimum Depth of a Binary Tree

Given a binary tree, find its minimum depth. 

The minimum depth is the number of nodes along the shortest path from 

the root node down to the nearest leaf node.

minimum depth不是指最少层数，是最短路径。如最短路径=1，即只有2个node相连，minimum depth = 2，不是1

从root node开始，到leaf node。 root node是level-1， 下一层的leaf node是level-2

leaf node定义：leaf node的left，right子节点都是Null，才叫leaf node

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def minDepth(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return minDepth(root.right) + 1
    
    if root.right is None:
        return minDepth(root.left) + 1
    
    return min(minDepth(root.left), minDepth(root.right)) + 1        


# Driver Program  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print("Minimum depth of the binary tree is:", minDepth(root))

'''
如果用BFS的方法
'''


def bfsMinDepth(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    left = bfsMinDepth(root.left)
    
    right = bfsMinDepth(root.right)
    
    if left is None:
        return right + 1
    
    if right is None:
        return left + 1
    
    return min(left, right) + 1
    
    
# Driver Program  
root = Node(6) 
root.left = Node(7) 
root.right = Node(73) 
root.left.left = Node(34) 
root.left.right = Node(55) 
print("Minimum depth of the binary tree by BFS is:", bfsMinDepth(root))
