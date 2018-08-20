# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:18:26 2018

@author: GEAR
"""

class Solution1:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
class Solution2:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i
    
class Solution3:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
            
        
        
s = Solution3()
nums = [1,2,4]
target = 0
print(s.searchInsert(nums, target))