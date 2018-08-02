from random import shuffle
from hand import Hand
from card import Card
from player import Player
from termcolor import colored


class Poker:

    def __init__(self, player_count):
        self.player_count = player_count
        self.deck = self.generate_deck()
        self.players = []
        self.deal()
        self.display()


    def generate_deck(self):
        suits  = ['h', 's', 'd', 'c']
        values = [x for x in range(2,15)]
        deck   = []

        for s in suits:
            for val in values:
                new_card = Card(val, s)
                deck.append(new_card)

        shuffled_deck = [card_tuple for card_tuple in deck]
        shuffle(shuffled_deck)

        return shuffled_deck


    def print_deck(self):
        for card in self.deck:
            print(card.str_val, card.suit)
        return


    def deal(self):
        for i in range(0, self.player_count):
            cards = []
            for x in range(5):
                cards.append(self.deck.pop())
            h = Hand(cards)
            p = Player(str(i), h)
            self.players.append(p)
        return


    def display(self):
        sorted_players = sorted(self.players, key = lambda p: p.hand.score, reverse=True)
        for p in sorted_players:
            print('{0}: {1:20}        Score: {2:10}    Hand: {3:15}'.
                  format(colored(p.name, 'green'),
                         colored(p.hand.evaluation.title(), 'red'),
                         colored(p.hand.score, 'blue'),
                         colored(p.hand, 'cyan')))
        return
