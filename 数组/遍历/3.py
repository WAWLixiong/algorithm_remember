"""
414.
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
"""




class Solution1:
    """
    t: O(nlog n)
    s: O(nlog n)
    """
    def thirdMax(self, nums):
        nums.sort(reversed=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                diff += 1
                if diff == 3:
                    return nums[i]
        return nums[0]


class Solution2:
    """
    t: O(n)
    s: O(1)
    """
    def thirdMax(self, nums):
        a = b = c = None
        for num in nums:
            if a is None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b is not None and b > num and (c is None or num > c):
                c = num
        return a if c is None else c