from day_16 import (
    create_map,
    get_next_tile_loc,
    move_beam,
    move_beams,
    get_num_energized_tiles,
    calculate_num_energized_tiles,
    get_all_start_beams,
)

text_input = """.|...{....
|.-.{.....
.....|-...
........|.
..........
.........{
..../.{{..
.-.-/..|..
.|....-|.{
..//.|....
"""

s = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

s1 = """
>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
"""

s2 = """
######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
"""


def test_create_map():
    test_map = create_map(text_input)
    assert len(test_map["tiles"]) == 100
    assert test_map["size"] == [10, 10]


def test_get_next_tile_loc():
    test_map = create_map(text_input)
    assert get_next_tile_loc(test_map, {"direction": "right", "tile": [0, 0]}) == [1, 0]
    assert get_next_tile_loc(test_map, {"direction": "left", "tile": [0, 0]}) == None
    assert get_next_tile_loc(test_map, {"direction": "top", "tile": [0, 0]}) == None
    assert get_next_tile_loc(test_map, {"direction": "down", "tile": [1, 1]}) == [1, 2]
    assert get_next_tile_loc(test_map, {"direction": "down", "tile": [1, 8]}) == [1, 9]
    assert get_next_tile_loc(test_map, {"direction": "left", "tile": [6, 6]}) == [5, 6]


def test_move_beam():
    test_map = create_map(text_input)
    beam = {"direction": "right", "tile": [0, 0], "added": False}
    beams = [beam]
    new_beam = move_beam(test_map, beam, beams)
    assert beams[0]["direction"] == "up"
    assert new_beam["direction"] == "down"


def test_move_beams():
    test_map = create_map(text_input)
    beam = {"direction": "right", "tile": [0, 0], "added": False}
    beams = [beam]
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    assert beams[0]["direction"] == "down"
    assert len(beams) == 1
    beams = move_beams(test_map, beams)
    assert len(beams) == 2
    assert beams[0]["direction"] == "left"
    assert beams[1]["direction"] == "right"
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    assert len(beams) == 1
    assert beams[0]["tile"] == [4, 7]
    assert beams[0]["direction"] == "up"
    beams = move_beams(test_map, beams)
    assert beams[0]["tile"] == [4, 6]
    assert beams[0]["direction"] == "right"
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    assert beams[0]["tile"] == [6, 6]
    assert beams[0]["direction"] == "down"
    beams = move_beams(test_map, beams)
    beams = move_beams(test_map, beams)
    assert len(beams) == 2
    assert beams[0]["tile"] == [6, 8]
    assert beams[0]["direction"] == "left"
    assert beams[1]["direction"] == "right"
    beams = move_beams(test_map, beams)
    assert len(beams) == 3
    beams = move_beams(test_map, beams)
    assert beams[0]["tile"] == [4, 8]
    assert beams[1]["tile"] == [7, 7]
    assert beams[2]["tile"] == [7, 9]


def test_get_num_energized_tiles():
    test_map = create_map(text_input)
    assert get_num_energized_tiles(test_map) == 0
    test_map["tiles"][0]["visited"]["down"] = True
    assert get_num_energized_tiles(test_map) == 1


def test_calculate_num_energized_tiles():
    # 46 tiles become energized.
    test_map = create_map(text_input)
    assert calculate_num_energized_tiles(test_map) == 46

    test_map = create_map(text_input)
    start_beam = {"direction": "down", "tile": [9, -1], "added": False}
    assert calculate_num_energized_tiles(test_map, start_beam) == 6


def test_get_all_start_beams():
    text_map = create_map(text_input)
    start_beams = get_all_start_beams(text_map)
    assert len(start_beams) == 40
