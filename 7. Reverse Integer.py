# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:27:31 2018

@author: GEAR
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_reverse = 0
        if x < 0:
            x = int(str(abs(x))[::-1])
            x_reverse = -x
        else:
            x = int(str(x)[::-1])
            x_reverse = x
        if x_reverse > 2**31 - 1 or x_reverse < -2**31:
            return 0
        else:
            return x_reverse
        
s = Solution()
x = -120
print(s.reverse(x))
        
        
            