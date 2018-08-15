# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:52:38 2018

@author: GEAR
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #用p1,p2赋值为l1,l2，以防止操作改变原始链表
        p1, p2 = l1, l2
        #创建一个空链表用来返回结果
        head = ListNode(0)
        tail = head
        #carry 表示进位值
        carry = 0
        #处理两个链表的公共部分，也就是两个链表都不为空的部分
        while p1 and p2:
            #计算当前位相加的值
            num = p1.val + p2.val + carry
            #大于9， 应该向前进位
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            #添加结点
            tail.next = ListNode(num)
            #尾结点向后移动
            tail = tail.next
            #移动两套链表的公共部分
            p1 = p1.next
            p2 = p2.next
        #取长链表剩余的部分，也就是未参与上边计算的部分
        if p2:
            #如果p2较长，将p2剩余的部分赋值给p1,只需处理p1就可以
            p1 = p2
        #接下来处理长链表剩余的部分
        while p1:
            #最近的一位，我们要考虑一下是否有进位
            num = p1.val + carry
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            #添加结点
            tail.next = ListNode(num)
            tail = tail.next
            #移动处理的链表
            p1 = p1.next
        #如果最后仍然有进位，需要再分配一个结点
        if carry:
            #创建一个val为1的ListNode结点，然后将tail向后移动一位
            tail.next = ListNode(1)
            tail = tail.next
        #将所有的加和进位都处理完了，现在将链表收尾
        tail.next = None
        #将链表的头结点返回
        return head.next    #去掉初始化为0的头结点
    
la = ListNode(2)
la.next = ListNode(4)
la.next.next = ListNode(3)

lb = ListNode(5) 
lb.next = ListNode(6)
lb.next.next = ListNode(4)

s = Solution()
ss = s.addTwoNumbers(la, lb)
print(ss.val)
print(ss.next.val)
print(ss.next.next.val)
print(ss.next.next.next)