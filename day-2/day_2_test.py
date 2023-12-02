from day_2 import (
    extract_game_from_game_log,
    extract_draw_from_draw_log,
    extract_game_id_from_log_text,
    is_game_draw_possible,
    is_game_possible,
    get_possible_games_from_logs,
    get_sum_of_possible_games_from_logs,
)

test_text = """# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_extract_game_id_from_log_text():
    assert extract_game_id_from_log_text("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 1


def text_extract_draw_from_draw_log():
    assert extract_draw_from_draw_log("1 red, 2 green, 6 blue") == (1, 2, 6)


def test_extract_game_from_game_log():
    assert extract_game_from_game_log("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        "id": 1,
        "draws": [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
    }


def test_is_game_draw_possible():
    assert is_game_draw_possible((1, 0, 0), (1, 2, 20)) == True
    assert is_game_draw_possible((2, 0, 0), (1, 2, 20)) == False


def test_is_game_possible():
    assert is_game_possible({"draws": [(1, 0, 0), (0, 0, 0)]}, (1, 2, 20)) == True
    assert is_game_possible({"draws": [(1, 0, 0), (0, 3, 0)]}, (1, 2, 20)) == False


def test_get_possible_games_from_logs():
    assert len(get_possible_games_from_logs(test_text)) == 3


def test_get_sum_of_possible_games_from_logs():
    get_sum_of_possible_games_from_logs(test_text) == 8
