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

    def test_hand_str_should_show_cards_and_value(self):
        hand = Hand.from_string('4D 4D 4S 7H 8D')
        excepected = "<hand ['4D', '4D', '4S', '7H', '8D'], THREE_OF_A_KIND>"
        self.assertEquals(str(hand), excepected)


class TestPokerHandValue(unittest.TestCase):

    def test_hand_with_a_high_card_should_return_HIGH_CARD_as_value(self):
        hand = Hand.from_string('4D 5D 3D 7H KD')
        self.assertEquals(hand.value, 'HIGH_CARD')

    def test_hand_with_one_pair_should_return_ONE_PAIR_as_value(self):
        hand = Hand.from_string('4D 4D 2D 7H KD')
        self.assertEquals(hand.value, 'ONE_PAIR')

    def test_hand_with_two_pairs_should_return_TWO_PAIRS_as_value(self):
        hand = Hand.from_string('4D 4D 7H 7H KD')
        self.assertEquals(hand.value, 'TWO_PAIR')

    def test_hand_with_same_three_cards_should_return_THREE_OF_A_KIND_as_value(self):
        hand = Hand.from_string('4D 4D 4S 7H KD')
        self.assertEquals(hand.value, 'THREE_OF_A_KIND')

    def test_hand_with_same_four_cards_should_return_FOUR_OF_A_KIND_as_value(self):
        hand = Hand.from_string('4D 4D 4C 4C KS')
        self.assertEquals(hand.value, 'FOUR_OF_A_KIND')

    def test_hand_with_same_three_cards_and_a_pair_should_return_FULL_HOUSE_as_value(self):
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


class TestPokerHandComparison(unittest.TestCase):

    def test_royal_flush_should_win_to_straight(self):
        winner_hand = Hand.from_string('TS JS QS KS AS')
        looser_hand = Hand.from_string('AS 2S 3D 4S 5D')
        self.assertTrue(winner_hand > looser_hand)

    def test_flush_should_looase_to_full_house(self):
        looser_hand = Hand.from_string('2D 4D TD 9D 2D')
        winner_hand = Hand.from_string('4D 4D 4C 3D 3D')
        self.assertTrue(looser_hand < winner_hand)

    def test_when_no_combination_high_card_should_win(self):
        winner_hand = Hand.from_string('4D 5D 3D 7H KD')
        looser_hand = Hand.from_string('4D 5D 3D 7H TD')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_straight_tie_high_card_should_win(self):
        winner_hand = Hand.from_string('3S 4S 5D 6S 7D')
        looser_hand = Hand.from_string('2S 3S 4D 5S 6D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_flush_tie_high_card_should_win(self):
        winner_hand = Hand.from_string('2D 4D TD KD 2D')
        looser_hand = Hand.from_string('2D 4D TD 9D 2D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_two_royal_flush_should_be_a_tie(self):
        hand_one = Hand.from_string('TS JS QS KS AS')
        hand_two = Hand.from_string('TD JD QD KD AD')
        self.assertTrue(hand_one == hand_two)

    def test_when_one_pair_tie_higher_pair_should_win(self):
        winner_hand = Hand.from_string('TD TD 2D 7H 5D')
        looser_hand = Hand.from_string('9D 9D 2D 7H AD')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_higher_one_pair_tie_higher_card_should_win(self):
        winner_hand = Hand.from_string('9D 9D 2D 7H 5D')
        looser_hand = Hand.from_string('9D 9D 2D 7H 3D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_two_pair_tie_higher_two_pair_should_win(self):
        winner_hand = Hand.from_string('4D 4D AH AH KD')
        looser_hand = Hand.from_string('4D 4D 2H 2H 8D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_higher_two_pairs_tie_higher_card_should_win(self):
        winner_hand = Hand.from_string('4D 4D 7H 7H AD')
        looser_hand = Hand.from_string('4D 4D 7H 7H KD')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_three_of_a_kind_tie_higher_three_of_a_kind_should_win(self):
        winner_hand = Hand.from_string('AD AD AS 7H 2D')
        looser_hand = Hand.from_string('KD KD KS 7H 3D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_higher_three_of_a_kind_tie_higher_card_should_win(self):
        winner_hand = Hand.from_string('AD AD AS KH 2D')
        looser_hand = Hand.from_string('AD AD AS 7H TD')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_four_of_a_kind_tie_higher_four_of_a_kind_should_win(self):
        winner_hand = Hand.from_string('TD TD TC TC KS')
        looser_hand = Hand.from_string('4D 4D 4C 4C 2S')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_higher_four_of_a_kind_tie_higher_card_should_win(self):
        winner_hand = Hand.from_string('4D 4D 4C 4C AS')
        looser_hand = Hand.from_string('4D 4D 4C 4C KS')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_full_house_tie_higher_full_house_should_win(self):
        winner_hand = Hand.from_string('4D 4D 4C 5D 5D')
        looser_hand = Hand.from_string('4D 4D 4C 3D 3D')
        self.assertTrue(winner_hand > looser_hand)

    def test_when_hands_are_equals_numbers_should_tie(self):
        hand1 = Hand.from_string('4D 4D 4C 5D 5D')
        hand2 = Hand.from_string('4D 4D 4C 5D 5D')

        self.assertTrue(hand1 == hand2)

        hand1 = Hand.from_string('TD TD TC TC KS')
        hand2 = Hand.from_string('TS TS TH TH KS')

        self.assertTrue(hand1 == hand2)

if __name__ == '__main__':
    unittest.main()
