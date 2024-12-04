import csv
from importlib import import_module
from importlib.resources import files
import sys


class csv_dialect(csv.unix_dialect):
    quoting = csv.QUOTE_MINIMAL


def main():
    outputs = [
        ("Day", "Part", "Output"),
    ]

    for day in range(1, 26):
        for part in range(1, 3):
            package = f"aoc_2024.days.day{day}"

            try:
                module = import_module(f"{package}.part{part}")
            except ImportError:
                outputs.append((
                    day, part, "[NOT_IMPLEMENTED]",
                ))
                continue

            input_path = files(module).joinpath(f"input")

            try:
                with input_path.open() as puzzle_input:
                    puzzle_output = module.solve_puzzle(puzzle_input.read())
                outputs.append((
                    day, part, puzzle_output,
                ))
            except Exception as e:
                raise RuntimeError(
                    f"Exception when solving puzzle for day {day}, part {part}: {e}"
                ) from e

    writer = csv.writer(sys.stdout, dialect=csv_dialect)
    writer.writerows(outputs)
