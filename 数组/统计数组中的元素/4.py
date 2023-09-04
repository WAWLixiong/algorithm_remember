"""
442.
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题
"""


class Solution1:
    """
    t: O(n), 每次交换都会让至少一个元素找到正确位置
    s: O(1)
    """
    def findDuplicates(self, nums):
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]


class Solution2:
    """
    t: O(n)
    s: O(1)
    """
    def findDuplicates(self, nums):
        ans = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                ans.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        return ans