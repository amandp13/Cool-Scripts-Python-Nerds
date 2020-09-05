from random import shuffle


class Cards:

    def __init__(self,value,suite):
        self.suite=suite
        self.value=value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k']
        self.cards=[]
        for suit in suits:
            for value in values:
                self.cards.append(Cards(suit,value))
        # pythonic way
        # self.cards = [Cards(value,suite) for value in values for suite in suites]    //  List Comprehension

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        return len(self.cards)

    def _deal(self,num):
        count=self.count()
        if count == 0:
            raise ValueError('All Cards Have Been Dealt')
        actual = min([count,num])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual] # Complex Explanation

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only Full Decks Can Be Shuffled')
        shuffle(self.cards)
        return self.cards
