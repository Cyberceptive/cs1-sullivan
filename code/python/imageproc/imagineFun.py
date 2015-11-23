import drawWorld as dw
import image_processing as ip

# This module provides the menu and associated functions
# for our imaging application. Start by reading the menu
# definition (a dictionary mapping keyboard characters to
# functions) at the end of the file. The functions in this
# dictionary are defined in the code that follows.

################################################################

# exit: state -> state
# sets runDone flag to true so app will exit
#
def exit(state):
    state['runDone'] = True
    return state

################################################################

# reset: state -> state
# resets processed image to original
#
def reset(state):
    state['processed'] = state['original'].copy()
    state['needsDisplayUpdate'] = True
    return state

################################################################

# negative: state -> state
# applies invert operation to processed image
#
def negative(state):
    (ip.invert)(state['processed'])
    state['needsDisplayUpdate'] = True
    return state

################################################################

# load: state -> state (IO)
# loads new "original" "image from file, copy in "processed"
# 
def load(state):
    print("Enter name of image file to load: ")
    imageName = input()
    resetImage = dw.loadImage(imageName)
    state['original'] = resetImage
    state['processed'] = state['original'].copy()
    state['needsDisplayUpdate'] = True
    return state

################################################################

# save: state -> state (IO)
# saves processsed image to file
# stubbed out
#
def save(state):
    return state

################################################################

# function to run on keypress for keys that do not correspond
# to menu items
def badChoice(state):
    print("Bad choice, try again")
    return state

################################################################

# A menu simply associated functions to call with menu items.
# Here the menu is just a set of single-character commands. We
# represent the menu as a dictionary from characters to functions
# that should be run when those commands are given by the user.
# The characters are encoded as 8-bit non-negative integers, 
# from 0 to 255 (an ""ASCII"" encoding). Comments in the following
# definition indicate which characters the numbers encode.
#
menu = {
    120 : exit,      # x
    110 : negative,  # n
    114 : reset,     # r
    108 : load,      # l
    115 : save       # s
    }

