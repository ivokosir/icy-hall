from helper import *
import pygame

new_inputs = R(is_forward=True, jump=False)

def collect(inputs, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            inputs.jump = True
        elif event.key == pygame.K_LEFT:
            inputs.is_forward = False
        elif event.key == pygame.K_RIGHT:
            inputs.is_forward = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            inputs.jump = False

    return inputs
