from dataclasses import dataclass
from enum import Enum, IntEnum


class Rank(Enum):
    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10", 10)
    JACK = ("J", 11)
    QUEEN = ("Q", 12)
    KING = ("K", 13)
    ACE = ("A", 14)


class Suit(Enum):
    SPADES = "♠"
    DIAMONDS = "♦"
    HEARTS = "♥"
    CLUBS = "♣"


def get_all_cards():
    cards: list[Card] = []
    for rank in Rank:
        for suit in Suit:
            cards.append(Card(rank, suit))
    return cards


@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit

    def __repr__(self):
        return self.rank.value[0] + self.suit.value

    def __lt__(self, other): return self.rank.value[1] < other.rank.value[1]

    def __le__(self, other): return self.rank.value[1] <= other.rank.value[1]

    def __gt__(self, other): return self.rank.value[1] > other.rank.value[1]

    def __ge__(self, other): return self.rank.value[1] >= other.rank.value[1]

    def __eq__(self, other): return self.rank.value[1] == other.rank.value[1]


@dataclass(frozen=True)
class Deck:
    cards: list[Card]

    def check_valid(self):
        if not len(self.cards) == len(get_all_cards()):
            raise Exception(f"Invalid Deck! {str(len(self.cards))} cards in deck, should be {len(get_all_cards())}")
        new_deck: set[Card] = set()
        for card in self.cards:
            if card in new_deck:
                raise Exception("Invalid Deck! " + repr(card) + " already in deck!")
            else:
                new_deck.add(card)

    def get_one(self):
        return self.cards.pop()


class Ranking(IntEnum):
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@dataclass(frozen=True)
class Result:
    ranking: Ranking
    result_cards: list  # sorted best 5
    residual_cards: set
