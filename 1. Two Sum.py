# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:57:48 2018

@author: GEAR
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):            
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []
            
            
nums = [3,3]
target = 6
s = Solution()
print(s.twoSum(nums, target))