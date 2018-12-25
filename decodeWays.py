"""
>>> numDecodings("251")
"""


def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if s == '':
        return 1
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    dp = [0] * (len(s) - 1)

    for i in range(1, len(s)):
        if s[i] == '0' and (s[i - 1] > '2' or s[i - 1] == '0'):
            return 0
        elif s[i] == '0' and (s[i - 1] == '2' or s[i-1] == '1'):
            dp[i - 1] = dp[i - 2]

        if i == 1 and s[:i + 1] <= '26':
            dp[0] = 2
        elif i == 1 and s[:i+1] > '26':
            dp[0] = 1
        if i > 1 and '10' <= s[i - 1:i+1] <= '26':
            dp[i - 1] = dp[i - 2] + 1
        elif i > 1 and s[i-1:i+1] < '10' or s[i-1:i+1] > '26':
            dp[i - 1] = dp[i - 2]
    return dp


if __name__ == "__main__":
    import doctest
    doctest.testmod()