# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:06:50 2018

@author: GEAR
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
    
s = Solution()
s1 = 'Hello World'
s2 = "Hello "
print(s.lengthOfLastWord(s1))
print(s.lengthOfLastWord(s2))