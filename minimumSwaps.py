"""
>>> minimumSwaps([7, 1, 3, 2, 4, 5, 6])
5

"""


def minimumSwaps(arr):
    sorted_arr = sorted(arr)
    dict_vals = {v: k for k, v in enumerate(arr)}
    min_swaps = 0
    for i, v in enumerate(arr):
        correct = sorted_arr[i]
        if v != correct:
            swap_index = dict_vals[correct]
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
            dict_vals[v] = swap_index
            dict_vals[correct] = i
            min_swaps += 1

    return min_swaps


if __name__ == "__main__":
    import doctest
    doctest.testmod()