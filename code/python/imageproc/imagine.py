# from trepan.api import debug

# import pdb
# pdb.set_trace()

import pygame as pg
import runWorld as rw
import drawWorld as dw
import image_processing as ip
import imagineFun as af

################################################################

# Initialize display

name = "Imaginator!"
width = 1200
height = 500
rw.newDisplay(width, height, name)

################################################################

# An image that we'll use when the system starts

initImage = dw.loadImage("cat.bmp")

# In our initial exercise with this simulation framework, we
# represented the "game state" as a tuple. A problem with that
# approach is that it doesn't give us good names for the fields
# of the tuples (records), so we end up with lots of cryptically
# subscripted tuple values, make it hard to write, reason about,
# debug, and enhance the code. We could of course write our own
# nicely named projection functions, and that would help. This
# is what we did in Idris, where we wrote functions such as
# first (fst) and second (snd) to extract fields from tuples.
# We then saw that the *record* construct enabled us to define
# tuple types with *named* fields. The compiler then provided
# projection functions with the names of the fields, making it
# much easier to write code where the intended interpretation
# is clarified by the use of meaningful field names.
#
# We now take one step on a path to fixing the same problem in
# Python. The idea we introduce now is to use a dictionary to
# represent a tuple with named fields. To access a field, we just
# do a lookup in the dictionary.


# To illustrate this idea, we define the initial state of our
# image processing system, implicitly defining the tuple type
# that will represent the state of our application. Here are the
# fields and their meanings:
#
# runDone -- Boolean, True if "exit" selected, ends run
# needsDisplayUpdate -- set to True when display update neede
# original -- the image that's being worked on
# processed -- a copy of original, subject to editing fuitcnons


initState = {
    'runDone': False,
    'needsDisplayUpdate': True,
    'original': initImage,
    'processed': initImage.copy()
    }

################################################################

# updateDisplay: state -> image (IO)
# if display update needed, render both images, otherwise "skip"
#
def updateDisplay(state):
#    print("Updating display with state = ", state)
    if (state['needsDisplayUpdate'] == True):
        dw.erase()
        dw.draw(state['original'], (0,0))
        dw.draw(state['processed'], (((state['original']).get_size())[0],0))
        dw.flush()
        state['needsDisplayUpdate'] = False


################################################################

# updateState: state -> state
# "no-op" in this application (this is not a simulation)
# i.e., this is just identity function on state type 
#
def updateState(state):
    return state

################################################################

# endState: state -> bool
# return True to quit pygame if runDone has been set to True
#
def endState(state):
    return state['runDone']

################################################################

# handleMouseDown: state -> event -> state
# Just a stub to illustrate possibility of handling mouse events
#
#
def handleMouseDown(state, pos, button):  
    return(state)

# handleKeyDown: state -> state
# run command designated by user or "badChoice" if no such command
#
def handleKeyDown(state, unicode, key, mod):
    print("Key pressed: ", key)

    # note that Python dictionary supports "get" command. It's a
    # lookup with an optional second argument that specifies what
    # the result of the lookup should be if the key is not present
    # in the dictionary. So the following command gets the function
    # designated by the given character, or "badChoice" if there
    # isn't one.
    #
    funcToRun = af.menu.get(key, af.badChoice)

    # Run the selected function!
    #
    # Quiz: Why do we not have to write: state = funcToRun(state)?
    #
    funcToRun(state)
    return(state)

################################################################

# Refresh screen at intended 20FPS
frameRate = 20

# Run the main event loop. Note that there is a change in
# the way you call runWorld: Instead of passing a single
# handleEvent function, you pass individual functions for
# handling different kinds of events; and if there is no
# need to handle particular kinds of events, you can just
# pass "None." The runWorld function makes sure that it
# does not try to call an event handler that is None. 
# 
# Make sure you see that we're passing initState off to
# runWorld, and that you understand that that is the state
# value that runWorld will pass back to the functions you
# define in this file.
#
rw.runWorld(initState, updateState, updateDisplay, endState, frameRate, handleMouseDown, None, handleKeyDown, None, None)
