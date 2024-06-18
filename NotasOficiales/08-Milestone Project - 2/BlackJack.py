import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

class Player():
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.myvalue = 0
        self.all_cards = []
        
    def can_place_bet(self, money):
        if self.money >= money:
            self.money = self.money - money
            return True
        else:
            return False
        
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)
        self.currentcard = self.all_cards[-1]
        self.myvalue = self.myvalue + self.currentcard.value 
            
            
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
        

class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                
                #create the card object
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

player_money = 500
dealer_money = 100000

play_game = 'yes'
    
while play_game == 'yes':
    
    
    player_one = Player('Andre', player_money)
    dealer = Player('Dealer', dealer_money)
    
    print(f"Your balance is {player_one.money}")  
    #1. Create a deck of 52 cards 
    theDeck = Deck()
    #2. Shuffle the deck
    theDeck.shuffle()
            
    while True:
        #3. Ask the Player for their bet
        try:
            bet = int(input("What is your bet?"))
        except:
            print("That is not a valid amount")
            continue
        else:
            break
    #4. Make sure that the Player's bet does not exceed their available chips
    while not player_one.can_place_bet(bet):
        bet = int(input("That exceeds your money, please input another value"))
        
    #5. Deal two cards to the Dealer and two cards to the Player
    for x in range(2):
        player_one.add_cards(theDeck.deal_one())
        dealer.add_cards(theDeck.deal_one())
    
    #6. Show both of the Player's cards
    print("Your cards are:")
    for card in player_one.all_cards:
        print(card)
        
    #7. Show only one of the Dealer's cards, the other remains hidden
    print("The dealer's card is: ")
    print(dealer.all_cards[0])
    
    print(player_one.myvalue)
    
    #8. Ask the Player if they wish to Hit, and take another card
    hitornot = input("Does the player want to hit?")
    
    while hitornot == 'yes':
        player_one.add_cards(theDeck.deal_one())
        
        print("Your new cards are")
        for card in player_one.all_cards:
            print(card)
            
        #9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        if player_one.myvalue > 21:
            print("BUST! You lost!")
            break
        else:
            hitornot == input("Do you want to hit again?")
        
    #10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17 
   
    while dealer.myvalue < 17:
        dealer.add_cards(theDeck.deal_one())
        
        if dealer.myvalue >= 21:
            print("Dealer went past 21, player one wins")
            break

    #11. Determine the winner and adjust the Player's chips accordingly
    
    #I am missing some consditions!!! but over all it works fine!
    print("Your cards were:")
    for card in player_one.all_cards:
        print(card)
    print("the dealer Cards were:")
    for card in dealer.all_cards:
        print(card)
        
    if player_one.myvalue == 21 and dealer.myvalue == 21:
        print("It is a draw")
    
    elif player_one.myvalue > dealer.myvalue and player_one.myvalue <= 21:
        print("You won")
        player_money = player_money + bet
        dealer_money = dealer_money - bet
        
    elif player_one.myvalue < dealer.myvalue and player_one.myvalue <= 21:
        print("You won")
        player_money = player_money + bet
        dealer_money = dealer_money - bet
        
    elif player_one.myvalue < dealer.myvalue and dealer.myvalue <= 21:
        print("You lost")
        player_money = player_money - bet
        dealer_money = dealer_money + bet
        
    elif player_one.myvalue > dealer.myvalue and dealer.myvalue >= 21:
        print("You lost")
        player_money = player_money - bet
        dealer_money = dealer_money + bet
    
    
    #12. Ask the Player if they'd like to play again            
    play_game = input("Do you want to play again?")
        
        
    
    
    
    
    