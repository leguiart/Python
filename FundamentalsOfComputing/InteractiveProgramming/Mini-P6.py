# Mini-project #6 - Blackjack

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, facedown=False):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        if facedown==True:
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	# create Hand object
        
    def __str__(self):
        # return a string representation of a hand
        s=""
        for i in self.hand:
            s=s+ ' ' + str(i)        
        return s

    def add_card(self, card):
        self.hand.append(card)# add a card object to a hand
        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value=0
        ace=False
        for cards in self.hand:                   
            for i,j in VALUES.items():                        
                if cards.get_rank()==i:
                    hand_value=hand_value+j        
                if cards.get_rank()=='A':
                    ace=True
        if ace is False:
            return hand_value  
        else:
            if hand_value+10<=21:
                return hand_value+10
            else:
                return hand_value
   
    def draw1(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        pos_ref=0
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0]=pos[0]+CARD_SIZE[0]
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for s in SUITS:
            for r in RANKS:
                c=Card(s,r)
                self.deck.append(c)
                # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        deal_c=self.deck.pop(len(self.deck)-1)
        return deal_c	# deal a card object from the deck
    
    def __str__(self):
        s=""
        for i in self.deck:
            s=s+ ' ' + str(i)        
        return 'Deck contains: ' +  s
    # return a string representing the deck      


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand,score
    n=0
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    while n<4:
        if n==0 or n==2:
            player_hand.add_card(deck.deal_card())
        elif n==1 or n==3:
            dealer_hand.add_card(deck.deal_card())
        n=n+1
    if in_play is True:
        score-=1
    in_play = True

def hit():
    global in_play, message, score
    # if the hand is in play, hit the player
    if in_play is True:        
    # if busted, assign a message to outcome, update in_play and score      
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value()==21:
            message= 'You have BLACKJACK'
            score+=1
            in_play= False
        elif player_hand.get_value()>21:
            message='You were busted'
            score-=1
            in_play= False
            
def stand():
    global in_play, message,score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play==True:
        while dealer_hand.get_value()<=17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value()>21:
            message= "Dealer's got busted"
            score+=1
        elif dealer_hand.get_value()<21:
            if player_hand.get_value() > dealer_hand.get_value():
                message='You Win!'
                score+=1
            else:
                message= 'Dealer Wins'
                score-=1
        elif dealer_hand.get_value()==21:
            message= 'Dealer Wins'
            score-=1
        elif dealer_hand.get_value()== player_hand.get_value():
            message= 'Tie, Dealer Wins'
            score-=1
    # assign a message to outcome, update in_play and score
    in_play=False
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw1(canvas, [70, 400])
    dealer_hand.draw1(canvas, [70, 150]) 
    canvas.draw_text('Black', (200, 60), 50, 'Black')
    canvas.draw_text('Jack', (320, 60), 50, 'Red')
    if in_play is True:
         card = Card("S", "A")
         card.draw(canvas, [70, 150], True)
         canvas.draw_text("Dealer's Hand", (70, 120), 30, 'Red')
         canvas.draw_text("Player's Hand", (70, 370), 30, 'Red')
         canvas.draw_text('Hit or Stand?', (300, 300), 30, 'White')
         canvas.draw_text("Player's hand value: "+str(player_hand.get_value()), (300,500), 30, 'White')         
    else:
        canvas.draw_text(message, (70, 137), 50, 'Red')
        canvas.draw_text('New Deal?', (70, 390), 50, 'Red')
        canvas.draw_text("Player's hand value: "+str(player_hand.get_value()), (300,500), 30, 'White')
        canvas.draw_text("Dealer's hand value: " + str(dealer_hand.get_value()), (300,550), 30, 'White')
    canvas.draw_text('Score: '+str(score),(470, 80), 30, 'Red')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric