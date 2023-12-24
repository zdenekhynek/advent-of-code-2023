from day_8 import (
    get_instruction_list_from_text,
    get_nodes_from_text,
    get_number_of_steps,
    get_simultaneous_number_of_steps,
)

text_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

text_input2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

part2_text_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def test_get_instruction_list_from_text():
    assert get_instruction_list_from_text(text_input) == "RL"


def test_get_nodes_from_text():
    result = get_nodes_from_text(text_input)
    assert len(result) == 7
    assert result["BBB"] == {"L": "DDD", "R": "EEE"}


def test_get_number_of_steps():
    assert get_number_of_steps(text_input) == 2
    assert get_number_of_steps(text_input2) == 6


def test_get_simultaneous_number_of_steps():
    assert get_simultaneous_number_of_steps(part2_text_input) == 6
