# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:49:08 2018

@author: GEAR
"""
'''
通过创建一个新链表，在原链表基础上添加一个节点，这样可避免原链表只有一个元素或没
元素的情况
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newList = ListNode(0)
        newList.next = head
        current = newList
        
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return newList.next


            
    
        
                