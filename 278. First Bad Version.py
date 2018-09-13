# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:40:07 2018

@author: GEAR
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n-1
        while left <= right:
            mid = (left+right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid -1
        return left
        
        