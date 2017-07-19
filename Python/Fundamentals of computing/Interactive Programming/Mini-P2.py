# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global computer
    computer = random.randrange(0,100)
    global remaining_g 
    remaining_g= 7
    


# define event handlers for control panel
def range100():
    new_game()
    # button that changes the range to [0,100) and starts a new game
    print 'New Game, Range: [0,100], Guesses: ', remaining_g


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global computer
    computer=random.randrange(0,1000)
    global remaining_g
    remaining_g=10
    print 'New Game, Range: [0,1000], Guesses: ', remaining_g


    
    
    
def input_guess(guess):
    # main game logic goes here
    global remaining_g
    guess=int(guess)
    remaining_g=remaining_g-1
    if guess<computer and remaining_g>=0:
        print 'Higher!'
        print 'Your guess was: ', guess
        print 'Remaining guesses: ', remaining_g
        print '\n'
    elif guess>computer and remaining_g>=0:
        print 'Lower!'
        print 'Your guess was: ', guess
        print 'Remaining guesses: ', remaining_g 
        print '\n'
    elif guess==computer and remaining_g>=0:
        print 'You win!'
        print 'Your guess was: ', guess
        print '\n'
    else:
        print 'You lose :('
        print '\n'

    
# create frame
f=simplegui.create_frame('Guess the Number', 300, 300)

# register event handlers for control elements and start frame
f.add_button('Range [0,100]', range100, 200)
f.add_button('Range [0,1000]', range1000, 200)
f.add_input('Your Guess ', input_guess, 200)

# call new_game 
new_game()

f.start()

