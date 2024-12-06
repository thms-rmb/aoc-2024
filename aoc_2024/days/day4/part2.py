coordinate = tuple[int, int]

def is_within_box(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    return 0 <= y <= end[0] and 0 <= x <= end[1]


def get_north_east(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    y -= 1
    x += 1

    if is_within_box(end, (y, x)):
        return (y, x)


def get_south_east(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    y += 1
    x += 1

    if is_within_box(end, (y, x)):
        return (y, x)


def get_south_west(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    y += 1
    x -= 1

    if is_within_box(end, (y, x)):
        return (y, x)


def get_north_west(
    end: coordinate,
    position: coordinate,
):
    y, x = position

    y -= 1
    x -= 1

    if is_within_box(end, (y, x)):
        return (y, x)


def is_xmas(
    grid: list[list[str]],
    end: coordinate,
    position: coordinate,
):
    pieces_left = {"M", "S"}
    for getter in get_north_west, get_south_east:
        if (new_position := getter(end, position)) is None:
            continue
        pieces_left -= {grid[new_position[0]][new_position[1]]}

    pieces_right = {"M", "S"}
    for getter in get_north_east, get_south_west:
        if (new_position := getter(end, position)) is None:
            continue
        pieces_right -= {grid[new_position[0]][new_position[1]]}

    return not pieces_left | pieces_right


def solve_puzzle(puzzle_input: str) -> str:
    grid = [list(line) for line in puzzle_input.splitlines()]

    end = (len(grid) - 1, len(grid[0]) - 1)

    a_coordinates = []
    res = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "A":
                a_coordinates.append((y, x))

    for a_coordinate in a_coordinates:
        if is_xmas(grid, end, a_coordinate):
            res += 1

    return str(res)
