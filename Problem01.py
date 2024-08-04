"""
General Ali has initiated an invasion in the sahpe of an NxM Grid behind enemy lines given by 2D array Q.
-> '*': cannot be visited
-> 'A': Ali's army
-> 'E': Enemy army
Every second, any block of 'E' that shares a side with 'A' gets occupied by Ali.
Calculate the minimum time it wil take for General Ali's army to invade all enemy cells in the grid.
"""
from typing import List


def solve(n: int, m: int, grid: List[List[str]]) -> int:
    q = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                q.append((i, j, 0))
                visited.add((i, j))

    max_time = 0

    while q:
        x, y, time = q.pop(0)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                visited.add((nx, ny))
                if grid[nx][ny] == 'E':
                    grid[nx][ny] = 'A'
                    q.append((nx, ny, time + 1))
                    max_time = max(time + 1, max_time)

    for row in grid:
        if 'E' in row:
            return -1

    return max_time


n, m = 2, 2
grid = [
    ["A", "E"],
    ["E", "E"]
]

tests = {
    1: {
        "n": 2,
        "m": 2,
        "grid": [
            ["A", "E"],
            ["E", "E"]
        ],
        "res": 2
    },
    2: {
        "n": 3,
        "m": 2,
        "grid": [
            ["A", "E"],
            ["*", "E"],
            ["E", "E"]
        ],
        "res": 4
    }
}

for key in tests:
    test = tests[key]
    result = solve(test["n"], test["m"], test["grid"])

    print(f"Test {key}: ", end="")
    if result == test["res"]:
        print("Passed")
    else:
        print("Failed")
