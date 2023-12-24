import os
import copy

# a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).
# The beam enters in the top-left corner from the left and heading to the right. Then,
# its behavior depends on what it encounters as it moves:


# ".", "/" , "\", "|", "-"
# how many tiles end up being energized?


def create_map(input_txt):
    # temp replace escape char
    rows = input_txt.splitlines()

    tiles = []
    for row in rows:
        for char in row:
            tiles.append({"type": char, "visited": {"left": False, "right": False, "up": False, "down": False}})

    size = [int(len(tiles) / len(rows)), len(rows)]
    return {"size": size, "tiles": tiles}


def get_next_tile_loc(map, beam):
    curr_tile = beam["tile"]
    curr_direction = beam["direction"]

    next_tile_loc = None
    if curr_direction == "right":
        if curr_tile[0] + 1 < map["size"][0]:
            next_tile_loc = [curr_tile[0] + 1, curr_tile[1]]
    elif curr_direction == "left":
        if curr_tile[0] - 1 >= 0:
            next_tile_loc = [curr_tile[0] - 1, curr_tile[1]]
    elif curr_direction == "up":
        if curr_tile[1] - 1 >= 0:
            next_tile_loc = [curr_tile[0], curr_tile[1] - 1]
    elif curr_direction == "down":
        if curr_tile[1] + 1 < map["size"][1]:
            next_tile_loc = [curr_tile[0], curr_tile[1] + 1]

    return next_tile_loc


def move_beam(map, beam, beams):
    # check if we're processing a newly added beam
    # which has been already to the next location
    # if beam["added"]:
    #     beam["added"] = False
    #     return

    # get next tile
    next_tile_loc = get_next_tile_loc(map, beam)
    if next_tile_loc is None:
        beams.remove(beam)
        return

    next_row = next_tile_loc[1] * map["size"][0]
    next_location = int(next_row + next_tile_loc[0])
    next_tile = map["tiles"][next_location]

    if next_tile["visited"][beam["direction"]] is True:
        #    print(f"Removing beam from a visited tile {beam}, {next_tile} ")
        beams.remove(beam)
        return

    # move beam and mark next tile as visited
    beam["tile"] = next_tile_loc
    next_tile["visited"][beam["direction"]] = True
    # print("next_tile_loc", next_tile_loc, "next_tile", next_tile, map["tiles"][next_location])

    # process tile, e.g. updating beam position and direction, adding beams etc.
    next_tile_type = next_tile["type"]
    if next_tile_type == ".":
        # If the beam encounters empty space (.), it continues in the same direction.
        pass
    elif next_tile_type == "/":
        # If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on
        # the angle of the mirror.
        if beam["direction"] == "right":
            beam["direction"] = "up"
        elif beam["direction"] == "left":
            beam["direction"] = "down"
        elif beam["direction"] == "up":
            beam["direction"] = "right"
        elif beam["direction"] == "down":
            beam["direction"] = "left"
    elif next_tile_type == "{":  # \
        if beam["direction"] == "right":
            beam["direction"] = "down"
        elif beam["direction"] == "left":
            beam["direction"] = "up"
        elif beam["direction"] == "up":
            beam["direction"] = "left"
        elif beam["direction"] == "down":
            beam["direction"] = "right"
    elif next_tile_type == "|":
        # If the beam encounters the flat side of a splitter (| or -), the beam is split into two
        # beams going in each of the two directions the  splitter's pointy ends are pointing.

        if beam["direction"] == "right" or beam["direction"] == "left":
            beam["direction"] = "up"
            new_beam = {"direction": "down", "tile": next_tile_loc, "added": True}
            # new_beam_next_loc = get_next_tile_loc(map, new_beam)
            # if new_beam_next_loc is not None:
            #   new_beam["tile"] = new_beam_next_loc
            return new_beam
            # beams.append(new_beam)
    elif next_tile_type == "-":
        # If the beam encounters the flat side of a splitter (| or -), the beam is split into two
        # beams going in each of the two directions the  splitter's pointy ends are pointing.

        if beam["direction"] == "up" or beam["direction"] == "down":
            beam["direction"] = "left"
            new_beam = {"direction": "right", "tile": next_tile_loc, "added": True}
            return new_beam
            # print(f"adding new beam {next_tile_loc}")
            # new_beam_next_loc = get_next_tile_loc(map, new_beam)
            # if new_beam_next_loc is not None:
            #   new_beam["tile"] = new_beam_next_loc
        # beams.append({"direction": "right", "tile": next_tile_loc, "added": True})
        # beams.append({"direction": "right", "tile": next_tile_loc, "added": True})


def move_beams(map, beams):
    beam_len = len(beams)
    new_beams = []
    for i in range(beam_len - 1, -1, -1):
        beam = beams[i]
        new_beam = move_beam(map, beam, beams)
        if new_beam is not None:
            new_beams.append(new_beam)

    beams.extend(new_beams)
    return beams


def get_num_energized_tiles(map):
    visited_tiles = [tile for tile in map["tiles"] if any(list(tile["visited"].values()))]
    return len(visited_tiles)


def print_out_map(map):
    num_rows = int(map["size"][0])
    num_cols = int(map["size"][1])

    print("=== MAP ===")
    for i in range(0, num_rows):
        start = i * num_cols
        end = start + num_cols
        row_tiles = map["tiles"][start:end]

        row_str = ""
        for tile in row_tiles:
            if any(list(tile["visited"].values())):
                row_str += "#"
            else:
                row_str += "."
        print(row_str)


def calculate_num_energized_tiles(map, start_beam={"direction": "right", "tile": [-1, 0], "added": False}):
    beams = [start_beam]

    while len(beams) > 0:
        beam_len = len(beams)
        new_beams = []
        for i in range(beam_len - 1, -1, -1):
            beam = beams[i]
            new_beam = move_beam(map, beam, beams)
            if new_beam is not None:
                new_beams.append(new_beam)

        beams.extend(new_beams)

    print_out_map(map)

    return get_num_energized_tiles(map)


def get_all_start_beams(map):
    start_beams = []

    # from right and left
    for i in range(0, map["size"][1]):
        start_beams.append({"direction": "right", "tile": [-1, i], "added": False})
        start_beams.append({"direction": "left", "tile": [map["size"][0], i], "added": False})

    # from top and bottom
    for i in range(0, map["size"][0]):
        start_beams.append({"direction": "down", "tile": [i, -1], "added": False})
        start_beams.append({"direction": "up", "tile": [i, map["size"][1]], "added": False})

    return start_beams


def calculate_max_num_tiles_energized(map):
    # get all possible beams
    start_beams = get_all_start_beams(map)

    num_tiles = []
    for start_beam in start_beams:
        map = create_map(input_text)
        num_tiles.append(calculate_num_energized_tiles(map, start_beam))

    return max(num_tiles)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_16_input.txt").read()
    map = create_map(input_text)
    print(f"Part 1: {calculate_num_energized_tiles(map)}")

    # PART 2
    print(f"Part 2: {calculate_max_num_tiles_energized(map)}")
