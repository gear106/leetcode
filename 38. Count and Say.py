# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:04:03 2018

@author: GEAR
"""
'''
''表示没有任何字符， ' '表示有一个空格字符
利用递归思想计算对应数的个数再加上对用的数
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + ' '
        res, count = '', 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res

        

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(3))