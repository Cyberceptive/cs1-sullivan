import pygame as pg
import runWorld as rw

def loadImage(filename):
    imageSurface = pg.image.load(filename)
    imageSurface.convert()
    return imageSurface


def makeLabel(content, typeface, size, color):
    font = pg.font.SysFont(typeface, size)
    return font.render(content, size, color)


def erase():
    for rect in rw.dirtyRects:
        rw.displaySurface.fill(black, rect)
#        print("Cleaned" + str(rect))
    pg.display.update(rw.dirtyRects)
    rw.dirtyRects = []

def fill(color):
    rw.displaySurface.fill(color)


def draw(image_surf, loc):
    rw.displaySurface.blit(image_surf, loc)
    rw.dirtyRects.append(image_surf.get_bounding_rect().move(loc))
#    print("Dirtied" + str(surf.get_bounding_rect().move(loc)))


def flush():
    pg.display.update(rw.dirtyRects)


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
