import re


coordinate = tuple[int, int]

def iter_horizontal(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    for i in range(x, end[1] + 1):
        yield y, i


def iter_vertical(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    for i in range(y, end[0] + 1):
        yield i, x


def iter_diagonal_up(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    for ii, i in enumerate(range(x, end[1] + 1)):
        if y - ii < 0:
            break
        yield y - ii, i


def iter_diagonal_down(
        end: coordinate,
        position: coordinate,
):
    y, x = position

    for ii, i in enumerate(range(x, end[1] + 1)):
        if y + ii > end[0]:
            break
        yield y + ii, i


xmas_re = re.compile("XMAS")


def solve_puzzle(puzzle_input: str) -> str:
    grid = [list(line) for line in puzzle_input.splitlines()]

    end = (len(grid) - 1, len(grid[0]) - 1)

    res = 0
    texts = []

    def append_with_reversed(coords):
        line = "".join(grid[y][x] for y, x in coords)
        texts.append(line)
        texts.append("".join(reversed(line)))

    for i in range(0, end[0] + 1):
        position = (i, 0)

        append_with_reversed(iter_horizontal(end, position))
        if i > 0:
            append_with_reversed(iter_diagonal_up(end, position))
        if i < end[0]:
            append_with_reversed(iter_diagonal_down(end, position))

    for i in range(0, end[1] + 1):
        position = (0, i)

        append_with_reversed(iter_vertical(end, position))
        if i > 0:
            append_with_reversed(iter_diagonal_down(end, position))

    for i in range(0, end[1] + 1):
        position = (end[0], i)

        if 0 < i < end[1]:
            append_with_reversed(iter_diagonal_up(end, position))

    for text in texts:
        for match in xmas_re.finditer(text):
            res += 1

    return str(res)
