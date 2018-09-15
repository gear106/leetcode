# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:12:59 2018

@author: GEAR
"""
'''
这道题有点误解，若排序数组中的数比target大，则返回第一个大于target的数
否则返回排序数组中的第一个数
solution1:采用顺序搜索
solution2:采用二分搜索

'''
class Solution1:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(0, len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]
    
class Solution2:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)-1
        
        while left <= right:
            mid = (left+right)//2
            if letters[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left % len(letters)]
