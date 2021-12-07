import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('spades', 1)
        self.card2 = Card('hearts', 5)
        self.cardgame = CardGame('card1', 'card2')
        self.cards = [self.card1, self.card2]
        
        
        
    def test_card_game_has_ace(self):
        self.assertEqual(1, self.card1.value)

    def test_card_game_has_highest_card(self):
        self.assertEqual(5, self.card2.value)

    def test_cards_total(self):
        total = self.cardgame.cards_total(self.cards)
        self.assertEqual("You have a total of 6", total)