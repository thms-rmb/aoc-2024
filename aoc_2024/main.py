import csv
from datetime import datetime
from importlib import import_module
from importlib.resources import files
import sys


class csv_dialect(csv.unix_dialect):
    quoting = csv.QUOTE_MINIMAL


def main():
    outputs = [
        ("Day", "Part", "Time (in microseconds)", "Output"),
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
                    start_time = datetime.now()
                    puzzle_output = module.solve_puzzle(puzzle_input.read())
                    end_time = datetime.now()
                    elapsed_time = (end_time - start_time).microseconds
                outputs.append((
                    day, part, elapsed_time, puzzle_output,
                ))
            except Exception as e:
                raise RuntimeError(
                    f"Exception when solving puzzle for day {day}, part {part}: {e}"
                ) from e

    writer = csv.writer(sys.stdout, dialect=csv_dialect)
    writer.writerows(outputs)
