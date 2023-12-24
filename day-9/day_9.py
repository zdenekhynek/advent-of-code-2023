import os

# your environmental report should include a prediction of the next value
# in each history.
# making a new sequence from the difference at each step of your history.
# if that sequence not all zeroes, use that as an input until you get
# Once all of the values in your latest sequence are zeroes,
# you can extrapolate what the next value of the original history
# should be.

# the first history is 0 3 6 9 12 15.
# the first sequence of differences will be 3 3 3 3 3
# the values differ by 0 at each step, so the next sequence is 0 0 0 0


def parse_txt_into_sequences(input_txt):
    sequences = []
    for line in input_txt.splitlines():
        int_strings = line.split(" ")
        sequences.append([int(x) for x in int_strings])
    return sequences


def get_sequence_diffs(sequence):
    diffs = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i + 1] - sequence[i])
    return diffs


def extrapolate_sequence(sequence, diff_sequence, fill_prev_value=False):
    new_sequence = sequence.copy()

    if fill_prev_value:
        new_sequence.insert(0, sequence[0] - diff_sequence[0])
    else:
        new_sequence.append(diff_sequence[-1] + sequence[-1])
    return new_sequence


def get_extrapolate_value(sequence, fill_prev_value=False):
    diff_sequence = get_sequence_diffs(sequence)

    diff_sequences = [diff_sequence]

    # get diff sequences until we get zero
    while not all([x == 0 for x in diff_sequence]):
        diff_sequence = get_sequence_diffs(diff_sequence)
        diff_sequences.append(diff_sequence)

    diff_sequences.reverse()
    diff_sequences.append(sequence)

    last_sequence = diff_sequences.pop(0)
    for diff_sequence in diff_sequences:
        last_sequence = extrapolate_sequence(diff_sequence, last_sequence, fill_prev_value)

    return last_sequence[0] if fill_prev_value else last_sequence[-1]


def get_sum_of_next_values(input_txt, fill_prev_value=False):
    sequences = parse_txt_into_sequences(input_txt)

    extrapolated_values = []
    for sequence in sequences:
        extrapolated_values.append(get_extrapolate_value(sequence, fill_prev_value))

    return sum(extrapolated_values)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_9_input.txt").read()
    print(f"Part 1: {get_sum_of_next_values(input_text)}")

    # PART 2
    print(f"Part 2: {get_sum_of_next_values(input_text, True)}")
