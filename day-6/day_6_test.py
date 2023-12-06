from day_6 import (
    calculate_distance,
    calculate_possible_race_wins,
    calculate_win_number_product,
    calculate_win_number_product_part2,
    get_num_of_possible_wins,
    get_win_number_product,
    parse_log,
    parse_bad_kerning_numbers_txt,
)

test_input = """Time:      7  15   30
Distance:  9  40  200"""

def test_parse_log():
    assert parse_log(test_input) == ([7, 15, 30], [9, 40, 200])

def test_parse_bad_kerning_numbers_txt():
    assert parse_bad_kerning_numbers_txt("Time:      7  15   30") == 71530
    
def test_calculate_distance():
    assert calculate_distance(7, 0) == 0
    assert calculate_distance(7, 2) == 10
    assert calculate_distance(7, 3) == 12
    assert calculate_distance(7, 4) == 12
    assert calculate_distance(7, 5) == 10
    assert calculate_distance(7, 6) == 6
    assert calculate_distance(7, 7) == 0

def test_get_num_of_possible_wins():
    assert get_num_of_possible_wins([9, 40, 200], 10) == 2


def test_get_win_number_product():
    assert get_win_number_product([4, 8, 9]) == 288


def test_calculate_possible_race_wins():
    assert calculate_possible_race_wins(7, 9) == 4


def test_calculate_win_number_product():
    assert calculate_win_number_product(test_input) == 288

def test_calculate_win_number_product_part2():
    assert calculate_win_number_product_part2(test_input) == 71503