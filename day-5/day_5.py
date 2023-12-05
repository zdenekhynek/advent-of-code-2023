"""
The almanac (your puzzle input) lists
- all of the seeds that need to be planted
- it also lists what type of soil to use with each kind of seed
- what type of fertilizer to use with each kind of soil
- what type of water to use with  each kind of fertilizer, and so on.

Every type of seed, soil, fertilizer and so on is identified with a number,  but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related  to each other.

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.
"""
import os
import tqdm


def single_map_value(value, map):
    # outside of mapping cases first
    if value < map["s_start"] or value >= map["s_start"] + map["range"]:
        return value
    else:
        s_offset = value - map["s_start"]
        return map["d_start"] + s_offset


def single_map_value_range(value_range, map):
    (start, end, range) = value_range

    if end < map["s_start"]:
        # range to map is before mapping range
        # and is not getting transformed
        return (start, end, range)
    elif start > map["s_start"] + map["range"]:
        # range to map is after mapping range
        # and is not getting transformed
        return (start, end, range)
    else:
        # range needs to be remapped
        # do we need to worry about splitting the range
        mapped_start = single_map_value(start, map)
        mappend_end = single_map_value(end, map)
        return (mapped_start, mappend_end, range)

        # if start < map["s_start"] or end >= map["s_start"] + map["range"]:
        # pass


def map_value(value, maps):
    mapped_value = value
    for map in maps:
        og_value = mapped_value
        if isinstance(value, tuple):
            mapped_value = single_map_value_range(mapped_value, map)
        else:
            mapped_value = single_map_value(mapped_value, map)
        if og_value != mapped_value:
            break

    return mapped_value


def parse_txt_to_single_map(txt):
    [d_start, s_start, range] = txt.split(" ")
    return {"d_start": int(d_start), "s_start": int(s_start), "range": int(range)}


def get_map_categories_from_txt(txt):
    categories = []

    for map_section in txt.split("\n\n"):
        lines = map_section.splitlines()
        map_name = lines[0]
        maps_text = lines[1:]
        maps = [parse_txt_to_single_map(map_txt) for map_txt in maps_text]
        categories.append({"name": map_name, "maps": maps})

    return categories


def get_seeds_id(txt, is_range=False):
    first_line = txt.splitlines()[0]
    seed_numbers = [int(i_str) for i_str in first_line.split(": ")[1].split(" ")]

    if not is_range:
        return seed_numbers
    else:
        range_seed_numbers = []
        range_start = None
        for index, seed_number in enumerate(seed_numbers):
            if index % 2 == 0:
                range_start = seed_number
            else:
                range_end = range_start + seed_number
                range_seed_numbers.append((range_start, range_end, seed_number))
                # range_seed_numbers.extend(list(range(range_start, range_end)))
        return range_seed_numbers


def get_map_text(txt):
    map_lines = txt.splitlines()[2:]
    return "\n".join(map_lines)


def get_location_for_seed(seed, categories):
    mapped_value = seed

    for category in categories:
        # og_value = mapped_value
        if isinstance(seed, tuple):
            mapped_value = map_value(mapped_value, category["maps"])
        elif isinstance(seed, int):
            mapped_value = map_value(mapped_value, category["maps"])
        # print(f"Mapping {og_value} to {mapped_value} for {category['name']}.")

    return mapped_value


def get_lowest_location_number(txt):
    categories = get_map_categories_from_txt(txt)
    seeds = get_seeds_id(txt)

    locations = [get_location_for_seed(seed, categories) for seed in seeds]
    return min(locations)


def get_lowest_location_number_for_seed_range(txt):
    categories = get_map_categories_from_txt(txt)
    seeds = get_seeds_id(txt, True)
    print(f"Running for: {len(seeds)} seeds.")

    locations = [get_location_for_seed(seed, categories) for seed in tqdm.tqdm(seeds)]
    print(locations)
    return min(locations)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_5_input.txt").read()
    print(f"Part 1: {get_lowest_location_number(input_text)}")

    # PART 2
    print(f"Part 2: {get_lowest_location_number_for_seed_range(input_text)}")
