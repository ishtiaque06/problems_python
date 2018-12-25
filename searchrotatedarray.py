"""
# >>> s = Solution()
#
# >>> s.search([4,5,6,7,0,1,2], 0)
# 4
#
# >>> s1 = Solution()
#
# >>> s1.search([4,5,6,7,0,1,2], 4)
# 0
#
# >>> s2 = Solution()
#
# >>> s2.search([4,5,6,7,0,1,2], 5)
# 1
#
# >>> s3 = Solution()
#
# >>> s3.search([4,5,6,7,0,1,2], 6)
# 2
#
# >>> s4 = Solution()
#
# >>> s4.search([4,5,6,7,0,1,2], 7)
# 3
#
# >>> s5 = Solution()
#
# >>> s5.search([4,5,6,7,0,1,2], 1)
# 5
#
# >>> s6 = Solution()
#
# >>> s6.search_split([4,5,6,7,0,1,2])
# 4
#
# >>> s6.split=0
#
# >>> s6.search_split([7,0])
# 1
#
# >>> s6.split=0
#
# >>> s6.search_split([1,2,3,4,5,6,7,8])
#
# >>> s6.split=0
#
# >>> s6.search_split([8,1,2,3,4,5,6,7])
# 1
#
# >>> s6.split=0
#
# >>> s6.search_split([2,3,4,5,6,7,8,1])
# 7
#
# >>> s6.split=0
#
# >>> s6.search_split([5,6,7,8,1,2,3,4])
# 4
#
# >>> s6.split=0
#
# >>> s6.search_split([5,6,7,8,9,1,2,3,4])
# 5

>>> s7 = Solution()

>>> s7.search([3,5,1], 1)
2

"""

import math


class Solution:
    def __init__(self):
        self.count = 0
        self.split = 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.split=0
        split_index = self.search_split(nums)
        mid = math.ceil((len(nums) - 1) / 2)
        if len(nums) == 2:
            if nums[0] == target:
                return self.count
            elif nums[1] == target:
                return self.count + 1
            else:
                return -1
        if split_index is None:
            if nums[0] > target:
                return -1
            if nums[mid] == target:
                self.count = self.count + mid
                return self.count
            if nums[mid] < target:
                self.count = self.count + mid
                return self.search(nums[mid:], target)
            else:
                return self.search(nums[:mid+1], target)

        if nums[split_index] <= target <= nums[-1]:
            self.count = self.count + split_index
            return self.search(nums[split_index:], target)
        else:
            return self.search(nums[:split_index], target)

    def search_split(self, nums):
        mid = math.ceil((len(nums) - 1) / 2)
        if nums[mid] < nums[mid - 1]:
            self.split = self.split + mid
            return self.split
        elif nums[mid] > nums[mid - 1]:
            if nums[0] > nums[mid]:
                return self.search_split(nums[:mid])
            else:
                self.split += mid
                return self.search_split(nums[mid:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
