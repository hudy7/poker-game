from random import shuffle
from hand import Hand
from card import Card
from player import Player
from termcolor import colored


class Poker:

    def __init__(self, player_count, print_data=True):
        self.player_count = player_count
        self.deck = self.generate_deck()
        self.players = []
        self.deal()
        if print_data:
            self.display()

    '''
    Bottleneck O(n^2) move this process to Deck class
    and pass the deck in to avoid generating it every time.

    O(n^2) --> double for loop
    '''
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

    '''
    O(n) --> n = len(deck)
    '''
    def print_deck(self):
        for card in self.deck:
            print(card.str_val, card.suit)
        return

    '''
    Bottleneck O(n^2) but this process is limited to only k operations
    and should not have extreme impact on process runtime.

    O(nk) --> n = number of players (max(9))
          --> k = number of cards in hand (max(5))

    '''
    def deal(self):
        for i in range(0, self.player_count):
            cards = []
            for x in range(5):
                cards.append(self.deck.pop())
            h = Hand(cards)
            p = Player(str(i), h)
            self.players.append(p)
        return

    '''
    O(n) --> n = len(players) max(9)
    '''
    def get_stats(self):
        stats = {}
        for p in self.players:
            if p.hand.evaluation in stats:
                stats[p.hand.evaluation] += 1
            else:
                stats[p.hand.evaluation] = 1
        return stats

    '''
    Bottleneck O(n log n) because of sorting the players based on there hand scoreself.
    Could possibly sort the players as their hands are being distributed.
    '''
    def display(self):
        sorted_players = sorted(self.players, key = lambda p: p.hand.score, reverse=True)
        for p in sorted_players:
            print('{0}: {1:20}        Score: {2:10}    Hand: {3:15}'.
                  format(colored(p.name, 'green'),
                         colored(p.hand.evaluation.title(), 'red'),
                         colored(p.hand.score, 'blue'),
                         colored(p.hand, 'cyan')))
        return
