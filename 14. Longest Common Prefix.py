# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:12:47 2018

@author: GEAR
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # 若存在则一定在第一个字符串strs[0]中
        for i in range(len(strs[0])):
            for str in strs:
                #存在比当前短的string或存在于当前index字符不相同的字符串
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]
    
