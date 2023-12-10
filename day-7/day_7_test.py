from day_7 import (
    get_hand_score,
    get_card_score,
    parse_hands,
    get_secondary_hand_score,
    get_total_hand_score,
    get_hand_sum,
    compute_rank_hands,
    sort_hands,
)

text_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_get_card_score():
    assert get_card_score("J") == "01"
    assert get_card_score("2") == "02"
    assert get_card_score("K") == "12"
    assert get_card_score("T") == "10"
    assert get_card_score("Q") == "11"
    assert get_card_score("A") == "13"


def test_get_hand_score():
    assert get_hand_score("32T3K") == 1
    assert get_hand_score("KK677") == 2
    assert get_hand_score("KTJJT") == 5
    assert get_hand_score("T55J5") == 5
    assert get_hand_score("QQQJA") == 5
    assert get_hand_score("JJJJA") == 6


def test_sort_hands():
    l = [{"hand": "KTJJT", "score": get_hand_score("KTJJT")}, {"hand": "QQQJA", "score": get_hand_score("QQQJA")}]
    assert sort_hands(l)[0]["hand"] == "QQQJA"

def test_get_secondary_hand_score():
    assert get_secondary_hand_score("AKQ") == 0.131211


def test_get_total_hand_score():
    assert get_total_hand_score("32T3K") == 1.0302100312

def test_parse_hands():
    assert parse_hands(text_input) == [
        {"hand": "32T3K", "bet": "765"},
        {"hand": "T55J5", "bet": "684"},
        {"hand": "KK677", "bet": "28"},
        {"hand": "KTJJT", "bet": "220"},
        {"hand": "QQQJA", "bet": "483"},
    ]


def test_get_hand_sum():
    assert get_hand_sum(text_input) == 5905
