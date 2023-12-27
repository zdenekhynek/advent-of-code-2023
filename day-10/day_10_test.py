from day_10 import (
    get_cell_neighbors,
    get_connected_tile_coords,
    find_start_tile,
    create_map_from_txt,
    move,
    follow_path,
    get_paths_from_start_point,
    get_furthest_tile_from_start,
    cast_from_tile,
    is_nested_tile,
    get_nested_tiles,
    get_num_of_nested_tiles,
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
    [
        {"x": 1, "y": 1, "char": "S"},
        {"x": 1, "y": 0, "char": "L"},
        {"x": 2, "y": 0, "char": "|"},
        {"x": 2, "y": 1, "char": "-"},
        {"x": 3, "y": 1, "char": "7"},
        {"x": 3, "y": 2, "char": "|"},
        {"x": 3, "y": 3, "char": "J"},
        {"x": 2, "y": 3, "char": "-"},
        {"x": 1, "y": 3, "char": "L"},
        {"x": 1, "y": 2, "char": "|"},
    ],
    [
        {"x": 1, "y": 1, "char": "S"},
        {"x": 0, "y": 1, "char": "7"},
        {"x": 0, "y": 2, "char": "L"},
        {"x": 1, "y": 2, "char": "|"},
        {"x": 1, "y": 3, "char": "L"},
        {"x": 2, "y": 3, "char": "-"},
        {"x": 3, "y": 3, "char": "J"},
        {"x": 3, "y": 2, "char": "|"},
        {"x": 3, "y": 1, "char": "7"},
        {"x": 2, "y": 1, "char": "-"},
    ],
    [
        {"x": 1, "y": 1, "char": "S"},
        {"x": 2, "y": 1, "char": "-"},
        {"x": 3, "y": 1, "char": "7"},
        {"x": 3, "y": 2, "char": "|"},
        {"x": 3, "y": 3, "char": "J"},
        {"x": 2, "y": 3, "char": "-"},
        {"x": 1, "y": 3, "char": "L"},
        {"x": 1, "y": 2, "char": "|"},
    ],
    [
        {"x": 1, "y": 1, "char": "S"},
        {"x": 1, "y": 2, "char": "|"},
        {"x": 1, "y": 3, "char": "L"},
        {"x": 2, "y": 3, "char": "-"},
        {"x": 3, "y": 3, "char": "J"},
        {"x": 3, "y": 2, "char": "|"},
        {"x": 3, "y": 1, "char": "7"},
        {"x": 2, "y": 1, "char": "-"},
    ],
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
    assert get_furthest_tile_from_start(test_input) == 4
    assert get_furthest_tile_from_start(test_input2) == 8
    assert get_furthest_tile_from_start(test_input3) == 4


def test_cast_from_tile():
    map = create_map_from_txt(test_input)
    path = get_paths_from_start_point(map)
    assert cast_from_tile(map["cells"][2][2], path, map, "N") == 1
    assert cast_from_tile(map["cells"][2][2], path, map, "S") == 1
    assert cast_from_tile(map["cells"][2][2], path, map, "E") == 1
    assert cast_from_tile(map["cells"][2][2], path, map, "W") == 1


def test_is_nested_tile():
    map = create_map_from_txt(test_input)
    path = get_paths_from_start_point(map)
    assert is_nested_tile(map["cells"][2][2], path, map) == True
    assert is_nested_tile(map["cells"][2][1], path, map) == False
    assert is_nested_tile(map["cells"][0][1], path, map) == False


def test_get_nested_tiles():
    map = create_map_from_txt(test_input)
    assert len(get_nested_tiles(map)[0]) == 1


test_part2_input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

test_part2_input2 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

"""
0F----7F7F7F7F-70000
0|F--7||||||||FJ0000
0||0FJ||||||||L70000
FJL7L7LJLJ||LJIL-700
L--J0L7IIILJS7F-7L70
0000F-JIIF7FJ|L7L7L7
IIIIL70F7||L7|IL7L7|
00000|FJLJ|FJ|F7|0LJ
0000FJL-70||0||||000
0000L---J0LJ0LJLJ000
"""

test_part2_input3 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

def test_get_num_of_nested_tiles():
    assert get_num_of_nested_tiles(test_input) == 1
    assert get_num_of_nested_tiles(test_part2_input) == 4
    assert get_num_of_nested_tiles(test_part2_input2) == 8
    assert get_num_of_nested_tiles(test_part2_input3) == 10
