from classes import Rank, Result, Ranking, Suit, Card


def compose_ranks(cards: set[Card]) -> dict:
    ranks = dict()
    for rank in Rank.__reversed__():
        ranks[rank.name] = set()
    for card in cards:
        ranks.get(card.rank.name).add(card)
    return ranks


def compose_suits(cards: set[Card]) -> dict:
    suits = dict()
    for suit in Suit:
        suits[suit.name] = set()
    for card in cards:
        suits.get(card.suit.name).add(card)
    return suits


def get_four_of_kind(cards: set[Card]) -> list[Card]:
    ranks = compose_ranks(cards)
    for rank in ranks:
        if len(ranks[rank]) == 4:
            return list(ranks[rank])


def get_highest_three_of_kind(cards: set[Card]) -> list[Card]:
    ranks = compose_ranks(cards)
    for rank in ranks:
        if len(ranks[rank]) >= 3:
            return list(ranks[rank])[0:3]


def get_highest_two_of_kind(cards: set[Card]) -> list[Card]:
    ranks = compose_ranks(cards)
    for rank in ranks:
        if len(ranks[rank]) >= 2:
            return list(ranks[rank])[0:2]


def get_flush_suit(cards: set[Card]) -> list[Card]:
    suits = compose_suits(cards)
    for suit in suits:
        if len(suits[suit]) >= 5:
            return sorted(list(suits[suit]), reverse=True)


def get_highest_flush_suit(cards: set[Card]) -> list[Card]:
    all_flush_suits = get_flush_suit(cards)
    if all_flush_suits is not None:
        return all_flush_suits[0:5]


def get_highest_straight(cards: set[Card]) -> list[Card]:
    ranks = list(compose_ranks(cards).values())
    for i in range(0, len(ranks) - 4):
        if len(ranks[i]) > 0 and len(ranks[i + 1]) > 0 and len(ranks[i + 2]) > 0 and len(ranks[i + 3]) > 0 and len(
                ranks[i + 4]) > 0:
            return [ranks[i].pop(), ranks[i + 1].pop(), ranks[i + 2].pop(), ranks[i + 3].pop(), ranks[i + 4].pop()]


class Resolver:
    def __init__(self, *args, **kwargs):

        if "cards" in kwargs.keys():
            self.cards = kwargs["cards"]
        else:
            self.cards = set()
            for card in args[0]: self.cards.add(card)
            for card in args[1]: self.cards.add(card)

    def resolve_best(self) -> Result:

        flush = get_flush_suit(self.cards)
        if flush is not None:
            straight_flush = get_highest_straight(set(flush))
            if straight_flush is not None:
                if straight_flush[0].rank == Rank.ACE:
                    return Result(Ranking.ROYAL_FLUSH, straight_flush, self.cards.difference(straight_flush))
                else:
                    return Result(Ranking.STRAIGHT_FLUSH, straight_flush, self.cards.difference(straight_flush))

        quads = get_four_of_kind(self.cards)
        if quads is not None:
            result_cards = quads
            result_cards.append(sorted(self.cards.difference(quads)).pop())
            return Result(Ranking.FOUR_OF_A_KIND, result_cards, self.cards.difference(result_cards))

        triple = get_highest_three_of_kind(self.cards)
        if triple is not None:
            pair = get_highest_two_of_kind(self.cards.difference(triple))
            if pair is not None:
                result_cards = triple + pair
                return Result(Ranking.FULL_HOUSE, result_cards, self.cards.difference(result_cards))

        if flush is not None:
            result_cards = get_highest_flush_suit(self.cards)
            return Result(Ranking.FLUSH, result_cards, self.cards.difference(result_cards))

        straight = get_highest_straight(self.cards)
        if straight is not None:
            return Result(Ranking.STRAIGHT, straight, self.cards.difference(straight))

        if triple is not None:
            result_cards = triple
            all_but_triple = sorted(self.cards.difference(triple))
            result_cards.append(all_but_triple.pop())
            result_cards.append(all_but_triple.pop())
            return Result(Ranking.THREE_OF_A_KIND, result_cards, self.cards.difference(result_cards))

        highest_pair = get_highest_two_of_kind(self.cards)
        if highest_pair is not None:
            second_pair = get_highest_two_of_kind(self.cards.difference(highest_pair))
            if second_pair is not None:
                result_cards = highest_pair + second_pair
                result_cards.append(sorted(self.cards.difference(result_cards)).pop())
                return Result(Ranking.TWO_PAIR, result_cards, self.cards.difference(result_cards))
            else:
                result_cards = highest_pair
                all_but_pair = sorted(self.cards.difference(result_cards))
                if len(all_but_pair) > 0:
                    result_cards.append(all_but_pair.pop())
                    result_cards.append(all_but_pair.pop())
                    result_cards.append(all_but_pair.pop())
                return Result(Ranking.ONE_PAIR, result_cards, self.cards.difference(result_cards))

        if len(self.cards) == 2:
            return Result(Ranking.HIGH_CARD, sorted(self.cards, reverse=True), set())
        else:
            result_cards = sorted(list(self.cards), reverse=True)[0:5]
            return Result(Ranking.HIGH_CARD, result_cards, self.cards.difference(result_cards))
