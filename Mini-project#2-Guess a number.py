# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

chooce = 100
guess_time = 7
# helper function to start and restart the game
def new_game(): 
    global secret_number
    global guess_time
    if chooce == 100:
        secret_number = random.randrange(0,100)
        guess_time = 7
        print 'New game. Range is from 0 to 100'
        print 'Number of remaining guesses is',guess_time
    else:
        secret_number = random.randrange(0,1000)
        guess_time = 10
        print 'New game. Range is from 0 to 100'
        print 'Number of remaining guesses is',guess_time
    frame.start()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global chooce
    chooce = 100
    new_game()
    print 'Now range 0 - 1000' 

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global chooce
    chooce = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here	
    n = int(guess)
    print
    print 'Guess was',n
    global guess_time
    
    if n != secret_number:
        if guess_time == 1:
            print 'You ran out of guesses. The number was',secret_number
            print
            new_game()
        else:
            guess_time -= 1
            print 'Number of remaining guesses is',guess_time
            if n < secret_number:
                print 'Higher!'
            else:
                print 'Lower!'
    else:
        print 'Correct!'
        print 'Wins'
        print 
        new_game()
      
  
# create frame
frame = simplegui.create_frame('Guess a number',300,300) 

# register event handlers for control elements and start frame
inp = frame.add_input('Guess a number',input_guess, 100)
button1 = frame.add_button('Range: 0 - 100',range100, 100)
button2 = frame.add_button('Range: 0 - 1000',range1000, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
