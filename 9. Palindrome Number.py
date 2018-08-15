# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:43:35 2018

@author: GEAR
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            if x != int(str(x)[::-1]):
                return False
            else:
                return True

s = Solution()
x = 1121
print(s.isPalindrome(x))
        