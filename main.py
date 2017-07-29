#!/usr/bin/env python3

from helper import *
import collect
import draw
import pygame
import update

def start(game, inputs_record):
    pygame.init()

    screen = pygame.display.set_mode(
        (draw.screen_w, draw.screen_h)
    )
    pygame.display.set_caption("ice-hall")

    clock = pygame.time.Clock()
    millis = 1
    exit = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit = True
            else: inputs_record = collect.collect(inputs_record, event)

        if exit: break

        game = update.update(game, inputs_record, millis/1000)

        draw.draw(screen, game)

        pygame.display.flip()
        millis = clock.tick(60)

    pygame.quit()

start(update.new_game, collect.new_inputs)
