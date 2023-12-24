from day_9 import (
    get_sum_of_next_values,
    parse_txt_into_sequences,
    get_sequence_diffs,
    extrapolate_sequence,
    get_extrapolate_value,
)


test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_parse_txt_into_sequences():
    sequences = parse_txt_into_sequences(test_input)
    assert len(sequences) == 3
    assert len(sequences[0]) == 6
    assert sequences[1][5] == 21


def test_get_sequence_diffs():
    sequences = parse_txt_into_sequences(test_input)
    assert get_sequence_diffs(sequences[0]) == [3, 3, 3, 3, 3]
    assert get_sequence_diffs(sequences[1]) == [2, 3, 4, 5, 6]


def test_extrapolate_sequence():
    sequences = parse_txt_into_sequences(test_input)
    assert extrapolate_sequence(sequences[0], [3, 3, 3, 3, 3]) == [0, 3, 6, 9, 12, 15, 18]
    assert extrapolate_sequence(sequences[0], [3, 3, 3, 3, 3], True) == [-3, 0, 3, 6, 9, 12, 15]
    assert extrapolate_sequence(sequences[2], [5, 3, 3, 5, 9, 15], True) == [5, 10, 13, 16, 21, 30, 45]


def test_get_extrapolate_value():
    sequences = parse_txt_into_sequences(test_input)
    assert get_extrapolate_value(sequences[0]) == 18
    assert get_extrapolate_value(sequences[1]) == 28
    assert get_extrapolate_value(sequences[2]) == 68
    assert get_extrapolate_value(sequences[0], True) == -3
    assert get_extrapolate_value(sequences[1], True) == 0
    assert get_extrapolate_value(sequences[2], True) == 5


def test_get_sum_of_next_values():
    assert get_sum_of_next_values(test_input) == 114
    assert get_sum_of_next_values(test_input, True) == 2
