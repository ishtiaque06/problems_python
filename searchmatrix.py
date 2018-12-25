"""
>>> s = Solution()

>>> s.searchMatrix([[5,6,10,14],[6,10,13,18],[10,13,18,19]], 14)
True
"""

import math
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        mid = math.ceil((len(matrix)-1)/2)
        temp = []
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                temp.append(row)
        rotated_temp = zip(*temp)
        in_list = []
        for row in rotated_temp:
            if row[0] <= target and row[-1] >= target:
                in_list.append(search(row, target))
        if True in in_list:
            return True

def search(list, target):
    if len(list) == 1:
        if list[0] == target:
            return True
        return False
    if len(list) == 2:
        if list[0] == target or list[1] == target:
            return True
        else:
            return False
    else:
        mid = math.ceil((len(list)-1)/2)
        if list[mid] == target:
            return True
        elif list[mid] > target:
            return search(list[:mid], target)
        else:
            return search(list[mid:], target)


if __name__ == "__main__":
    import doctest
    doctest.testmod()