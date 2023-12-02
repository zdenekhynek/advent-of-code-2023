# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# In game 1, three sets of cubes are revealed from the bag
# (and then put back again). The first set is 3 blue cubes and 4 red cubes;
# the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
# the third set is only 2 green cubes.

# The Elf would first like to know which games would have been
# possible if the bag contained only 12 red cubes, 13 green cubes, and
# 14 blue cubes?

import os
import re

# RGB
input_bag = (12, 13, 14)


def extract_game_id_from_log_text(str):
    match = re.search(r"Game (\d+)", str)
    if match:
        return int(match.group(1))


def parse_color_log(color_log):
    [int_str, color] = color_log.strip().split(" ")
    return (color, int(int_str))


def extract_draw_from_draw_log(draw_log_txt):
    """
    1 red, 2 green, 6 blue -> (1, 2, 6)
    3 blue, 4 red -> (4, 0, 3)
    """
    color_parts = [parse_color_log(s) for s in draw_log_txt.split(",")]
    color_parts_dict = {color: count for color, count in color_parts}

    r = color_parts_dict["red"] if "red" in color_parts_dict else 0
    g = color_parts_dict["green"] if "green" in color_parts_dict else 0
    b = color_parts_dict["blue"] if "blue" in color_parts_dict else 0

    return (r, g, b)


def extract_game_from_game_log(txt):
    [id_log_part, draws_log_part] = [s.strip() for s in txt.split(":")]
    id = extract_game_id_from_log_text(id_log_part)

    draw_log_parts = [s.strip() for s in draws_log_part.split(";")]
    draws = [extract_draw_from_draw_log(draw_log) for draw_log in draw_log_parts]
    return {"id": id, "draws": draws}


def is_game_draw_possible(draw, bag=input_bag):
    return all(count <= available for count, available in zip(draw, bag))


def is_game_possible(game, bag=input_bag):
    return all(is_game_draw_possible(draw, bag) for draw in game["draws"])


def get_possible_games_from_logs(txt, bag=input_bag):
    lines = txt.splitlines()
    games = [extract_game_from_game_log(line) for line in lines]
    return list(filter(lambda game: is_game_possible(game, bag), games))


def get_sum_of_possible_games_from_logs(txt):
    possible_games = get_possible_games_from_logs(txt)
    ids = [game["id"] for game in possible_games]
    return sum(ids)


def get_game_minimum_set(game):
    draws = game["draws"]

    minimum_set = (0, 0, 0)
    for draw in draws:
        minimum_set = tuple(max(d, m) for d, m in zip(draw, minimum_set))

    return minimum_set


def get_power_of_set(set):
    return set[0] * set[1] * set[2]


def sum_of_game_minimum_sets(txt):
    lines = txt.splitlines()
    games = [extract_game_from_game_log(line) for line in lines]
    minimum_sets = [get_game_minimum_set(game) for game in games]
    return sum(get_power_of_set(set) for set in minimum_sets)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_2_input.txt").read()
    print(f"Part 1: {get_sum_of_possible_games_from_logs(input_text)}")

    # PART 2
    # The power of a set of cubes is equal to the numbers of
    # red, green, and blue cubes multiplied together.
    print(f"Part 2: {sum_of_game_minimum_sets(input_text)}")
