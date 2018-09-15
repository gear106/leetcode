# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:38:38 2018

@author: GEAR
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            else:
                if guess(mid) == -1:
                    right = mid - 1
                else:
                    left = mid + 1
        