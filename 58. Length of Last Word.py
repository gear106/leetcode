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
        if s[-1] == '':
            return 0
        else:
            s = s.split()
            return len(s[-1])
    
s = Solution()
s1 = 'Hello World'
s2 = "Hello "
print(s.lengthOfLastWord(s1))
print(s.lengthOfLastWord(s2))