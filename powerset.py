"""
>>> hello = powerset([1,2,3,4,5])

>>> len(hello)
32

>>> print(hello)

"""



def powerset(nums):
    powerset = [[]]
    for i in nums:
        powerset = powerset+[elem+[i] for elem in powerset]

    return powerset

if __name__=="__main__":
    import doctest
    doctest.testmod()