# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:31:44 2018

@author: GEAR
"""
'''
一个整数与自身的异或运算为零，
一个整数与零的异或运算为其本身
'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for item in nums[1:]:
            result ^= i
        return result