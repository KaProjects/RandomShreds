import itertools
from math import comb

from resolver import Resolver


def resolve(players: list, table: tuple, remaining_deck: list):
    players_cards = list()
    wins = list()

    for player in players:
        players_cards.append(set(player).union(set(table)))
        wins.append(set())

    combinations = itertools.combinations(remaining_deck, 5 - len(table))
    combs_count = comb(len(remaining_deck), 5 - len(table))

    for combination in combinations:

        results = list()

        for i in range(0, len(players_cards)):
            result = Resolver(cards=players_cards[i].union(set(combination))).resolve_best()
            if len(results) == 0:
                results.append((i, result))
            else:
                better = get_better_result(results[0], (i, result))
                if better == "both":
                    results.append((i, result))
                else:
                    results.clear()
                    results.append(better)

        for result in results:
            res = result[1]
            player_cards = players_cards[result[0]]
            added_cards = res.residual_cards.union(res.result_cards).difference(player_cards)
            wins[result[0]].add(tuple(added_cards))

    for i in range(0, len(players)):
        print("---------")
        print(str(players[i]) + " " + str(table) + " " + str())
        print(Resolver(tuple(players[i]), table).resolve_best())
        print(str(round(len(wins[i]) / combs_count * 100, 2)) + "% " + str(len(wins[i])) + " " + str(
            sorted(wins[i], reverse=True)))


def get_better_result(player0, player1):
    result0 = player0[1]
    result1 = player1[1]

    if result0.ranking > result1.ranking:
        return player0

    if result0.ranking < result1.ranking:
        return player1

    if result0.ranking == result1.ranking:
        if result0.result_cards > result1.result_cards:
            return player0
        if result0.result_cards < result1.result_cards:
            return player1
        if result0.result_cards == result1.result_cards:
            return "both"
    raise Exception(str(player0) + str(player1))
