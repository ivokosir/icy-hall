from helper import *
from rect import Rect

import rect
import math

world_w, world_h = (200, 100)
new_platforms = [
    rect.Rect(0, 50, 50, 5),
    rect.Rect(55, 10, 5, 100),
    rect.Rect(30, 0, 5, 40),
    rect.Rect(55, 40, 200, 5),
    rect.Rect(300, 45, 300, 5),
]
new_player = R(y=0, vy=0, x=10, vx=0)

new_game = R(platforms=new_platforms, player=new_player)

player_thickness = 5
platform_thickness = 5

def player_rect(player):
    return rect.Rect(
        player.x - player_thickness/2,
        player.y - player_thickness/2,
        player_thickness,
        player_thickness
    )

def intersection_direction(player_r, i):
    if i.w >= i.h:
        if abs(i.y - player_r.y) > player_r.h/2: return 'N'
        else: return 'S'
    else:
        if abs(i.x - player_r.x) > player_r.w/2: return 'W'
        else: return 'E'

def nudge_player(player, direction, platform):
    if direction == 'N':
        player.y = platform.y - player_thickness/2
    elif direction == 'S':
        player.y = platform.y + platform.h + player_thickness/2
    elif direction == 'W':
        player.x = platform.x - player_thickness/2
    elif direction == 'E':
        player.x = platform.x + platform.w + player_thickness/2


def update(game, inputs, delta):
    game.player.x += delta * game.player.vx
    game.player.y += delta * game.player.vy

    player_r = player_rect(game.player)

    intersections = [
        (rect.intersection(player_r, p), p) for p in game.platforms
    ]
    intersections = [
        (i, p, intersection_direction(player_r, i))
        for i, p in intersections if i is not None
    ]

    for intersection, platform, direction in intersections:
        nudge_player(game.player, direction, platform)

    directions = [d for i, p, d in intersections]

    if 'N' in directions and game.player.vy > 0: game.player.vy = 0
    if 'S' in directions and game.player.vy < 0: game.player.vy = 0
    if 'W' in directions and game.player.vx > 0: game.player.vx = 0
    if 'E' in directions and game.player.vx < 0: game.player.vx = 0

    if 'N' in directions:
        friction_a = 50
        friction_v = min(abs(game.player.vx), delta * friction_a)
        friction_direction = 1.0 if game.player.vx < 0 else -1.0
        game.player.vx += friction_direction * friction_v
    else:
        gravity_a = 100
        game.player.vy += delta * gravity_a

    if inputs.jump:
        if 'N' in directions:
            game.player.vy = -50
            jump_direction = 1.0 if inputs.is_forward else -1.0
            game.player.vx += jump_direction * 50
        if 'W' in directions:
            game.player.vy = -50
            game.player.vx = -50
        if 'E' in directions:
            game.player.vy = -50
            game.player.vx = 50

    return game
