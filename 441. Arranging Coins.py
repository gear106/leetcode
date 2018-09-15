# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:58:18 2018

@author: GEAR
"""

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(2*n + 0.25) - 0.5)