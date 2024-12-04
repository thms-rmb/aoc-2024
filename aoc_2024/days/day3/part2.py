import re

instructions_re = re.compile(
    r"((mul)|(do)|(don't))\((([0-9]{1,3}),([0-9]{1,3}))?\)"
)

def solve_puzzle(puzzle_input: str) -> str:
    res = 0

    state = True

    for line in puzzle_input.splitlines():
        for m in instructions_re.finditer(line):
            func, *rest = m.groups()

            if func == "do":
                state = True
            elif func == "don't":
                state = False
            elif func == "mul" and state:
                left, right = map(int, rest[-2:])

                res += left * right

    return str(res)
