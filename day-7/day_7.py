# A hand consists of five cards labeled one of
# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
# A is the highest and 2 is the lowest.


# secondary ordering: 33332 and 2AAAA are both four of a kind hands, but
# 33332 is stronger because its first card is stronger. Similarly, 77888
# and 77788 are both a full house, but 77888 is stronger because its third
# card is stronger (and both hands have the same first and second card).

import os


def get_card_score(card):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    int_score = len(cards) - cards.index(card)
    str_score = str(int_score).rjust(2, "0")
    return str_score


def get_secondary_hand_score(cards):
    numeric_decimals = "".join([get_card_score(card) for card in cards])
    return float(f"0.{numeric_decimals}")


def group_hand_cards(hand):
    group_cards = {}
    for card in hand:
        if card in group_cards:
            group_cards[card] += 1
        else:
            group_cards[card] = 1
    return group_cards


def get_hand_score(hand):
    group_cards = group_hand_cards(hand)

    # if J is in the hand, we can change it to something
    # that gets better score
    if "J" in hand:
        group_cards_copy = group_cards.copy()
        del group_cards_copy["J"]
        
        if bool(group_cards_copy) is not False:
          most_common_card = max(group_cards_copy, key=group_cards.get)
          hand = hand.replace("J", most_common_card)
          group_cards = group_hand_cards(hand)

    # 6 - Five of a kind, where all five cards have the same label: AAAAA
    if max(group_cards.values()) == 5:
        return 6
    # 5 - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if max(group_cards.values()) == 4:
        return 5
    # 4 - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    if 3 in group_cards.values() and 2 in group_cards.values():
        return 4
    # 3 - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    if 3 in group_cards.values():
        return 3
    # 2 - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if list(group_cards.values()).count(2) == 2:
        return 2
    # 1 - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if 2 in group_cards.values():
        return 1

    # 0 - High card, where all cards' labels are distinct: 23456
    return 0


def get_total_hand_score(hand):
    return get_hand_score(hand) + get_secondary_hand_score(hand)


def parse_hands(hands_txt):
    hands_lines = hands_txt.split("\n")
    hands = [hand_line.split(" ") for hand_line in hands_lines]
    return [{"hand": hand[0], "bet": hand[1]} for hand in hands]


def sort_hands(hands):
    sorted_hands = sorted(hands, key=lambda hand: hand["score"])
    sorted_hands.reverse()
    return sorted_hands


def compute_rank_hands(hands):
    for hand in hands:
        hand["score"] = get_total_hand_score(hand["hand"])

    sorted_hands = sort_hands(hands)

    # add rank
    for hand in sorted_hands:
        hand["rank"] = len(sorted_hands) - sorted_hands.index(hand)

    return sorted_hands


def get_hand_sum(hand_txt):
    hands = parse_hands(hand_txt)
    hands_with_ranks = compute_rank_hands(hands)
    calculated_bids = [int(hand["bet"]) * int(hand["rank"]) for hand in hands_with_ranks]
    return sum(calculated_bids)


if __name__ == "__main__":
    # PART 1
    working_dir = os.path.dirname(os.path.abspath(__file__))
    input_text = open(f"{working_dir}/day_7_input.txt").read()
    print(f"Part 1: {get_hand_sum(input_text)}")
