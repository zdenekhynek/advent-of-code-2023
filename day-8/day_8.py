import os
from collections import OrderedDict

"""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

# lookup to easily access points
# iterate over the list of points
# while increasing the step index to get the instruction


def get_instruction_list_from_text(txt):
    return txt.splitlines()[0].strip()


def get_nodes_from_text(txt):
    node_lines = txt.splitlines()[2:]
    nodes = OrderedDict()
    for line in node_lines:
        node_key, edges = line.split(" = ")
        edges = edges.replace("(", "").replace(")", "")
        edges_l = edges.split(", ")

        if node_key in nodes:
            raise Exception(f"Node {node_key} already exists")

        nodes[node_key] = {"L": edges_l[0], "R": edges_l[1]}
    return nodes


def get_number_of_steps(input_txt):
    instructions = get_instruction_list_from_text(input_txt)
    nodes = get_nodes_from_text(input_txt)

    counts = {}
    step = 0
    curr_node_key = "AAA"
    while curr_node_key != "ZZZ":
        direction = instructions[step % len(instructions)]
        curr_node_key = nodes[curr_node_key][direction]
        step += 1

        if curr_node_key not in counts:
            counts[curr_node_key] = 1
        else:
            counts[curr_node_key] += 1

        if step % 10000000 == 0:
            print(counts, len(counts.keys()))

    return step


def get_simultaneous_number_of_steps(input_txt):
    instructions = get_instruction_list_from_text(input_txt)
    nodes = get_nodes_from_text(input_txt)

    # find starting nodes
    curr_node_keys = [key for key in nodes.keys() if key.endswith("A")]
    print(curr_node_keys)
    counts = {}
    step = 0
    # curr_node_key = "AAA"
    while not all([key.endswith("Z") for key in curr_node_keys]):
        direction = instructions[step % len(instructions)]

        # should_log = "ZZZ" in nodes[curr_node_key].values()
        # if should_log:
        #   print(f"Step {step}: direction: {direction}: {curr_node_key} -> {nodes[curr_node_key][direction]}")

        curr_node_keys = [nodes[key][direction] for key in curr_node_keys]
        step += 1

        for curr_node_key in curr_node_keys:
            if curr_node_key not in counts:
                counts[curr_node_key] = 1
            else:
                counts[curr_node_key] += 1

        if step % 1000000 == 0:
            # print(step, curr_node_keys)
            print(counts, len(counts.keys()))

    return step


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_8_input.txt").read()
    print(f"Part 1: {get_number_of_steps(input_text)}")

    print(f"Part 2: {get_simultaneous_number_of_steps(input_text)}")
