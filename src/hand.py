# encoding: utf-8
import re
import collections


class Hand(object):

    cards = []

    def __init__(self, cards):
        tot_cards = len(cards)
        if tot_cards != 5:
            raise Exception('{0} cards in the hand, must be 5'.format(tot_cards))
        self.numbers = collections.defaultdict(int)
        self.suits = collections.defaultdict(int)
        self.cards = cards
        self._set_numbers_and_suits()

    @staticmethod
    def from_string(cards_str):
        cards = cards_str.split(" ")
        return Hand(cards)

    def _set_numbers_and_suits(self):
        for card in self.cards:
            match = re.match(r"([24556789TJQKA]+)([CDHS]+)", card, re.I)
            if not match:
                raise Exception('wrong card defined')
            else:
                values = match.groups()
                self.numbers[values[0]] += 1
                self.suits[values[1]] += 1
