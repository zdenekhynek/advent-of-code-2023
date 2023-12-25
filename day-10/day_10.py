import os


def create_map_from_txt(input_txt):
    lines = input_txt.splitlines()

    cells = []
    for y, line in enumerate(lines):
        cells.append([])
        for x, char in enumerate(line):
            cells[y].append({"x": x, "y": y, "char": char})

    return {"cells": cells, "size": (len(lines[0]), len(lines))}


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this
def get_connected_tile_coords(tile, map):
    connected_tiles = []
    if tile["char"] == "|":
        connected_tiles.append({"x": tile["x"], "y": tile["y"] - 1})
        connected_tiles.append({"x": tile["x"], "y": tile["y"] + 1})
    elif tile["char"] == "-":
        connected_tiles.append({"x": tile["x"] - 1, "y": tile["y"]})
        connected_tiles.append({"x": tile["x"] + 1, "y": tile["y"]})
    elif tile["char"] == "L":
        connected_tiles.append({"x": tile["x"] + 1, "y": tile["y"]})
        connected_tiles.append({"x": tile["x"], "y": tile["y"] - 1})
    elif tile["char"] == "J":
        connected_tiles.append({"x": tile["x"] - 1, "y": tile["y"]})
        connected_tiles.append({"x": tile["x"], "y": tile["y"] - 1})
    elif tile["char"] == "7":
        connected_tiles.append({"x": tile["x"] - 1, "y": tile["y"]})
        connected_tiles.append({"x": tile["x"], "y": tile["y"] + 1})
    elif tile["char"] == "F":
        connected_tiles.append({"x": tile["x"] + 1, "y": tile["y"]})
        connected_tiles.append({"x": tile["x"], "y": tile["y"] + 1})

    validated_connected_tiles = [
        tile
        for tile in connected_tiles
        if tile["x"] >= 0 and tile["y"] >= 0 and tile["x"] < map["size"][0] and tile["y"] < map["size"][1]
    ]
    return validated_connected_tiles


def move(tile, path, map):
    # every tile has at most two
    # get possible next tiles, should be two max
    possible_tile_coords = get_connected_tile_coords(tile, map)
    possible_tiles = [map["cells"][tile["y"]][tile["x"]] for tile in possible_tile_coords]

    # pick the one which we haven't came from
    next_tile = None
    for possible_tile in possible_tiles:
        if possible_tile not in path:
            next_tile = possible_tile
            break

    return next_tile


def follow_path(start_tile, initial_tile, map):
    curr_tile = initial_tile
    path = [start_tile, curr_tile]

    while curr_tile is not None and curr_tile is not start_tile:
        if curr_tile["char"] == ".":
            break

        curr_tile = move(curr_tile, path, map)
        if curr_tile is not None and curr_tile not in path:
            path.append(curr_tile)

        # check if it has been visited before
    return path


def find_start_tile(map):
    for y, line in enumerate(map["cells"]):
        for x, cell in enumerate(line):
            if cell["char"] == "S":
                return {"x": x, "y": y, "char": "S"}


def get_cell_neighbors(cell, map):
    neighbors = []
    x = cell["x"]
    y = cell["y"]

    if (y - 1) >= 0:
        neighbor = map["cells"][y - 1][x]
        if neighbor["char"] in ["7", "F", "|"]:
            neighbors.append(neighbor)

    if (x - 1) >= 0:
        neighbor = map["cells"][y][x - 1]
        if neighbor["char"] in ["L", "F", "-"]:
            neighbors.append(neighbor)
    if (x + 1) < map["size"][0]:
        neighbor = map["cells"][y][x + 1]
        if neighbor["char"] in ["7", "J", "-"]:
            neighbors.append(neighbor)

    if (y + 1) < map["size"][1]:
        neighbor = map["cells"][y + 1][x]
        if neighbor["char"] in ["|", "J", "L"]:
            neighbors.append(neighbor)

    return neighbors


def get_paths_from_start_point(map):
    # find the start tile
    start_tile = find_start_tile(map)

    if start_tile:
        # for each neighbour of the start tile, try to follow path
        start_neighbors = get_cell_neighbors(start_tile, map)

        viable_paths = []
        for neighbor in start_neighbors:
            path = follow_path(start_tile, neighbor, map)
            if path is not None:
                if len(path) > 4 and path[-1] in start_neighbors:
                    viable_paths.append(path)

        # there should be two identical viable paths?
        return viable_paths[0]


def get_furthest_tile_from_start(input_txt):
    map = create_map_from_txt(input_txt)
    path = get_paths_from_start_point(map)
    return len(path) / 2


def cast_from_tile(tile, path, map, direction, num_crosses=0):
    if tile in path:
        num_crosses += 1

    # cast north
    if direction == "N":
        if tile["y"] > 0:
            tile = map["cells"][tile["y"] - 1][tile["x"]]
        else:
            return num_crosses
    elif direction == "E":
        if tile["x"] > 0:
            tile = map["cells"][tile["y"]][tile["x"] - 1]
        else:
            return num_crosses
    elif direction == "S":
        if tile["y"] < map["size"][1] - 1:
            tile = map["cells"][tile["y"] + 1][tile["x"]]
        else:
            return num_crosses
    elif direction == "W":
        if tile["x"] < map["size"][0] - 1:
            tile = map["cells"][tile["y"]][tile["x"] + 1]
        else:
            return num_crosses

    return cast_from_tile(tile, path, map, direction, num_crosses)


def is_nested_tile(tile, path, map):
    # raycasting
    if tile in path:
        return False

    directions = ["N", "E", "S", "W"]
    num_direction_crosses = [cast_from_tile(tile, path, map, direction) for direction in directions]
    return all([num % 2 == 1 for num in num_direction_crosses])


def get_nested_tiles(map):
    path = get_paths_from_start_point(map)

    nested_tiles = []
    for cell_row in map["cells"]:
        for cell in cell_row:
          is_nested = is_nested_tile(cell, path, map)
          if is_nested:
              nested_tiles.append(cell)

    return nested_tiles


def get_num_of_nested_tiles(input_txt):
    map = create_map_from_txt(input_txt)
    nested_cells = get_nested_tiles(map)
    return len(nested_cells)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_10_input.txt").read()
    # print(f"Part 1: {get_furthest_tile_from_start(input_text)}")

    # PART 2
    print(f"Part 2: {get_num_of_nested_tiles(input_text)}")
