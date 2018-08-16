# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:25:18 2018

@author: GEAR
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)
            