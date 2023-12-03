from day_3 import get_numbers, create_grid, is_valid_part_number, get_cells_neighbords, has_symbol, sum_part_numbers

test_small_input = """abcd
efgh
ijkl"""

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_create_grid():
    assert len(create_grid(test_input)) == 10
    assert len(create_grid(test_input)[0]) == 10
    assert create_grid(test_input)[0][0] == "4"
    assert create_grid(test_input)[1][3] == "*"


def test_get_numbers():
    assert get_numbers(0, "467..114..") == [
        {"number": 467, "start": 0, "end": 3, "line": 0},
        {"number": 114, "start": 5, "end": 8, "line": 0},
    ]


def test_get_cells_neighbords():
    grid = create_grid(test_small_input)

    assert get_cells_neighbords(grid, 1, 3, 1) == ["a", "b", "c", "d", "e", "h", "i", "j", "k", "l"]

    # try top
    assert get_cells_neighbords(grid, 1, 3, 0) == ["a", "d", "e", "f", "g", "h"]

    # try bottom
    assert get_cells_neighbords(grid, 1, 3, 2) == ["e", "f", "g", "h", "i", "l"]

    # try left
    assert get_cells_neighbords(grid, 0, 1, 1) == ["a", "b", "f", "i", "j"]

    # try right
    assert get_cells_neighbords(grid, 3, 4, 1) == ["c", "d", "g", "k", "l"]

    # try top right
    assert get_cells_neighbords(grid, 3, 4, 0) == ["c", "g", "h"]

    # try bottom right
    assert get_cells_neighbords(grid, 3, 4, 2) == ["g", "h", "k"]

    # try top left
    assert get_cells_neighbords(grid, 0, 1, 0) == ["b", "e", "f"]

    # try bottom left
    assert get_cells_neighbords(grid, 0, 1, 2) == ["e", "f", "j"]


def test_has_symbol():
    assert has_symbol([".", "a", 0, "0"]) == False
    assert has_symbol(["*", "a", 0, "0"]) == True
    assert has_symbol([".", "a", 0, "-"]) == True
    assert has_symbol([".", "$", 0, "0"]) == True
    assert has_symbol([".", "+", 0, "0"]) == True


def test_is_valid_part_number():
    grid = create_grid(test_input)

    assert is_valid_part_number(grid, {"number": 114, "start": 5, "end": 8, "line": 0}) == False

    assert is_valid_part_number(grid, {"number": 35, "start": 2, "end": 4, "line": 2}) == True


def test_sum_part_numbers():
    assert sum_part_numbers(test_input) == 4361