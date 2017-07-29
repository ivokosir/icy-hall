from helper import *
from rect import Rect

import pygame
import update

screen_w, screen_h = (1200, 700)
border_w, border_h = (0, 100)

def world_to_screen(point):
    x, y = point
    return (
        x/update.world_w*(screen_w-border_w),
        y/update.world_h*(screen_h-border_h)
    )

def draw_rect(screen, color, rect):
    screen_x, screen_y = world_to_screen((rect.x, rect.y))
    screen_w, screen_h = world_to_screen((rect.w, rect.h))
    rect = (
        border_w/2 + screen_x, border_h/2 + screen_y,
        screen_w, screen_h
    )
    pygame.draw.rect(screen, color, rect)

def block(color, rect):
    return R(color=color, rect=rect)

def group(*children, rect=Rect(0,0,0,0)):
    return R(children=children, rect=rect)

def draw_item(screen, x, y, i):
    r = i.rect
    children = i.children
    color = i.color
    if children is not None:
        for c in i.children:
            draw_item(screen, x+r.x, y+r.y, c)
    elif color is not None:
        offset_r = r.copy()
        offset_r.x += x
        offset_r.y += y
        draw_rect(screen, i.color, offset_r)

def draw(screen, game):
    platform_blocks = [block(0X222222, p) for p in game.platforms]

    root = group(
        group(*platform_blocks),
        block(0X3333FF, update.player_rect(game.player)),
        rect=Rect(update.world_w/2-game.player.x, update.world_h/2-game.player.y, 0, 0)
    )

    screen.fill(0XEEEEEE)
    draw_item(screen, 0, 0, root)
