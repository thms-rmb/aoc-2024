from collections import defaultdict
import functools



def solve_puzzle(puzzle_input: str) -> str:
    lines = puzzle_input.splitlines()

    orderings = defaultdict(set)

    def cmp(a, b):
        if b in orderings[a]:
            return 1
        if a in orderings[b]:
            return -1
        return 0

    while line := lines.pop(0):
        before, num = map(int, line.split('|'))

        orderings[num].add(before)

    res = 0

    while lines and (line := lines.pop(0)):
        numbers = [int(n) for n in line.split(",")]
        sorted_numbers = sorted(numbers, key=functools.cmp_to_key(cmp))

        if numbers != sorted_numbers:
            continue

        res += numbers[len(numbers) // 2]

    return str(res)
