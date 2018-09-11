# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:54:26 2018

@author: GEAR
"""
'''
234. 回文链表:
    采用将链表的元素储存到列表中，最后反转列表比较两个列表是否相同
'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val = []
        while head is not None:
            val.append(head.val)
            head = head.next
        return val == val[::-1]
    
    