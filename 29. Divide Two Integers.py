# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 10:27:52 2018

@author: GEAR
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)  #这里不加括号会出错
        dividend, divisor =abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i = i << 10
                temp = temp << 10
                
        if not positive:
            res = -res
        return min(max(-2**31,res), 2**31 - 1)

s = Solution()
dividend, divisor = 9,3
print(s.divide(dividend, divisor))
        