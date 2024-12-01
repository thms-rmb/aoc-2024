def solve_puzzle(puzzle_input: str) -> str:
    left = []
    right = []

    for line in puzzle_input.splitlines():
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

    result = 0
    for a, b in zip(sorted(left), sorted(right)):
        result += abs(a - b)

    return str(result)
