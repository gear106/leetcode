# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:24:05 2018

@author: GEAR
"""
#方法1
class Solution1:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
#方法2  
class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for num in nums[:]:  # 这里需要对nums做拷贝，直接使用nums会出错
            if num == val:
                nums.remove(num)
        return len(nums)
    
#方法3
class Solution3:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for num in nums[:]:
            if num == val:
                nums.pop(s.index(num))
        return len(nums)     
            