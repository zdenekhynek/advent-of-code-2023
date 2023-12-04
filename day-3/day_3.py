# any number adjacent to a symbol, even diagonally, is a "part number"
# and should be included in your sum. (Periods (.) do not count as a symbol.)

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers
# because they are not adjacent to a symbol: 114 (top right)
# and 58 (middle right). Every other number is adjacent to
# a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger.
# What is the sum of all of the part numbers in
# the engine schematic?

import os
import re


def get_numbers(index, txt):
    """
    467..114.. -> [467, 114]
    """

    # match all numbers
    pattern = "\d+"

    numbers = []
    for match in re.finditer(pattern, txt):
        s = match.start()
        e = match.end()
        numbers.append({"number": int(match.group(0)), "start": s, "end": e, "line": index})

    return numbers


def get_cells_neighbords(grid, start, end, line):
    neighbors = []

    if line > 0:
        start_index = max(0, start - 1)
        end_index = min(len(grid[line - 1]), end + 1)

        neighbors.extend(grid[line - 1][start_index:end_index])

    if start > 0:
        neighbors.append(grid[line][start - 1])
    if end < len(grid[line]):
        neighbors.append(grid[line][end])

    if (line + 1) < len(grid):
        start_index = max(0, start - 1)
        end_index = min(len(grid[line + 1]), end + 1)

        neighbors.extend(grid[line + 1][start_index:end_index])

    return neighbors


def has_symbol(l):
    """
    match any symbol in list
    """
    pattern = "[^.a-zA-z\d]"
    string = "".join([str(x) for x in l])
    return re.search(pattern, string) is not None


def is_valid_part_number(grid, number):
    # get numbers neighbours (top, bottom, left, right)
    neighbors = get_cells_neighbords(grid, number["start"], number["end"], number["line"])

    # see if any of them are symbols
    return has_symbol(neighbors)


def create_grid(txt):
    return [line[:] for line in txt.splitlines()]


def get_part_numbers(txt):
    grid = create_grid(txt)

    lines = txt.splitlines()

    numbers = []
    for index, line in enumerate(lines):
        numbers.extend(get_numbers(index, line))

    part_numbers = list(filter(lambda number: is_valid_part_number(grid, number), numbers))

    return part_numbers


def sum_part_numbers(txt):
    part_numbers = get_part_numbers(txt)
    part_numbers_values = [number["number"] for number in part_numbers]

    return sum(part_numbers_values)


def get_symbols(lines):
    symbols = []

    for line_index, line in enumerate(lines):
        # get all * symbols
        # print(line)
        for match in re.finditer("\*", line):
            symbols.append({"start": match.start(), "end": match.end(), "line": line_index})

    return symbols


def get_near_numbers(part_numbers, symbol):
    near_part_numbers = []

    for part_number in part_numbers:
        # is in the line vicinity
        if abs(part_number["line"] - symbol["line"]) < 2:
            if part_number["start"] <= symbol["start"] + 1:
                if part_number["end"] > symbol["start"] - 1:
                    near_part_numbers.append(part_number)

    return near_part_numbers


def get_gear_symbols(txt):
    part_numbers = get_part_numbers(txt)

    # A gear is any * symbol that is adjacent to exactly two part numbers.
    # Its gear ratio is the result of multiplying those two numbers together.
    lines = txt.splitlines()
    symbols = get_symbols(lines)

    symbols_with_near_numbers = [get_near_numbers(part_numbers, symbol) for symbol in symbols]

    return [symbol for symbol in symbols_with_near_numbers if len(symbol) == 2]


def compute_gear_ratios(txt):
    gear_symbols = get_gear_symbols(txt)
    gear_products = [gear[0]["number"] * gear[1]["number"] for gear in gear_symbols]
    return sum(gear_products)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_3_input.txt").read()
    print(f"Part 1: {sum_part_numbers(input_text)}")

    # PART 2
    print(f"Part 2: {compute_gear_ratios(input_text)}")
