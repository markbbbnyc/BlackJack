'''
Udemy Python Course Milestone 2 Challange to create a Black Jack game with the following assumtions:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. You can not just use functions in your game.
    Use classes to help you define the Deck and the Player's hand. There are many right ways to do this,
     so explore it well!
'''

# defining the deck with 52 cards, no spaids all the same we ar enot considering any special
# moves like splitting. will have to import shuffle to randomize deck. will then
# .pop off all drawn cards trhrough the game

import random

class Deck():
    def __init__(self):
        self.bj_deck = [
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        '2','3','4','5','6','7','8','9','10','J','Q','K','A',
        ]
# defining Player Class which has a bankroll of money they can start playing withself.
# Player can only play of bankroll > 0

class Player():
    def __init__(self,bankroll):
        self.bankroll = int(bankroll)
        self.hand = []
        self.score = 0

# defining class of Dealer -

class Dealer():
    def __init__(self,bank):
        self.bank = int(bank)
        self.hand = []
        self.score = 0

def calcscore(player_dealer):
    myscore = 0
    for x in player_dealer.hand:
        if x in ['J','Q','K']:
            myscore = myscore + 10
            continue
        if x == 'A' and ((myscore + 10) >= 21):
            myscore = myscore + 1
            continue
        if x == 'A' and ((myscore + 10) < 21):
            myscore = myscore + 10
            continue
        myscore = myscore + int(x)
    player_dealer.score = myscore


# assigning Dealier and Player, bankrolling both

my_dealer = Dealer(1000)
my_player = Player(100)

gamenotover = True
again = True

while again:
    # initializing Game, creating Deck to play and shuffling cards
    gamenotover = True
    again = True
    my_player.hand = []
    my_dealer.hand = []
    my_deck = Deck()
    random.shuffle(my_deck.bj_deck)
    # starting Game - first Player then Dealer, both get two cards

    bet = int(input(f'Your balance is {my_player.bankroll}. Player, place your bet:  '))


    my_player.hand.append(my_deck.bj_deck.pop())
    my_dealer.hand.append(my_deck.bj_deck.pop())
    my_player.hand.append(my_deck.bj_deck.pop())
    my_dealer.hand.append(my_deck.bj_deck.pop())

    calcscore(my_player)
    calcscore(my_dealer)

    print('Dealer holds: ',my_dealer.hand, 'Score: ',my_dealer.score)
    print('Player holds: ',my_player.hand, 'Score: ',my_player.score)


    while True:
        move = input("Player, do you want to Hit or Stay? [H,S]: ")
        if move.upper() == 'H':
            my_player.hand.append(my_deck.bj_deck.pop())
            calcscore(my_player)
            print('Dealer holds: ',my_dealer.hand, 'Score: ',my_dealer.score)
            print('Player holds: ',my_player.hand, 'Score: ',my_player.score)
        if my_player.score > 21:
            print('Player, you are bust and lose the game and your bet')
            my_player.bankroll = my_player.bankroll - bet
            gamenotover = False
            break
        if my_player.score == 21:
            print('Player, you score 21. Congratulations. Dealers turn')
            gamenotover = True
            break
        if move.upper() == 'S':
            gamenotover = True
            break

    while my_dealer.score < my_player.score and gamenotover:
        my_dealer.hand.append(my_deck.bj_deck.pop())
        calcscore(my_dealer)
        print('Dealer holds: ',my_dealer.hand, 'Score: ',my_dealer.score)
        print('Player holds: ',my_player.hand, 'Score: ',my_player.score)

        if my_dealer.score > 21:
            print('Dealer, you are bust and lose the game. Pay up')
            my_player.bankroll = my_player.bankroll + bet
            break
        if my_player.score <= my_dealer.score:
            print('Player, tough luck. The Bank wins')
            my_player.bankroll = my_player.bankroll - bet
            break

    print('=======================')
    print('Player balance: ', my_player.bankroll)
    print('=======================')

    if my_player.bankroll > 0:
        if input('You want to go again [Y|N]? ').upper() == 'Y':
            again = True
            continue
        else:
            again = False
            break
    else:
        print('Sorry you are broke. Good luck next time.')
        again = False
        break

print('Thank you for playing.')
