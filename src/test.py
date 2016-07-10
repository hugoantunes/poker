import unittest
from hand import Hand


class TestPokerHand(unittest.TestCase):

    def test_hand_should_be_created_by_method_from_string(self):
        hand = Hand.from_string('4D 4D 4D 7H 8D')
        self.assertTrue(isinstance(hand, Hand))

if __name__ == '__main__':
    unittest.main()
