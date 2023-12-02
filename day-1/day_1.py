# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.
#
# It looks like some of the digits are actually spelled out
# with letters: one, two, three, four, five, six, seven, eight,
# and nine also count as valid "digits".

import os
import re


def replace_spelled_digits(text, reversed=False):
    word_to_digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if reversed:
        word_to_digit_map = {k[::-1]: v for k, v in word_to_digit_map.items()}

    def replace_match(match):
        word = match.group(0)
        return word_to_digit_map.get(word, word)

    pattern = "|".join(re.escape(word) for word in word_to_digit_map.keys())
    return re.sub(pattern, replace_match, text)


def find_string_first_digit(str, reversed=False):
    first_digit = None

    parsed_str = replace_spelled_digits(str, reversed)
    for char in parsed_str:
        if char.isdigit():
            first_digit = char
            break

    return first_digit


def find_first_last_digit(str):
    first_digit = find_string_first_digit(str)
    last_digit = find_string_first_digit(str[::-1], True)
    return first_digit, last_digit


def get_rows_from_text(text):
    return text.split("\n")


def get_calibration_value(text):
    first_digit, last_digit = find_first_last_digit(text)

    digit_str = ""
    if first_digit is not None:
        digit_str += first_digit
    if last_digit is not None:
        digit_str += last_digit

    return int(digit_str) if digit_str else 0


def sum_calibration_values(text):
    rows = get_rows_from_text(text)
    calibration_values = [get_calibration_value(row) for row in rows]
    return sum(calibration_values)


if __name__ == "__main__":
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_1_input.txt").read()
    print(sum_calibration_values(input_text))
