# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:00:26 2018

@author: GEAR
"""
'''
解题思路：
采用牛顿迭代法 x[n+1] = x[n] - f(x[n]) / diff(f(x[n]))
'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 1
        while (abs(res*res - x) > 0.1):
            res = res - (res*res - x)/(2*res)
        return int(res)
    
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))