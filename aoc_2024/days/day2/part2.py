def is_safe(levels, increasing):
    if len(levels) == 1:
        return True

    left, right, *rest = levels
    diff = left - right

    if diff == 0:
        return False
    elif increasing is None:
        increasing = diff < 0
    elif increasing != (diff < 0):
        return False

    if not 1 <= abs(diff) <= 3:
        return False

    return is_safe([right, *rest], increasing)


def solve_puzzle(puzzle_input: str) -> str:
    reports = puzzle_input.splitlines()

    res = 0

    for levels in [
        [int(l) for l in report.split()] for report in reports
    ]:
        if is_safe(levels, None):
            res += 1
        else:
            for i in range(len(levels)):
                if is_safe([*levels[0:i], *levels[i + 1:]], None):
                    res += 1
                    break

    return str(res)
