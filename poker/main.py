import probabilities
from game import Game

if __name__ == '__main__':
    game = Game()
    game.create_deck()
    print(game.deck.cards[::-1])
    game.set_number_of_players(2)

    game.deal_players()

    # game.deal_flop()

    # game.deal_turn()

    # game.deal_river()

    probabilities.resolve(game.players, game.table, game.deck.cards)

    # print(game.deck.cards[::-1])
