# Created by: Jenny Trac
# Group members: Sydney, Francisco
# Created on: Oct 3 2017
# This program asks you to the guess the number it's thinking

import ui
from numpy import random

# get random number
number_to_guess = random.randint(1, 10)

# show random number for testing
print(number_to_guess)

def guess_the_number_touch_up_inside(sender):
    # function checks if the number you guessed is right
    
    # input
    input_number = int(view['number_textfield'].text)
    
    # process
    
    # output
    if input_number == number_to_guess:
        view['answer_label'].text = "You guessed it right!"
    else:
        view['answer_label'].text = "Sorry the number is " + str(number_to_guess)

view = ui.load_view()
view.present('sheet')
