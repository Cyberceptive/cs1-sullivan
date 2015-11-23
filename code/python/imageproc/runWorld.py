import pygame as pg


def newDisplay(win_width, win_height, win_caption):
    global clock, displaySurface, dirtyRects
    pg.init()
    pg.display.set_caption(win_caption)
    displaySurface = pg.display.set_mode((win_width, win_height))
    displaySurface.convert()
    clock = pg.time.Clock()
    dirtyRects = []


def runWorld(initState, updateState, updateDisplay, endState, frameRate, handleMouseDown, handleMouseUp, handleKeyDown, handleKeyUp, handleMouseMove):
    done = False
    currentState = initState
    while not done:
        updateDisplay(currentState)
        if (endState(currentState)):
            done = True
            break
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                done = True
                break
            elif (event.type == pg.MOUSEBUTTONDOWN and handleMouseDown != None):
                print(event)
                currentState = handleMouseDown(currentState, event.pos, event.button)
            elif (event.type == pg.MOUSEBUTTONUP and handleMouseUp != None):
                currentState = handleMouseUp(currentState, event.pos, event.button)
            elif (event.type == pg.KEYDOWN and handleKeyDown != None):
                currentState = handleKeyDown(currentState, event.unicode, event.key, event.mod)
            elif (event.type == pg.KEYUP and handleKeyUp != None):
                currentState = handleKeyUp(currentState, event.key, event.mod)
            elif (event.type == pg.MOUSEMOTION and handleMouseMove != None):
                currentState = handleMouseMove(currentState, event.rel, event.buttons)
        currentState = updateState(currentState)
        clock.tick(frameRate)
    pg.quit()

