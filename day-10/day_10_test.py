from day_10 import (
    get_cell_neighbors,
    get_connected_tile_coords,
    find_start_tile,
    create_map_from_txt,
    move,
    follow_path,
    get_paths_from_start_point,
    get_furthest_tile_from_start,
)


test_input = """.....
.S-7.
.|.|.
.L-J.
.....
"""

test_input2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

test_input3 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF


[
    [{'x': 1, 'y': 1, 'char': 'S'}, {'x': 1, 'y': 0, 'char': 'L'}, {'x': 2, 'y': 0, 'char': '|'}, {'x': 2, 'y': 1, 'char': '-'}, {'x': 3, 'y': 1, 'char': '7'}, {'x': 3, 'y': 2, 'char': '|'}, {'x': 3, 'y': 3, 'char': 'J'}, {'x': 2, 'y': 3, 'char': '-'}, {'x': 1, 'y': 3, 'char': 'L'}, {'x': 1, 'y': 2, 'char': '|'}]
    ,
    [{'x': 1, 'y': 1, 'char': 'S'}, {'x': 0, 'y': 1, 'char': '7'}, {'x': 0, 'y': 2, 'char': 'L'}, {'x': 1, 'y': 2, 'char': '|'}, {'x': 1, 'y': 3, 'char': 'L'}, {'x': 2, 'y': 3, 'char': '-'}, {'x': 3, 'y': 3, 'char': 'J'}, {'x': 3, 'y': 2, 'char': '|'}, {'x': 3, 'y': 1, 'char': '7'}, {'x': 2, 'y': 1, 'char': '-'}],
    [{'x': 1, 'y': 1, 'char': 'S'}, {'x': 2, 'y': 1, 'char': '-'}, {'x': 3, 'y': 1, 'char': '7'}, {'x': 3, 'y': 2, 'char': '|'}, {'x': 3, 'y': 3, 'char': 'J'}, {'x': 2, 'y': 3, 'char': '-'}, {'x': 1, 'y': 3, 'char': 'L'}, {'x': 1, 'y': 2, 'char': '|'}],
    [{'x': 1, 'y': 1, 'char': 'S'}, {'x': 1, 'y': 2, 'char': '|'}, {'x': 1, 'y': 3, 'char': 'L'}, {'x': 2, 'y': 3, 'char': '-'}, {'x': 3, 'y': 3, 'char': 'J'}, {'x': 3, 'y': 2, 'char': '|'}, {'x': 3, 'y': 1, 'char': '7'}, {'x': 2, 'y': 1, 'char': '-'}]
]

def test_create_map_from_txt():
    map = create_map_from_txt(test_input)
    assert map["size"] == (5, 5)
    assert map["cells"][0][0] == {"x": 0, "y": 0, "char": "."}
    assert map["cells"][1][2] == {"x": 2, "y": 1, "char": "-"}


def test_find_start_tile():
    map = create_map_from_txt(test_input)
    start_tile = find_start_tile(map)
    assert start_tile["x"] == 1
    assert start_tile["y"] == 1
    assert start_tile["char"] == "S"


def test_get_connected_tile_coords():
    map = create_map_from_txt(test_input)
    assert get_connected_tile_coords(map["cells"][1][2], map) == [{"x": 1, "y": 1}, {"x": 3, "y": 1}]
    assert get_connected_tile_coords(map["cells"][1][3], map) == [{"x": 2, "y": 1}, {"x": 3, "y": 2}]


def test_move():
    map = create_map_from_txt(test_input)
    start_tile = find_start_tile(map)
    path = [start_tile, map["cells"][1][2]]
    moved = move(path[1], path, map)
    assert moved == {"x": 3, "y": 1, "char": "7"}
    path.append(moved)
    moved = move(moved, path, map)
    assert moved == {"x": 3, "y": 2, "char": "|"}
    path.append(moved)
    moved = move(moved, path, map)
    assert moved == {"x": 3, "y": 3, "char": "J"}
    path.append(moved)
    moved = move(moved, path, map)
    assert moved == {"x": 2, "y": 3, "char": "-"}

    # test move on "."
    path = []
    moved = move(map["cells"][0][1], path, map)
    assert moved == None

    # test move on "F"
    map2 = create_map_from_txt(test_input2)
    path = []
    moved = move(map2["cells"][1][1], path, map2)
    assert moved == {"x": 2, "y": 1, "char": "J"}


def test_follow_path():
    map = create_map_from_txt(test_input)
    start_tile = find_start_tile(map)
    initial_tile = map["cells"][start_tile["y"]][start_tile["x"] + 1]
    path = follow_path(start_tile, initial_tile, map)

    assert len(path) == 8
    assert path[-1] == {"x": 1, "y": 2, "char": "|"}


def test_get_cell_neighbors():
    map = create_map_from_txt(test_input)
    start_tile = find_start_tile(map)
    neighbors = get_cell_neighbors(start_tile, map)

    assert len(neighbors) == 2
    assert neighbors[0] == {"x": 2, "y": 1, "char": "-"}


def test_get_paths_from_start_point():
    map = create_map_from_txt(test_input)
    path = get_paths_from_start_point(map)
    assert len(path) == 8


def test_get_furthest_tile_from_start():
    # assert get_furthest_tile_from_start(test_input) == 4
    # assert get_furthest_tile_from_start(test_input2) == 8
    assert get_furthest_tile_from_start(test_input3) == 4
