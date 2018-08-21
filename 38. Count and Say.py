# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:01:18 2018

@author: GEAR
"""

class Solution1:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*'
        res, count = '', 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res

        

if __name__ == '__main__':
    s = Solution1()
    print(s.countAndSay(3))