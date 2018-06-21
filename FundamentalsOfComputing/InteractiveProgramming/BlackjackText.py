#Blackjack Textgame in preparation for the mini-project
import random

deck=[]
for i in range(4):
    deck.extend(range(1,14))  
    
def new_game():
    global wins, deck, losses, cont_gen
    wins=0
    losses=0
    cont_gen=0
    random.shuffle(deck)
    dealer_hand=[]
    user_hand=[]
    play='y'

new_game()
    
while True:
    n=0
    while True:
        cont=0
        if n==0:
            user_hand=[]
            dealer_hand=[]
            for i in deck:
                if cont==0 or cont==2:
                    user_hand.append(i)
                elif cont==1 or cont==3:
                    dealer_hand.append(i)
                if cont>=4:
                    break
                cont=cont+1
            user_total=user_hand[n]+user_hand[n+1]
            dealer_total=dealer_hand[n]+dealer_hand[n+1]
        else:
            if choice=='h':
                user_hand.append(deck[n])
            if dealer_total<17:
                dealer_hand.append(deck[n])
            user_total=user_total+user_hand[n]
            dealer_total=dealer_total+dealer_hand[n]
        print str(user_hand)+ 'your count is: ', user_total
        print dealer_hand[1:]
            
        if user_total==21 and dealer_total==21:
            print 'Its a tie'
            break
        elif user_total==21:
            print 'BLACKJACK! You Win'
            wins=wins+1
            break
        elif dealer_total==21:
            print 'Dealer got Blackjack, Dealer Wins'
            losses=losses+1
            break
        elif user_total>21 and dealer_total<21:
            print 'You were busted'
            losses=losses+1
            break
        elif user_total<21 and dealer_total>21:
            print 'Dealer got busted'
            wins=wins+1
            break
        elif user_total>21 and dealer_total>21:
            if user_total-21 < dealer_total-21:
                print 'You Win!'
                wins=wins+1
                break
            elif user_total-21 > dealer_total-21:
                print 'Dealer Wins'
                losses=losses+1
                break
            elif user_total==dealer_total:
                print 'Its a tie'
                break 
        if dealer_total>=17 and dealer_total<21:
            if n>=1:
                if choice=='s':
                    if user_total-21 < dealer_total-21:
                        print 'You Win!'
                        wins=wins+1
                    elif user_total-21 >dealer_total-21:
                        print 'Dealer Wins'
                        losses=losses+1
                    elif user_total==dealer_total:
                        print 'Its a tie'
                    break
            
        choice=raw_input('Hit or Stand? h/s?')
        
        n=n+1
    play= raw_input('Deal? y/n')
    random.shuffle(deck)

        
        
        
        
        
        
