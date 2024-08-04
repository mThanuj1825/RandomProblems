"""
Find the minimum size of a subset S of A which satisfy the following conditions:
-> Let the product of the subset be S be equal to P
-> P must be divisible by X
"""
from typing import List


def solve(n: int, x: int, arr: List[int]) -> int:
    min_size = float("inf")

    # For all subarrays
    # for i in range(1 << n):
    #     prod = 1
    #     ss = 0
    #     for j in range(n):
    #         if i & (1 << j):
    #             prod *= arr[j]
    #             ss += 1
    #
    #     if prod % x == 0:
    #         min_size = min(min_size, ss)
    #

    # For contigous subarrays
    # prod = 1
    # left = 0
    #
    # for right in range(n):
    #     prod *= arr[right]
    #
    #     while prod % x == 0 and left <= right:
    #         min_size = min(min_size, right - left + 1)
    #         prod //= arr[left]
    #         left += 1
    #
    # return min_size


tests = {
    1: {
        "n": 1,
        "x": 2,
        "arr": [2],
        "res": 1
    },
    2: {
        "n": 4,
        "x": 16,
        "arr": [2, 2, 2, 2],
        "res": 4
    }
}

for key in tests:
    test = tests[key]
    result = solve(test["n"], test["x"], test["arr"])

    if result == test["res"]:
        print("Passed")
    else:
        print("Failed")
