import random
def name_to_number(name):
    if name=='rock':
        number=1
    elif name=='spock':
        number=2
    elif name=='paper':
        number=3
    elif name=='lizard':
        number=4
    elif name=='scissors':
        number=5
    else:
        print 'Error, Incorrect input. Please select any of the options given'
        number= None
    return number
    
def number_to_name(number):
    if number==1:
        name='rock'
    elif number==2:
        name='spock'
    elif number==3:
        name='paper'
    elif number==4:
        name='lizard'
    elif number==5:
        name='scissors'
    else:
        print 'Error, Incorrect input. Please select any of the options given'
    return name
 
 def is_num_conv(n):
    try:
        n=int(n)
        return n
    except:
        return str(n)

def rpsls(player):
    print '\n'
    if player<=5:
        player=number_to_name(player)        
    computer=random.randrange(1,6)
    print 'Player chooses '+ player
    print 'Computer chooses ' + number_to_name(computer)
    player= name_to_number(player) 
    if player!=computer:
        if computer==1:
            decision=computer-player
            decision=decision*(-1)
            if decision<=2:
                print 'player wins'
            else:
                print 'computer wins'                
        elif player!=1:
            if player==2 and computer==5:
                print 'player wins'
            elif (player-computer)>0:
                print 'player wins'
            elif (player-computer)<0:
                print 'computer wins'
        else:
            decision=player-computer
            decision=decision*(-1)
            if decision<=2:
                print 'computer wins'
            else:
                print 'player wins'
    else:
        print 'Tie!!'
    
player_choice= raw_input('Choose between rock(1), spock(2), paper(3), lizard(4) or scissors(5) (Either number or string, Note that it is case-sensitive):')
player_choice= is_num_conv(player_choice)
rpsls(player_choice)


