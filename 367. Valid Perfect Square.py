# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 23:27:48 2018

@author: GEAR
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            res = mid**2
            if res == num:
                return True
            else:
                if res > num:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
    
    
                