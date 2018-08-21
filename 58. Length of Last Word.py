# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:06:50 2018

@author: GEAR
"""
'''
s.strip()去掉字符串首尾的指定的字符（默认为空格或换行符
s.lstrip() 去掉左边的字符
s.rstrip() 去掉右边的字符
'''

class Solution1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1]) #这里split()无参数会出错？
 
class Solution1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if len(s) >= 1:
            return len(s[-1])
        return 0

    
s = Solution()
s1 = 'Hello World'
s2 = "Hello "
print(s.lengthOfLastWord(s1))
print(s.lengthOfLastWord(s2))