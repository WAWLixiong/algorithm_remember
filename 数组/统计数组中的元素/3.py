"""
448.
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for num in nums:
            x = (num - 1) % n  # num % n - 1 也是正确的, 而且更容易理解
            nums[x] += n
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret