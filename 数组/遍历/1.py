"""
485.
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            if count > maxCount:
                maxCount = count
                count = 0
        return max(maxCount, count)