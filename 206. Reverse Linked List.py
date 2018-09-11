# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:59:54 2018

@author: GEAR
"""
'''
206. 反转链表:
    通过创建一个新链表来实现链表反转
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        newList = None
        
        while current is not None:
            nxt = current.next
            current.next = newList
            newList = current
            current = nxt
        return newList
    
