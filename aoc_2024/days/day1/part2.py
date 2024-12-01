from collections import defaultdict


def solve_puzzle(puzzle_input: str) -> str:
    left = []
    right = defaultdict(int)

    for line in puzzle_input.splitlines():
        a, b = map(int, line.split())
        left.append(a)
        right[b] += 1

    result = 0

    for a in left:
        result += a * right[a]

    return result
