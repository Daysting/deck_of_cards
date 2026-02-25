# Erick Hofer
# CIS261
# Deck of Cards

# This module defines a simple card game using classes to represent a deck of cards and individual cards.
# The Deck class creates a standard 52-card deck, shuffles it, and allows dealing cards one at a time.

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
# The Card class represents each card with its suit and rank.    
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
    
# The main function demonstrates creating a deck, shuffling it, and dealing a few cards while showing the remaining cards in the deck.    
def main():
    deck = Deck()
    print(deck)
    deck.shuffle()
    print("Dealing cards:")
    for _ in range(5):
        card = deck.deal_card()
        if card:
            print(card)
        else:
            print("No more cards to deal.")
    print(deck)

# The entry point of the program calls the main function to execute the card game demonstration.
if __name__ == "__main__":
    main()
