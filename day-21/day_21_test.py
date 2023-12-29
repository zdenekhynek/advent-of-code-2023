from day_21 import (
    create_map,
    get_position_in_direction,
    step_from_position,
    step,
    find_start_in_map,
    find_tiles_for_steps,
)


test_input = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def test_create_map():
    map = create_map(test_input)
    assert len(map) == 11
    assert len(map[0]) == 11
    assert map[9][1] == {"type": "#", "x": 1, "y": 9, "visited": False}


def test_get_position_in_direction():
    pos = {"x": 0, "y": 0}
    assert get_position_in_direction("E", pos) == {"x": 1, "y": 0}
    assert get_position_in_direction("W", pos) == {"x": -1, "y": 0}
    assert get_position_in_direction("N", pos) == {"x": 0, "y": -1}
    assert get_position_in_direction("S", pos) == {"x": 0, "y": 1}


def test_step_from_position():
    map = create_map(test_input)
    pos = {"x": 0, "y": 0}
    new_positions = step_from_position(map, pos)
    assert len(new_positions) == 2


def test_find_start_in_map():
    map = create_map(test_input)
    start_tile = find_start_in_map(map)
    assert start_tile == {"x": 5, "y": 5, "type": "S", "visited": False}


def test_step():
    # map = create_map(test_input)
    # new_positions = [{"x": 0, "y": 0}]
    # map[0][0]["visited"] = True
    # new_positions = step(map, new_positions)
    # assert len(new_positions) == 2
    # new_positions = step(map, new_positions)
    # assert new_positions == False

    # start from an actual position
    map = create_map(test_input)
    start_tile = find_start_in_map(map)
    new_positions = [start_tile]
    new_positions = step(map, new_positions)
    assert len(new_positions) == 2

    new_positions = step(map, new_positions)
    assert len(new_positions) == 4

    # new_positions = step(map, new_positions)
    # assert len(new_positions) == False


def test_find_tiles_for_steps():
    map = create_map(test_input)
    visited_tiles = find_tiles_for_steps(map, 6)
    assert len(visited_tiles) == 16


first_step = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

second_step = """
...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

third_step = """
...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........
"""
