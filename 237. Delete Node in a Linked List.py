# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:47:19 2018

@author: GEAR
"""
'''
237. 删除链表中的节点
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
