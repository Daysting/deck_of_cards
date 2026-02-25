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

    def deal_cards(self, count):
        """Deal a specific number of cards from the deck.

        Returns a list of Card objects. If the deck runs out of cards before
        reaching the requested count, the list will contain as many cards as
        possible.
        """
        dealt = []
        for _ in range(count):
            card = self.deal_card()
            if card:
                dealt.append(card)
            else:
                break
        return dealt

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
    
# The main function demonstrates creating a deck, shuffling it, and dealing a few cards while showing the remaining cards in the deck.    
def main():
    # display program title
    print("="*50)
    print("=== Welcome to the Card Dealer ===")
    print("="*50)
    deck = Deck()
    print(deck)
    print("="*50)
    print("Shuffling the deck...")
    print("="*50)
    deck.shuffle()

    # let the user choose how many cards to deal
    try:
        how_many = int(input("How many cards would you like to deal? "))
    except ValueError:
        print("Invalid number, dealing 5 cards by default.")
        how_many = 5

    print("="*50)
    print(f"Dealing your {how_many} cards:")
    print("="*50)
    dealt_cards = deck.deal_cards(how_many)
    if dealt_cards:
        for card in dealt_cards:
            print(card)
    else:
        print("No cards were dealt.")

    print("="*50)
    print(deck)
    print("="*50)

# The entry point of the program calls the main function to execute the card game demonstration.
if __name__ == "__main__":
    main()
