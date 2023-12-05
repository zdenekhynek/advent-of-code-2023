from day_5 import (
    single_map_value,
    single_map_value_range,
    map_value,
    get_map_text,
    get_seeds_id,
    get_map_categories_from_txt,
    get_location_for_seed,
    get_lowest_location_number,
    get_lowest_location_number_for_seed_range,
)

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_single_map_value():
    single_map = {"d_start": 50, "s_start": 98, "range": 2}
    assert single_map_value(49, single_map) == 49
    assert single_map_value(98, single_map) == 50
    assert single_map_value(99, single_map) == 51
    assert single_map_value(100, single_map) == 100

    fertilize_map = {"d_start": 49, "s_start": 53, "range": 8}
    assert single_map_value(53, fertilize_map) == 49

def test_single_map_value_range():
    single_map = {"d_start": 50, "s_start": 98, "range": 2}
    assert single_map_value_range((49, 50, 2), single_map) == (49, 50, 2)
    assert single_map_value_range((101, 102, 2), single_map) == (101, 102, 2)
    assert single_map_value_range((98, 99, 2), single_map) == (50, 51, 2)

def test_map_value():
    maps = [{"d_start": 50, "s_start": 98, "range": 2}, {"d_start": 52, "s_start": 50, "range": 48}]
    
    assert map_value(79, maps) == 81
    assert map_value(14, maps) == 14
    assert map_value(55, maps) == 57
    assert map_value(13, maps) == 13

    maps = [
       {'d_start': 49, 's_start': 53, 'range': 8},
       {'d_start': 0, 's_start': 11, 'range': 42},
       {'d_start': 42, 's_start': 0, 'range': 7},
       {'d_start': 57, 's_start': 7, 'range': 4},
    ]
    assert map_value(53, maps) == 49


def test_get_map_text():
    assert get_map_text(test_input).startswith("seed-to-soil map:") == True


def test_get_seeds_id():
    assert get_seeds_id(test_input) == [79, 14, 55, 13]
    assert get_seeds_id("seeds: 1 2 5 2", True) == [(1, 3, 2), (5, 7, 2)]
    assert get_seeds_id(test_input, True) == [(79, 93, 14), (55, 68, 13)]


def test_get_map_categories_from_txt():
    categories = get_map_categories_from_txt(get_map_text(test_input))
    assert len(categories) == 7
    assert categories[0]["name"] == "seed-to-soil map:"
    assert len(categories[0]["maps"]) == 2
    assert categories[0]["maps"][0] == {"d_start": 50, "s_start": 98, "range": 2}
    assert categories[0]["maps"][1] == {"d_start": 52, "s_start": 50, "range": 48}

    assert categories[2]["name"] == "fertilizer-to-water map:"
    assert len(categories[2]["maps"]) == 4
    assert categories[2]["maps"][2] == {"d_start": 42, "s_start": 0, "range": 7}
    assert categories[2]["maps"][3] == {"d_start": 57, "s_start": 7, "range": 4}


def test_get_location_for_seed():
    categories = get_map_categories_from_txt(get_map_text(test_input))
    assert get_location_for_seed(79, categories) == 82
    assert get_location_for_seed(14, categories) == 43
    assert get_location_for_seed(55, categories) == 86
    assert get_location_for_seed(13, categories) == 35

def test_get_lowest_location_number():
    assert get_lowest_location_number(test_input) == 35

def test_get_lowest_location_number_for_seed_range():
    assert get_lowest_location_number_for_seed_range(test_input) == 46