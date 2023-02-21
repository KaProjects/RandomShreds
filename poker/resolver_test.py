import unittest

import resolver
from classes import Card, Rank, Suit, Ranking


class Test_get_four_of_kind(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_four_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(Card(Rank.TEN, Suit.SPADES) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.HEARTS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.CLUBS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))

    def test_none(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TWO, Suit.DIAMONDS)}
        result = resolver.get_four_of_kind(cards)
        self.assertIsNone(result, cards)


class Test_get_highest_three_of_kind(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_three_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.HEARTS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.CLUBS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result, str(cards) + " => " + str(result))

    def test_from_quads(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_three_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 3, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))

    def test_from_two_triples(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.FIVE, Suit.HEARTS), Card(Rank.FIVE, Suit.CLUBS),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.HEARTS)}
        result = resolver.get_highest_three_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 3, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.CLUBS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.HEARTS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.CLUBS) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.HEARTS) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.SIX, Suit.HEARTS) not in result, str(cards) + " => " + str(result))

    def test_none(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_three_of_kind(cards)
        self.assertIsNone(result, cards)


class Test_get_highest_two_of_kind(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.JACK, Suit.HEARTS) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.CLUBS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result, str(cards) + " => " + str(result))

    def test_from_quads(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 2, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))

    def test_from_triples(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.JACK, Suit.SPADES),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 2, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.JACK, Suit.SPADES) not in result, str(cards) + " => " + str(result))

    def test_from_full_house(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.NINE, Suit.HEARTS),
                 Card(Rank.TEN, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 2, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.HEARTS) not in result, str(cards) + " => " + str(result))

    def test_from_two_pairs(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.NINE, Suit.HEARTS),
                 Card(Rank.JACK, Suit.HEARTS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(Card(Rank.TEN, Suit.CLUBS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.FIVE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.SPADES) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.NINE, Suit.HEARTS) not in result, str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.JACK, Suit.HEARTS) not in result, str(cards) + " => " + str(result))

    def test_none(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.HEARTS), Card(Rank.QUEEN, Suit.CLUBS), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_two_of_kind(cards)
        self.assertIsNone(result, cards)


class Test_get_highest_flush_suit(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_highest_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_more_suits(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.QUEEN, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_highest_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.QUEEN, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_straight_flush(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.FOUR, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.SIX, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_highest_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.SIX, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FOUR, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.THREE, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_royal_flush(self):
        cards = {Card(Rank.JACK, Suit.SPADES), Card(Rank.QUEEN, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.ACE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_highest_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.ACE, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.KING, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.QUEEN, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_none(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.HEARTS), Card(Rank.TWO, Suit.CLUBS),
                 Card(Rank.JACK, Suit.DIAMONDS)}
        result = resolver.get_highest_flush_suit(cards)
        self.assertIsNone(result, cards)


class Test_get_flush_suit(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.TEN, Suit.DIAMONDS)}
        result = resolver.get_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_more_suits(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.QUEEN, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 6, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.QUEEN, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[4], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[5], str(cards) + " => " + str(result))

    def test_straight_flush(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.FOUR, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.SIX, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 6, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.SIX, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FOUR, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.THREE, Suit.SPADES), result[4], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[5], str(cards) + " => " + str(result))

    def test_royal_flush(self):
        cards = {Card(Rank.JACK, Suit.SPADES), Card(Rank.QUEEN, Suit.SPADES), Card(Rank.TWO, Suit.SPADES),
                 Card(Rank.ACE, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.SPADES),
                 Card(Rank.QUEEN, Suit.HEARTS)}
        result = resolver.get_flush_suit(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 6, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.ACE, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.KING, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.QUEEN, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[4], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[5], str(cards) + " => " + str(result))

    def test_none(self):
        cards = {Card(Rank.FIVE, Suit.SPADES), Card(Rank.NINE, Suit.HEARTS), Card(Rank.TWO, Suit.CLUBS),
                 Card(Rank.JACK, Suit.DIAMONDS)}
        result = resolver.get_flush_suit(cards)
        self.assertIsNone(result, cards)


class Test_get_highest_straight(unittest.TestCase):

    def test_basic(self):
        cards = {Card(Rank.SEVEN, Suit.SPADES), Card(Rank.TWO, Suit.HEARTS), Card(Rank.EIGHT, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.NINE, Suit.DIAMONDS)}
        result = resolver.get_highest_straight(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.DIAMONDS), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.EIGHT, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.SEVEN, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_more_straight(self):
        cards = {Card(Rank.SEVEN, Suit.SPADES), Card(Rank.QUEEN, Suit.HEARTS), Card(Rank.EIGHT, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES), Card(Rank.NINE, Suit.DIAMONDS)}
        result = resolver.get_highest_straight(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.QUEEN, Suit.HEARTS), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.NINE, Suit.DIAMONDS), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.EIGHT, Suit.SPADES), result[4], str(cards) + " => " + str(result))

    def test_with_pair(self):
        cards = {Card(Rank.KING, Suit.SPADES), Card(Rank.NINE, Suit.SPADES), Card(Rank.SEVEN, Suit.HEARTS),
                 Card(Rank.EIGHT, Suit.SPADES), Card(Rank.JACK, Suit.SPADES), Card(Rank.TEN, Suit.SPADES),
                 Card(Rank.NINE, Suit.DIAMONDS)}
        result = resolver.get_highest_straight(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.JACK, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TEN, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.EIGHT, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.SEVEN, Suit.HEARTS), result[4], str(cards) + " => " + str(result))
        self.assertTrue(Card(Rank.KING, Suit.SPADES) not in result, str(cards) + " => " + str(result))

    def test_smallest(self):
        cards = {Card(Rank.KING, Suit.SPADES), Card(Rank.SIX, Suit.SPADES), Card(Rank.FOUR, Suit.HEARTS),
                 Card(Rank.FIVE, Suit.SPADES), Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES),
                 Card(Rank.NINE, Suit.DIAMONDS)}
        result = resolver.get_highest_straight(cards)
        self.assertIsNotNone(result, cards)
        self.assertTrue(len(result) == 5, str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.SIX, Suit.SPADES), result[0], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FIVE, Suit.SPADES), result[1], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.FOUR, Suit.HEARTS), result[2], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.THREE, Suit.SPADES), result[3], str(cards) + " => " + str(result))
        self.assertEqual(Card(Rank.TWO, Suit.SPADES), result[4], str(cards) + " => " + str(result))


