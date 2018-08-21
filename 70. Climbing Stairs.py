# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:12:02 2018

@author: GEAR
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]