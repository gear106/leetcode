# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:39:54 2018

@author: GEAR
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []  #创建一个栈
        for bracket in s:
            if bracket in left: #若当前字符在left中
                stack.append(bracket)   #把当前左括号入栈
            elif bracket in right:
                if not stack or not 1 <= ord(bracket) - ord(stack[-1]) <=2:
                    #若当前栈为空
                    #或右括号减去左括号的值不是小于等于2大于等于1
                    return False
                stack.pop() #删除左括号
        return not stack  #若栈内没有值返回True,否则返回False
        
s = Solution()
print(s.isValid('()'))
        