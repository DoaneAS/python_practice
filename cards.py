class Card(object):

    """Represents a playing card"""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    """note variables like rank_names are
     inside a class but outside a method and called class attributes
    which is different from variables like suit and rank"""

    """ the expression 'Card.rank_names[self.rank]' means “use the attribute 'rank
    from the object 'self' as an index into the list ￼'rank_names￼'￼ from the class ￼Card,
    and select the appropriate string.” """
       #
    # def __cmp__(self, other):
    # Check the suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1
    #
    # suits are same...check rank...
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1
    #
    # ranks are same....tie
    #     return 0

    """same as above, using tuples """

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

# create a card:


class Deck(object):

    """Represents a deck of class Cards """
    import random

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
        """method using another fx as above is called a veneer"""

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()


class Hand(Deck):
    """represents a hand of playing cards"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


#deck = Deck()
# print deck
#ds = deck.sort()
# type(deck)
# print deck


if __name__ == '__main__':
    deck = Deck()
    print deck
