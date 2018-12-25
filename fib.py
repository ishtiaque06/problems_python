"""
>>> fib(1)
0
>>> fib(2)
1

>>> fib(3)
1

>>> fib(4)
2

>>> fib(5)
3

>>> fib(6)
5

>>> fib(7)
8

>>> fib(8)
13

>>> fib(9)
21

>>> fib(10)
34

>>> fib(11)
55

>>> fib(100)
218922995834555169026

>>> fib(500)
86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501

"""

"""
    Dynamic Programming Array Example of Fibonacci Problem O(n) space, O(n) time
"""
# def fib(n):
#     fibArray = [0] * (n + 1)
#     for i in range(1, n + 1):
#         if i == 1:
#             fibArray[i] = 0
#         elif i == 2:
#             fibArray[i] = 1
#         elif i == 3:
#             fibArray[i] = 1
#         else:
#             fibArray[i] = fibArray[i - 1] + fibArray[i - 2]
#     return fibArray[n]


"""
    Dynamic Programming Example without Array in Fib (Problem) with O(1) space, O(n) time
"""
def fib(n):
    prev = 0
    prev_prev = 0
    result = 0
    for i in range(1, n+1):
        if i == 2 or i == 3:
            prev = 1
            result = prev + prev_prev
        else:
            prev_prev = prev
            prev = result
            result = prev + prev_prev
    return result



if __name__ == "__main__":
    import doctest

    doctest.testmod()
