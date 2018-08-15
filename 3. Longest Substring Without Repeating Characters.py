# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:08:20 2018

@author: GEAR
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, start, n = 0, 0 , len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1) + 1)
            l = max(l, i-start+1)
            maps[s[i]] = i
        return l
    

s = "libinglin"
ss = Solution()
print(ss.lengthOfLongestSubstring(s))