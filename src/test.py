import unittest
from hand import Hand


class TestPokerHand(unittest.TestCase):

    def test_hand_must_be_created_by_method_from_string(self):
        hand = Hand.from_string('4D 4D 4S 7H 8D')
        self.assertTrue(isinstance(hand, Hand))

    def test_hand_wrong_card_parameter_should_raise_exception(self):
        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D 4S 99k 8D')
        self.assertEquals(cm.exception.message, 'wrong card defined')

    def test_less_than_5_cards_should_raise_exception(self):
        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D')
        self.assertEquals(cm.exception.message, '2 cards in the hand, must be 5')

        with self.assertRaises(Exception) as cm:
            Hand.from_string('4D 4D 4D 4D 4D 4D 4D 4D')
        self.assertEquals(cm.exception.message, '8 cards in the hand, must be 5')

    def test_hand_must_count_numbers(self):
        hand = Hand.from_string('4D 4D 4S 7H 8D')
        self.assertEquals(hand.numbers['4'], 3)
        self.assertEquals(hand.numbers['7'], 1)
        self.assertEquals(hand.numbers['8'], 1)

    def test_hand_must_count_suits(self):
        hand = Hand.from_string('4D 4D 4H 7H 8D')
        self.assertEquals(hand.suits['D'], 3)
        self.assertEquals(hand.suits['H'], 2)

    def test_hand_with_a_high_card_should_return_HIGH_CARD_as_value(self):
        hand = Hand.from_string('4D 5D 3D 7H KD')
        self.assertEquals(hand.value, 'HIGH_CARD')

    def test_hand_with_one_pair_should_return_ONE_PAIR_as_value(self):
        hand = Hand.from_string('4D 4D 2D 7H KD')
        self.assertEquals(hand.value, 'ONE_PAIR')

    def test_hand_with_two_pairs_should_return_TWO_PAIRS_as_value(self):
        hand = Hand.from_string('4D 4D 7H 7H KD')
        self.assertEquals(hand.value, 'TWO_PAIR')

    def test_hand_with_same_tree_cards_should_return_TREE_OF_A_KIND_as_value(self):
        hand = Hand.from_string('4D 4D 4S 7H KD')
        self.assertEquals(hand.value, 'TREE_OF_A_KIND')

    def test_hand_with_same_four_cards_should_return_FOUR_OF_A_KIND_as_value(self):
        hand = Hand.from_string('4D 4D 4C 4C KS')
        self.assertEquals(hand.value, 'FOUR_OF_A_KIND')

    def test_hand_with_same_tree_cards_and_a_pair_should_return_FULL_HOUSE_as_value(self):
        hand = Hand.from_string('4D 4D 4C 3D 3D')
        self.assertEquals(hand.value, 'FULL_HOUSE')

    def test_hand_with_same_all_suits_should_return_FLUSH_as_value(self):
        hand = Hand.from_string('2D 4D TD 9D 2D')
        self.assertEquals(hand.value, 'FLUSH')

    def test_hand_with_sequence_numbers_should_return_STRAIGHT_as_value(self):
        hand = Hand.from_string('2D 3D 4D 5D 6S')
        self.assertEquals(hand.value, 'STRAIGHT')

    def test_hand_with_sequence_numbers_and_the_same_suits_should_return_STRAIGHT_FLUSH_as_value(self):
        hand = Hand.from_string('2D 3D 4D 5D 6D')
        self.assertEquals(hand.value, 'STRAIGHT_FLUSH')

    def test_hand_with_high_sequence_numbers_and_the_same_suits_should_return_ROYAL_FLUSH_as_value(self):
        hand = Hand.from_string('TS JS QS KS AS')
        self.assertEquals(hand.value, 'ROYAL_FLUSH')

    def test_hand_with_sequence_cards_when_A_is_lower_card_should_return_STRAIGHT_as_value(self):
        hand = Hand.from_string('AS 2S 3D 4S 5D')
        self.assertEquals(hand.value, 'STRAIGHT')

if __name__ == '__main__':
    unittest.main()
