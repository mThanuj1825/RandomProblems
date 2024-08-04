"""
Find the minimum size of a subset S of A which satisfy the following conditions:
-> Let the product of the subset be S be equal to P
-> P must be divisible by X
"""
import time
from typing import List


def solve(n: int, x: int, arr: List[int]) -> int:
    min_size = float("inf")

    for i in range(1, 1 << n):
        prod = 1
        ss = 0
        for j in range(n):
            if i & (1 << j):
                prod *= arr[j]
                ss += 1

        if prod % x == 0:
            min_size = min(min_size, ss)

    return min_size


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
    start = time.time()
    result = solve(test["n"], test["x"], test["arr"])
    end = time.time()

    print(f"Test {key}: ", end="")
    if result == test["res"]:
        print("Passed")
    else:
        print("Failed")

    print(f"Time: {(end - start)}")
