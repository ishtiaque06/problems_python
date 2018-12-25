"""
>>> s = Solution()

>>> s.validPalindrome("ebcbbececabbacecbbcbe")
True

"""



class Solution:
    def __init__(self):
        self.removed = False

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        return self.isValid(l)

    def isValid(self, list):
        if len(list) <= 2:
            return True
        if list[0] == list[-1]:
            return self.isValid(list[1:-1])
        elif list[0] != list[-1]:
            if self.removed == True:
                return False
            if list[0] == list[-2]:
                self.removed = True
                return self.isValid(list[0:-1]) or self.isValid(list[1:])
            elif list[1] == list[-1]:
                self.removed = True
                return self.isValid(list[1:])
            else:
                return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()