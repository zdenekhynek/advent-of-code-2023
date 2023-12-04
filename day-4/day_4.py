import os
import re


def parse_numbers_set_txt(numbers_txt):
    pattern = "\d+"
    return [int(match) for match in re.findall(pattern, numbers_txt)]


def parse_card_text(line_text):
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    numbers_txt = line_text.split(": ")[1]
    [winning_set_txt, chosen_set_txt] = numbers_txt.split(" | ")
    # card_text = [card.split(" ") for card in card_text]
    return [parse_numbers_set_txt(winning_set_txt), parse_numbers_set_txt(chosen_set_txt)]


def find_winning_numbers(winning_set, chosen_set):
    """
    card 1 has five winning numbers (41, 48, 83, 86, and 17)
    and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53).
    Of the numbers you have, four of them (48, 83, 17, and 86)
    are winning numbers! That means card 1 is worth 8 points
    (1 for the first match, then doubled three times for each of
    the three matches after the first).
    """
    winning_numbers = []
    for number in chosen_set:
        if number in winning_set:
            winning_numbers.append(number)
    return winning_numbers


def get_card_score(winning_numbers):
    score = 0
    for i in range(len(winning_numbers)):
        if i == 0:
            score += 1
        else:
            score *= 2
    return score


def get_cards_score(cards_text):
    cards = [parse_card_text(line) for line in cards_text.split("\n")]
    scores = [get_card_score(find_winning_numbers(card[0], card[1])) for card in cards]
    return sum(scores)


def get_total_scratchcards(cards_text):
    cards = [parse_card_text(line) for line in cards_text.split("\n")]

    cards_number = 0

    # So, if you win a copy of card 10 and it has 5 matching numbers,
    # it would then win a copy of the same cards that the original
    # card 10 won: cards 11, 12, 13, 14, and 15. This process repeats
    # until none of the copies cause you to win any more cards.

    curr_index = 0
    card_queue = [(curr_index, cards[0])]
    while len(card_queue) > 0:
        (card_index, card) = card_queue.pop(0)
        cards_number += 1
        winning_numbers = find_winning_numbers(card[0], card[1])

        queue_index = card_index + 1
        cards_to_queue = cards[queue_index : queue_index + len(winning_numbers)]
        # print(f"Popped card {card_index}, queue index: {queue_index}, queue length: {len(card_queue)}, adding: {len(winning_numbers)}")

        for card_to_queue in cards_to_queue:
            card_queue.append((queue_index, card_to_queue))
            queue_index += 1

        if len(card_queue) == 0 and curr_index < len(cards) - 1:
            curr_index += 1
            card_queue.append((curr_index, cards[curr_index]))
            print(f"Adding card {curr_index} to queue {len(card_queue)}")

    return cards_number


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_4_input.txt").read()
    print(f"Part 1: {get_cards_score(input_text)}")

    # PART 2
    print(f"Part 2: {get_total_scratchcards(input_text)}")
