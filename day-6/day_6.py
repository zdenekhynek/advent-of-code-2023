"""
As part of signing up, you get a sheet of paper (your puzzle input) 
that lists the time allowed for each race and also the best distance 
ever recorded in that race. To guarantee you win the grand prize, 
you need to make sure you go farther in each race than the current
record holder.
"""

"""Time:      7  15   30
Distance:  9  40  200"""

import re
import os


def parse_numbers_txt(numbers_txt):
    pattern = "\d+"
    return [int(match) for match in re.findall(pattern, numbers_txt)]


def parse_bad_kerning_numbers_txt(numbers_txt):
    pattern = "\d+"

    number = ""
    for match in re.findall(pattern, numbers_txt):
        number += match
    return int(number)


def parse_log(txt, has_bad_kerning=False):
    [time_line, distance_line] = txt.splitlines()
    if has_bad_kerning:
        times = [parse_bad_kerning_numbers_txt(time_line)]
        records = [parse_bad_kerning_numbers_txt(distance_line)]
    else:
        times = parse_numbers_txt(time_line)
        records = parse_numbers_txt(distance_line)
    return (times, records)


def calculate_distance(total_time, pressed_time):
    acc = 1
    speed = pressed_time * acc
    travel_time = total_time - pressed_time
    return speed * travel_time


def get_num_of_possible_wins(distances, record):
    wins = [distance for distance in distances if distance > record]
    return len(wins)


def calculate_possible_race_wins(time, record):
    pressed_times = range(0, time)
    race_distances = [calculate_distance(time, pressed_time) for pressed_time in pressed_times]
    num_possible_wins = get_num_of_possible_wins(race_distances, record)
    return num_possible_wins


def get_win_number_product(num_wins):
    product = 1
    for x in num_wins:
        product = product * x
    return product


def calculate_win_number_product(txt):
    (times, records) = parse_log(txt)
    num_wins = [calculate_possible_race_wins(time, record) for time, record in zip(times, records)]
    return get_win_number_product(num_wins)


def calculate_win_number_product_part2(txt):
    (times, records) = parse_log(txt, True)
    num_wins = [calculate_possible_race_wins(time, record) for time, record in zip(times, records)]
    return get_win_number_product(num_wins)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_6_input.txt").read()
    print(f"Part 1: {calculate_win_number_product(input_text)}")

    # PART 2
    print(f"Part 2: {calculate_win_number_product_part2(input_text)}")
