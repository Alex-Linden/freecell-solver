import random


class Card:
    def __init__(self, suit, value, order):
        self.suit = suit
        self.value = value
        self.order = order
        self.color = "red" if suit in ["hearts", "diamonds"] else "black"

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for order, value in enumerate([
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]):
                self.cards.append(Card(suit, value, order))

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def __str__(self):
        # str_cards = [f"{card.value} of {card.suit}" for card in self.cards]
        str_cards = [card for card in self.cards]
        return str(str_cards)


# class Pile:
#     def __init__(self):
#         self.cards = []

#     def add(self, card):
#         self.cards.append(card)

#     def pop(self):
#         return self.cards.pop()

#     def is_empty(self):
#         return len(self.cards) == 0

#     def top(self):
#         return self.cards[-1]

#     def bottom(self):
#         return self.cards[0]

#     def __len__(self):
#         return len(self.cards)

#     def __getitem__(self, key):
#         return self.cards[key]

#     def __setitem__(self, key, value):
#         self.cards[key] = value

#     def __iter__(self):
#         return iter(self.cards)

#     def __reversed__(self):
#         return reversed(self.cards)

#     def __contains__(self, item):
#         return item in self.cards

#     def __str__(self):
#         return str(self.cards)

#     def __repr__(self):
#         return repr(self.cards)


class FreeCellGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.tableau = [[] for _ in range(8)]
        self.freecells = [[] for _ in range(4)]
        self.foundations = [[] for _ in range(4)]
        self.deal()

    def deal(self):
        for i in range(len(self.deck.cards)):
        # for i in range(len(self.deck)):
            self.tableau[i % 8].append(self.deck.pop())

    def max_stack(self):
        max_stack = 1
        for pile in self.freecells:
            if len(pile) == 0:
                max_stack += 1

        """If a tableau pile is empty, the max stack size is doubled.
        This may need to be implemented differently.
        possibly a check when the move is made
        since the max stack isn't doubled if the only empty pile is being moved to"""
        for pile in self.tableau:
            if len(pile) == 0:
                max_stack *= 2
                break
        return max_stack

    def move(self, source, target):
        """written by copilot. This is a placeholder for the move function."""
        if source == "deck":
            if target == "freecell":
                for pile in self.freecells:
                    if pile.is_empty():
                        pile.add(self.deck.pop())
                        break
            elif target == "tableau":
                for pile in self.tableau:
                    if pile.is_empty():
                        pile.add(self.deck.pop())
                        break
        elif source == "freecell":
            if target == "tableau":
                for pile in self.tableau:
                    if pile.is_empty():
                        pile.add(self.freecells.pop())
                        break
            elif target == "foundation":
                for pile in self.foundations:
                    if pile.is_empty():
                        pile.add(self.freecells.pop())
                        break
        elif source == "tableau":
            if target == "tableau":
                for pile in self.tableau:
                    if pile.is_empty():
                        pile.add(self.tableau.pop())
                        break
            elif target == "foundation":
                for pile in self.foundations:
                    if pile.is_empty():
                        pile.add(self.tableau.pop())
                        break
        elif source == "foundation":
            if target == "tableau":
                for pile in self.tableau:
                    if pile.is_empty():
                        pile.add(self.foundations.pop())
                        break
            elif target == "freecell":
                for pile in self.freecells:
                    if pile.is_empty():
                        pile.add(self.foundations.pop())
                        break

    def is_won(self):
        '''Returns True if the game is won, False otherwise.
        This code was written by copilot. Logic to check a win condition is not implemented yet.'''
        for pile in self.foundations:
            if pile.is_empty():
                return False
        return True

    def __str__(self):
        return f"Deck: {self.deck}\nTableau: {self.tableau}\nFreecells: {self.freecells}\nFoundations: {self.foundations}"


# deck = Deck()
# print(deck.cards)
# print(deck)
# deck.shuffle()
# print("Shuffled deck:")
# print(deck)

frecell = FreeCellGame()
print(frecell)

for stack in frecell.tableau:
    print(len(stack))