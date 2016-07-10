# encoding: utf-8


class Hand(object):

    cards = []

    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def from_string(cards_str):
        cards = cards_str.split(" ")
        return Hand(cards)
