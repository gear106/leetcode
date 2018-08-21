# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:43:18 2018

@author: GEAR
"""
'''
解题思路：采用递归思想求和
当最后一位都为1时，先将1加给b[-1],然后再递归
'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (a == '' or b == ''):
            return a + b
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1], self.addBinary(b[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        
        