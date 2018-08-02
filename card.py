class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        self.card_values = {
            2  : '2',
            3  : '3',
            4  : '4',
            5  : '5',
            6  : '6',
            7  : '7',
            8  : '8',
            9  : '9',
            10 : '10',
            11 : 'J',
            12 : 'Q',
            13 : 'K',
            14 : 'A'
        }
        #self.num_val = self.evaluate_card()
        self.str_val = self.card_values[self.val]


    def evaluate_card(self):
        return self.card_values[self.val]
