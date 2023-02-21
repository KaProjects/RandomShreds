import random

from classes import *


class Game:
    # TODO fixed stages

    def __init__(self):
        self.n_players = None
        self.deck = None
        self.players = list()
        self.table = ()

    def create_deck(self):
        cards = get_all_cards()
        self.deck = Deck(random.sample(cards, len(cards)))
        self.deck.check_valid()

    def set_number_of_players(self, number_of_players: int):
        self.n_players = number_of_players

    def deal_players(self):
        for i in range(0, self.n_players):
            self.players.append((self.deck.get_one(), None))

        for i in range(0, self.n_players):
            self.players[i] = (self.players[i][0], self.deck.get_one())

    def deal_flop(self):
        self.table = (self.deck.get_one(), self.deck.get_one(), self.deck.get_one())

    def deal_turn(self):
        self.table = (self.table[0], self.table[1], self.table[2], self.deck.get_one())

    def deal_river(self):
        self.table = (self.table[0], self.table[1], self.table[2], self.table[3], self.deck.get_one())
