import os

# which garden plots he can reach with exactly his remaining 64 steps
# He gives you an up-to-date map (your puzzle input) of
# his starting position (S), garden plots (.), and rocks (#)


def create_map(input_txt):
    map = []
    lines = [line for line in input_txt.splitlines() if line is not ""]
    for row, line in enumerate(lines):
        map.append([])
        for col, tile in enumerate(line):
            map[row].append({"x": col, "y": row, "type": tile, "visited": False})

    return map


def get_position_in_direction(direction, position):
    if direction == "N":
        return {"x": position["x"], "y": position["y"] - 1}
    elif direction == "S":
        return {"x": position["x"], "y": position["y"] + 1}
    elif direction == "E":
        return {"x": position["x"] + 1, "y": position["y"]}
    elif direction == "W":
        return {"x": position["x"] - 1, "y": position["y"]}


def step_from_position(map, position):
    """
    He can take one step north, south, east, or west,
    but only onto tiles that are garden plots.
    """
    new_positions = []

    directions = ["N", "E", "S", "W"]

    for direction in directions:
        new_position = get_position_in_direction(direction, position)

        # check if tile exists and if it does,
        # if it's not visited already and is not out of bounds
        x_in_bounds = new_position["x"] > -1 and new_position["x"] < len(map[0])
        y_in_bounds = new_position["y"] > -1 and new_position["y"] < len(map)
        if x_in_bounds and y_in_bounds:
            new_tile = map[new_position["y"]][new_position["x"]]
            # if new_tile["visited"] == False:
            if new_tile["type"] is not "#":  # and new_tile["type"] is not "S":
                new_tile["visited"] = True
                new_positions.append({"x": new_tile["x"], "y": new_tile["y"]})

    return new_positions


def visualise_map(map, positions):
    positions_lookup = {f'{pos["x"]}_{pos["y"]}': True for pos in positions}

    for y, col in enumerate(map):
        for x, _ in enumerate(col):
            # tile = map[x][y]
            # if tile["visited"] == True:
            if f"{x}_{y}" in positions_lookup:
                # print("printing", x, y)
                print("O", end="")
            else:
                print(map[x][y]["type"], end="")
        print("\n", end="")


def step(map, positions):
    """ """

    print("STEP")
    new_positions = {}
    for position in positions:
        positions_from_step = step_from_position(map, position)
        # use set to avoid duplication
        for pos in positions_from_step:
            new_positions[f'{pos["x"]}_{pos["y"]}'] = pos

    #print(f"new positions:{new_positions}")
    visualise_map(map, new_positions.values())

    return new_positions.values()


def find_start_in_map(map):
    start_tile = None
    for y, row in enumerate(map):
        for x, _ in enumerate(row):
            tile = map[y][x]
            if tile["type"] == "S":
                start_tile = tile

    return start_tile


def find_tiles_for_steps(map, num_steps=64):
    """
    Starting from the garden plot marked S on your map,
    how many garden plots could the Elf reach in exactly 64 steps?
    """

    positions = [find_start_in_map(map)]

    for i in range(num_steps):
        positions = step(map, positions)
        # visualise_map(map, positions)

    return positions

    # get number of visited tiles
    # visited_tiles = []
    # for y, row in enumerate(map):
    #     for x, _ in enumerate(row):
    #         tile = map[y][x]
    #         if tile["visited"]:
    #             visited_tiles.append(tile)

    # return visited_tiles


def part_1(input_txt):
    map = create_map(input_txt)
    visited_tiles = find_tiles_for_steps(map, 64)
    return len(visited_tiles)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_txt = open(f"{working_dir}/day_21_input.txt").read()
    print(part_1(input_txt))

    # PART 2
