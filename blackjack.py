import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen")
values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""  
        for card in self.deck:
            deck_comp += "\n " + card.__str__()  
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = [] 
        self.value = 0  


    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter [h/s] ")

        if x[0].lower() == "h":
            hit(deck, hand)  

        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Invalid input. Please enter [h/s].")
            continue
        break


def show_some(player, dealer):
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])


def show_all(player, dealer):
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)


def player_busts(player, dealer):
    print("\nPlayer busts!")


def player_wins(player, dealer):
    print("\nPlayer wins!")


def dealer_busts(player, dealer):
    print("\nDealer busts! You win!")


def dealer_wins(player, dealer):
    print("\nDealer wins!")


def push(player, dealer):
    print("\nIt's a tie!")


while True:
    print("Welcome to BlackJack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        print("Final Results:")
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)

    new_game = input("\nPlay another hand? Enter yes [y] or no [n]: ")
    while new_game.lower() not in ["y", "n"]:
        new_game = input("Invalid input. Please enter [y] or [n]: ")
    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break