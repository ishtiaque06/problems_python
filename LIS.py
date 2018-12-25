"""
>>> LIS([], [])
'hello'

"""


def LIS(list, LIS):
    return "hello"


if __name__ == "__main__":
    print("Testing the given tests...")
    import doctest

    doctest.testmod()
    input_list = input("Enter your python list: ").split(',')
    for item in input_list:
        item = int(item)
        print(type(item))
    print(input_list)
