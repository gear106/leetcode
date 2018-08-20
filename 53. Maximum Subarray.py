# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:46:43 2018

@author: GEAR
"""

class Solution1:    #这个方法在leetcode上会超时
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 设置为无穷小
        ans = float('-inf')
        # 这个循环控制子串的元素个数
        for i in range(1, len(nums)+1):
            # 这个循环控制子串从哪个位置开始计算
            for j in range(len(nums)+1 - i):
                big = 0
                big = sum(nums[j: j+i])
                if big > ans:
                    ans = big
        return ans
    
class Solution2: 
    '''
    使用动态规划，我们知道计算到i处的最大值有两种可能，一是加上nums[i]另一个是从
    nums[i]重新开始计算，我们比较maxSum[i-1]+ nums[i] 和 nums[i]的大小即可
    '''
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[i] for i in range(n)]
        for i in range(1, len(nums)):
            maxSum[i] = max(maxSum[i-1] + nums[i], nums[i])
        return max(maxSum)



s = Solution2()               
nums = [-2,1]
print(s.maxSubArray(nums))