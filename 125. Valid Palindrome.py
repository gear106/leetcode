# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:54:15 2018

@author: GEAR
"""
'''
解题思路：
利用python内置函数s.isalnum()将字符串中的数字和字母提取到列表中
利用列表的倒序方法[::-1]比较对应位置上的字符是否相等
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [ch for ch in s.lower() if s.isalnum()]
        return s == s[::-1]
        