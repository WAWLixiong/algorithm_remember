"""
628.
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
"""

class Solution1:
    """
    t: O(nlog n)
    s: O(nlog n)
    """
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        return max(nums[0] * nums[1] * nums[n-1], nums[n-1] * nums[n-2] * nums[n-3])


class Solution2:
    """
    t: O(n)
    s: O(1)
    """
    def maximumProduct(self, nums):
        min1, min2 = float('inf'), float('inf')
        max1 = max2 = max3= -float('inf')

        for i in nums:
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif max1 > i > max2:
                max2, max3 = i, max2
            elif i > max2:
                max2 = i

            if i < min1:
                min1, min2 = i, min1
            elif min1 < i < min2:
                min2 = i
        return max(min1 * min2 * max1, max1 * max2 * max3)
