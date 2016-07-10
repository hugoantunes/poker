import unittest
from hand import Hand


class TestPokerHand(unittest.TestCase):

    def test_hand_must_be_created_by_method_from_string(self):
        hand = Hand.from_string('4D 4D 4D 7H 8D')
        self.assertTrue(isinstance(hand, Hand))

    def test_hand_wrong_card_parameter_should_raise_exception(self):
        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D 4D 99k 8D')
        self.assertEquals(cm.exception.message, 'wrong card defined')

    def test_less_than_5_cards_should_raise_exception(self):
        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D')
        self.assertEquals(cm.exception.message, '2 cards in the hand, must be 5')

        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D 4D 4D 4D 4D 4D 4D')
        self.assertEquals(cm.exception.message, '8 cards in the hand, must be 5')

    def test_hand_must_count_numbers(self):
        hand = Hand.from_string('4D 4D 4D 7H 8D')
        self.assertEquals(hand.numbers['4'], 3)
        self.assertEquals(hand.numbers['7'], 1)
        self.assertEquals(hand.numbers['8'], 1)

    def test_hand_must_count_suits(self):
        hand = Hand.from_string('4D 4D 4D 7H 8D')
        self.assertEquals(hand.suits['D'], 4)
        self.assertEquals(hand.suits['H'], 1)


if __name__ == '__main__':
    unittest.main()
