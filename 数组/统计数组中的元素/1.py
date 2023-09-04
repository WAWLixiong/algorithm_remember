"""
645.
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""


class Solution1:
    """
    t: O(nlog n)
    s: O(nlog n)
    """
    def findErrorNums(self, nums):
        n = len(nums)
        errorNums = [0, 0]
        nums.sort()
        prev = 0
        for idx, i in enumerate(nums):
            if i == prev:
                errorNums[0] = i
            elif i - prev > 1:
                errorNums[1] = prev + 1
            prev = i

        if nums[n - 1] != n:
            errorNums[1] = n
        return errorNums


class Solution2:
    """
    t: O(n)
    s: O(n)
    """
    def findErrorNums(self, nums):
        errorNums = [0, 0]
        n = len(nums)
        book = {}
        for i in nums:
            book.setdefault(i, 0)
            book[i] += 1

        for i in range(1, n+1):
            if book.get(i, 0) == 2:
                errorNums[0] = i
            elif book.get(i, 0) == 0:
                errorNums[1] = i
        return errorNums


class Solution3:
    """
    t: O(n)
    s: O(1)

    """
    def findErrorNums(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        n = len(nums)
        for i in range(1, n+1):
            xor ^= i
        lowbit = xor & -xor
        num1, num2 = 0, 0
        for i in nums:
            if i & lowbit == 0:
                num1 ^= i
            else:
                num2 ^= i
        for i in range(1, n+1):
            if i & lowbit == 0:
                num1 ^= i
            else:
                num2 ^= i
        for i in nums:
            if i == num1:
                return [num1, num2]
        return [num2, num1]