class Test_resolve_best(unittest.TestCase):

    def test_high_card_player(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = ()
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.HIGH_CARD)
        self.assertTrue(len(result.result_cards) == 2, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 0, result.residual_cards)

    def test_pair_player(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS))
        table = ()
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.ONE_PAIR)
        self.assertTrue(len(result.result_cards) == 2, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 0, result.residual_cards)

    def test_unfinished_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.QUEEN, Suit.DIAMONDS), Card(Rank.KING, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.HIGH_CARD)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.ACE, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.KING, Suit.CLUBS), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.QUEEN, Suit.DIAMONDS), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 0, result.residual_cards)

    def test_high_card_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.QUEEN, Suit.DIAMONDS),
                 Card(Rank.KING, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.HIGH_CARD)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.ACE, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.KING, Suit.CLUBS), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.QUEEN, Suit.DIAMONDS), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_one_pair_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.KING, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.ONE_PAIR)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.ACE, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.KING, Suit.CLUBS), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_two_pairs_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.KING, Suit.CLUBS), Card(Rank.KING, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.TWO_PAIR)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.KING, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.KING, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_three_pairs_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.THREE, Suit.CLUBS), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.KING, Suit.CLUBS), Card(Rank.KING, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.TWO_PAIR)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.KING, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.KING, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.CLUBS) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_one_triple_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.TWO, Suit.SPADES), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.THREE_OF_A_KIND)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.ACE, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TWO, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_two_triples_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.TEN, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.TEN, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FULL_HOUSE)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.TEN, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TEN, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.TEN, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.THREE, Suit.SPADES) not in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_quads_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS))
        table = (Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.THREE, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.JACK, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FOUR_OF_A_KIND)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.JACK, Suit.HEARTS), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_quads_with_triple_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS))
        table = (Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.TEN, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.TEN, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FOUR_OF_A_KIND)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_quads_with_pair_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS))
        table = (Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.TEN, Suit.SPADES), Card(Rank.SIX, Suit.DIAMONDS),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.JACK, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FOUR_OF_A_KIND)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.SPADES) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.HEARTS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.DIAMONDS) in result.result_cards, result.result_cards)
        self.assertTrue(Card(Rank.SIX, Suit.CLUBS) in result.result_cards, result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.JACK, Suit.HEARTS), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_straight_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES))
        table = (Card(Rank.QUEEN, Suit.DIAMONDS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.NINE, Suit.SPADES),
                 Card(Rank.EIGHT, Suit.HEARTS), Card(Rank.ACE, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.TEN, Suit.CLUBS), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.EIGHT, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_longer_straight_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES))
        table = (Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.TEN, Suit.CLUBS), Card(Rank.NINE, Suit.SPADES),
                 Card(Rank.EIGHT, Suit.HEARTS), Card(Rank.JACK, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.JACK, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.TEN, Suit.CLUBS), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.EIGHT, Suit.HEARTS), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.ACE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.SIX, Suit.CLUBS), Card(Rank.JACK, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.ACE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_longer_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.ACE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.KING, Suit.SPADES), Card(Rank.JACK, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.ACE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.KING, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_straight_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.KING, Suit.DIAMONDS), Card(Rank.TWO, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT_FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_longer_straight_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.JACK, Suit.SPADES), Card(Rank.TWO, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT_FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.JACK, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_straight_longer_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.KING, Suit.SPADES), Card(Rank.TWO, Suit.HEARTS))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT_FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_longest_straight_flush_game(self):
        player = (Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES), Card(Rank.SEVEN, Suit.SPADES),
                 Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.STRAIGHT_FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.NINE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.EIGHT, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.SEVEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.SIX, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)

    def test_royal_flush_game(self):
        player = (Card(Rank.KING, Suit.SPADES), Card(Rank.JACK, Suit.SPADES))
        table = (Card(Rank.TEN, Suit.SPADES), Card(Rank.QUEEN, Suit.SPADES), Card(Rank.SEVEN, Suit.DIAMONDS),
                 Card(Rank.FOUR, Suit.CLUBS), Card(Rank.ACE, Suit.SPADES))
        result = resolver.Resolver(player, table).resolve_best()
        self.assertEqual(result.ranking, Ranking.ROYAL_FLUSH)
        self.assertTrue(len(result.result_cards) == 5, result.result_cards)
        self.assertEqual(result.result_cards[0], Card(Rank.ACE, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[1], Card(Rank.KING, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[2], Card(Rank.QUEEN, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[3], Card(Rank.JACK, Suit.SPADES), result.result_cards)
        self.assertEqual(result.result_cards[4], Card(Rank.TEN, Suit.SPADES), result.result_cards)
        self.assertTrue(len(result.residual_cards) == 2, result.residual_cards)


if __name__ == '__main__':
    unittest.main()
