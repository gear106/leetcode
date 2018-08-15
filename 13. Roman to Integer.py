# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 21:08:13 2018

@author: GEAR
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
                'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1
                }
        
        res = 0
        for i in range(len(s)):
            if i > 0 and lookup[s[i]] > lookup[s[i-1]]:
                res = res + lookup[s[i]] - 2 * lookup[s[i-1]]
            else:
                res += lookup[s[i]]
        return res
    
s = Solution()
string = 'IV'
print(s.romanToInt(string))