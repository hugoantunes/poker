# encoding: utf-8
import re
import collections


class Hand(object):
    possible_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    possible_values = [
        'HIGH_CARD', 'ONE_PAIR', 'TWO_PAIR', 'TREE_OF_A_KIND', 'STRAIGHT',
        'FLUSH', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'STRAIGHT_FLUSH', 'ROYAL_FLUSH'
    ]
    cards = []

    def __init__(self, cards):
        tot_cards = len(cards)
        if tot_cards != 5:
            raise Exception('{0} cards in the hand, must be 5'.format(tot_cards))
        self.numbers = collections.defaultdict(int)
        self.suits = collections.defaultdict(int)
        self.cards = cards
        self._set_numbers_and_suits()

    def __str__(self):
        return "<hand {0}, {1}>".format(self.cards, self.value)

    def __cmp__(self, other):
        if self.possible_values.index(self.value) > self.possible_values.index(other.value):
            return 1
        else:
            return -1

    def _set_numbers_and_suits(self):
        for card in self.cards:
            match = re.match(r'([23456789TJQKA]+)([CDHS]+)', card, re.I)
            if not match:
                raise Exception('wrong card defined')
            else:
                values = match.groups()
                self.numbers[values[0]] += 1
                self.suits[values[1]] += 1

    @staticmethod
    def from_string(cards_str):
        cards = cards_str.split(' ')
        return Hand(cards)

    @property
    def value(self):
        numbers = self.numbers.values()
        qnt_suits = len(self.suits.values())
        qnt_numbers = len(numbers)
        msg = 'HIGH_CARD'

        if qnt_numbers == 2 and qnt_suits > 1:
            if 4 in numbers:
                return 'FOUR_OF_A_KIND'
            return 'FULL_HOUSE'
        elif qnt_numbers == 3 and qnt_suits > 1:
            if 3 in numbers:
                return 'TREE_OF_A_KIND'
            return 'TWO_PAIR'
        elif qnt_numbers == 4 and qnt_suits > 1:
            return 'ONE_PAIR'
        else:
            flush, straight = False, False
            lower_card = min([self.possible_numbers.index(x) for x in self.numbers.keys()])
            higher_card = max([self.possible_numbers.index(x) for x in self.numbers.keys()])
            low_straight = set(("A", "2", "3", "4", "5"))

            if qnt_suits == 1:
                flush = True
                msg = 'FLUSH'
            if higher_card - lower_card == 4 or not set(self.numbers.keys()).difference(low_straight):
                straight = True
                msg = 'STRAIGHT'

            if straight and flush:
                if self.possible_numbers[higher_card] is 'A':
                    return 'ROYAL_FLUSH'
                return 'STRAIGHT_FLUSH'

            return msg
