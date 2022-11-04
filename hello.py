import pygame
import Sprites
import Constants
from Constants import *
import states

#this is a new comment


#Initalise pygame and window
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
#current_state = states.Game()
current_state = states.TitleScreen()
print("hello")
#Game loop
while current_state.running:
    #handle input
    if current_state.next_state:
        current_state = current_state.next_state
    events = pygame.event.get()
    for event in events:

        current_state.handle_event(event)
    #game logic
    current_state.update()
    #drawing
    current_state.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)


#Quit
pygame.quit()
