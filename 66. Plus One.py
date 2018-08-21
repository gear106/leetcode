# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:19:36 2018

@author: GEAR
"""
'''
解题思路：
若为空列表直接返回[1],若最后一位小于9，则直接去掉最后一位的列表加上最后
一位进位后的数，若最后一位大于9，则采用递归思想计算去掉最后一位的列表加上
[0]
'''
class Solution1:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        if digits[-1] < 9:
            return digits[:-1] + (digits[-1] + 1)
        else:
            return self.plusOne(digits[:-1]) + [0]
'''
解题思路：
采用位运算的思路,从发列表最后一位计算其加上1后的值是否小于10，若小于10则循环结束
否则对应位置为进位后的数减去10
'''       
class Solution2:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """     
        carry = 1
        for i in range(len(digits)-1, -1, -1): #这里循环从列表的最后一个位置开始
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] -= 10
        if carry == 1:
            digits.insert(0, 1)
        return digits