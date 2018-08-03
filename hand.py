import card

class Hand:
    
    def __init__(self, cards):
        self.cards = cards
        self.scores = {
            'high card'       : 1,
            'pair'            : 2,
            '2 pair'          : 3,
            '3 of a kind'     : 4,
            'straight'        : 5,
            'flush'           : 6,
            'full house'      : 7,
            '4 of a kind'     : 8,
            'straight flush'  : 9,
            'royal flush'     : 10
        }
        self.value_counts = self.setup_value_counts()
        self.suit_counts  = self.setup_suit_counts()
        self.evaluation   = self.evaluate_hand()
        self.score        = self.scores[self.evaluation]

    '''
    Planning on moving setup_value_counts and setup_suit_counts into one operation.
    value_counts, suit_counts = self.setup_counts()
    setup_counts() returns 2 dictionaries
    '''

    '''
    O(n) --> n = len(cards) --> max(5)
    '''
    def setup_value_counts(self):
        d = {}
        for c in self.cards:
            if c.str_val in d:
                d[c.str_val] += 1
            else:
                d[c.str_val] = 1
        return d


    '''
    O(n) --> n = len(cards) --> max(5)
    '''
    def setup_suit_counts(self):
        d = {}
        for c in self.cards:
            if c.suit in d:
                d[c.suit] += 1
            else:
                d[c.suit] = 1
        return d


    '''
    O(n) --> n = len(cards) --> max(5)
    '''
    def __str__(self):
        return ' '.join((c.str_val + c.suit.upper()) for c in self.cards)


    '''
    Main logic
    O(n log n) --> worst case - when you have to sort in isStraight()
    O(n) --> best case - all other operations
    '''
    def evaluate_hand(self):
        if self.isStraight() and self.isFlush():
            if self.isRoyalStraight():
                return 'royal flush'
            return 'straight flush'

        if self.isNumOfKind(4):
            return '4 of a kind'

        if self.isNumOfKind(3) and self.isNumOfKind(2):
            return 'full house'

        if self.isFlush():
            return 'flush'

        if self.isStraight():
            return 'straight'

        if self.isTwoPair():
            return '2 pair'

        if self.isNumOfKind(3):
            return '3 of a kind'

        if self.isNumOfKind(2):
            return 'pair'

        return 'high card'


    '''
    Evaluators
    '''

    '''
    O(n) -> n = len(cards) --> max(5)
    '''
    def isRoyalStraight(self):
        return max(card.val for card in self.cards) == 14


    '''
    O(n) -> n = len(self.value_counts)
    '''
    def isNumOfKind(self, n):
        #for card in cards
        for val in self.value_counts.values():
            if val == n:
                return True
        return False


    '''
    O(n) -> n = len(cards) --> max(5)
    '''
    def isFlush(self):
        suits = set()
        for card in self.cards:
            suits.add(card.suit)
        return len(suits) == 1


    '''
    O(n log n) -> sorted operation
    '''
    def isStraight(self):
        sorted_cards = sorted(self.cards, key=lambda card: card.val)

        for i in range(1, len(sorted_cards)):
            if sorted_cards[i-1].val + 1 != sorted_cards[i].val:
                return False

        return True


    '''
    O(n) -> n = len(self.value_counts)
    '''
    def isTwoPair(self):
        twos_count = 0
        for val in self.value_counts.values():
            if val == 2:
                twos_count += 1
        return twos_count == 2
