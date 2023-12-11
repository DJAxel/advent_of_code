from __future__ import annotations
from collections import defaultdict
from functools import reduce


class Card:
    POSSIBLE_VALUES = "23456789TJQKA"

    def __init__(self, char: str):
        if len(char) != 1:
            raise ValueError(
                f"Card value must be exactly one character. Given value was {char}"
            )
        if char not in self.POSSIBLE_VALUES:
            raise ValueError(
                f"Card value must be one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. Given value was {char}"
            )
        self._value = self.POSSIBLE_VALUES.index(char)

    @property
    def value(self) -> int:
        return self._value

    def __repr__(self) -> str:
        return self.POSSIBLE_VALUES[self._value]

    def __gt__(self, other: Card) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.value > other.value

    def __eq__(self, other: Card) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.value == other.value


class JokerCard(Card):
    @property
    def value(self) -> int:
        return -1


class Type:
    TYPES = {
        "High card": 5 * [1],
        "One pair": [1, 1, 1, 2],
        "Two pair": [1, 2, 2],
        "Three of a kind": [1, 1, 3],
        "Full house": [2, 3],
        "Four of a kind": [1, 4],
        "Five of a kind": [5],
    }

    def __init__(self, cards: list[Card]):
        card_dict = defaultdict(lambda: 0)
        for card in cards:
            card_dict[card.value] += 1

        sorted_card_dict = sorted(card_dict.values()) or [0]
        sorted_card_dict[-1] += 5 - len(cards)  # Joker values -> highest other value

        types_list = list(self.TYPES.values())
        self._value = types_list.index(sorted_card_dict)

    @property
    def value(self) -> int:
        return self._value


class Hand:
    def __init__(self, string: str, use_jokers=False):
        cards, bid = string.split()
        self._bid = int(bid)
        self._cards: list[Card] = [
            JokerCard("J") if use_jokers and char == "J" else Card(char)
            for char in cards
        ]
        self._type = Type(
            list(filter(lambda card: not isinstance(card, JokerCard), self.cards))
        )

    @property
    def bid(self) -> int:
        return self._bid

    @property
    def cards(self) -> list[Card]:
        return self._cards

    @property
    def type(self) -> Type:
        return self._type

    def __repr__(self) -> str:
        return f'Hand("{reduce(lambda x, y: x + y, [str(c) for c in self.cards])} {self.bid}")'

    def __gt__(self, other: Hand) -> bool:
        if self.type.value != other.type.value:
            return self.type.value > other.type.value

        for own_card, other_card in zip(self.cards, other.cards):
            if own_card.value == other_card.value:
                continue

            return own_card.value > other_card.value

        raise ValueError(f"Values are the same: {self.cards} and {other.cards}")


if __name__ == "__main__":
    with open("./2023/day07/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]

    for use_jokers in [False, True]:
        hands = [Hand(x, use_jokers) for x in lines]
        answer = 0

        for i, hand in enumerate(sorted(hands)):
            rank = i + 1
            answer += rank * hand.bid

        print(answer)
