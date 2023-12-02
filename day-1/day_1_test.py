from day_1 import (
    sum_calibration_values,
    get_calibration_value,
    find_string_first_digit,
    find_first_last_digit,
    get_rows_from_text,
    replace_spelled_digits,
)

part1_test_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

part2_test_text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_rows_from_text():
    assert len(get_rows_from_text(part1_test_text)) == 4
    assert get_rows_from_text(part1_test_text)[3] == "treb7uchet"


def test_replace_spelled_digits():
    assert replace_spelled_digits("two1nine") == "219"
    assert replace_spelled_digits("eightwothree") == "8wo3"
    assert replace_spelled_digits("eightwo") == "8wo"
    assert replace_spelled_digits("eightwo"[::-1], True) == "eigh2"[::-1]


def test_find_string_first_digit():
    assert find_string_first_digit("asd2") == "2"
    assert find_string_first_digit("pqr3stu8vwx") == "3"
    assert find_string_first_digit("asd") == None


def test_find_first_last_digit():
    assert find_first_last_digit("a1b2c3d4e5f") == ("1", "5")
    assert find_first_last_digit("pqr3stu8vwx") == ("3", "8")
    assert find_first_last_digit("two1nine") == ("2", "9")
    assert find_first_last_digit("oneeightwo") == ("1", "2")


def test_calibration_value():
    assert get_calibration_value("a1b2c3d4e5f") == 15
    assert get_calibration_value("eightwothree") == 83
    assert get_calibration_value("fdas") == 0
    assert get_calibration_value("two1nine") == 29
    assert get_calibration_value("oneeighthree") == 13
    assert get_calibration_value("49onefour7fivezchhjrpbmteightwokrs") == 42


def test_sum_calibration_values():
    assert sum_calibration_values(part1_test_text) == 142
    assert sum_calibration_values(part2_test_text) == 281
