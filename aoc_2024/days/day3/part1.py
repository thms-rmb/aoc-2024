import re

mul_re = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

def solve_puzzle(puzzle_input: str) -> str:
    res = 0

    for line in puzzle_input.splitlines():
        for match in mul_re.finditer(line):
            left, right = map(int, match.groups())

            res += left * right

    return str(res)
