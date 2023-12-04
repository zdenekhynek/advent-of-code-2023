from day_4 import (
    find_winning_numbers,
    get_card_score,
    parse_card_text,
    parse_numbers_set_txt,
    get_cards_score,
    get_total_scratchcards,
)

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_winning_numbers():
    winning_numbers = [41, 48, 83, 86, 17]
    chosen_numbers = [83, 86, 6, 31, 17, 9, 48, 53]
    assert find_winning_numbers(winning_numbers, chosen_numbers) == [83, 86, 17, 48]


def test_get_card_score():
    winning_numbers = [83]
    assert get_card_score(winning_numbers) == 1

    winning_numbers = [83, 86, 17, 48]
    assert get_card_score(winning_numbers) == 8


def test_parse_numbers_set_txt():
    assert parse_numbers_set_txt("41 48 83 86 17") == [41, 48, 83, 86, 17]


def test_parse_card_text():
    assert parse_card_text("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == [
        [41, 48, 83, 86, 17],
        [83, 86, 6, 31, 17, 9, 48, 53],
    ]


def test_get_cards_score():
    assert get_cards_score(test_input) == 13


def test_get_total_scratchcards():
    assert get_total_scratchcards(test_input) == 30
