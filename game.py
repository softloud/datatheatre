import pygame as pg
import pygame_menu
from pygame_menu import themes
import pandas as pd
import numpy as np
from janitor import clean_names

# game modules
from game_fns import set_completion_params, button_press

# Set win conditions
completion_key = set_completion_params(3,3)


# Get game text images
text_img = pd.read_csv("game-text-meta.csv")
text_img.head()
text_files = text_img.file_path.to_list()

# get game event meta information
event_key = clean_names(pd.read_csv("game-event-key.csv"))

# pg setup
pg.init()

# Set game background size to full screen
infoObject = pg.display.Info()

# Set width and height of game display
display_width = infoObject.current_w
display_height = infoObject.current_h

# Create background
background = pg.display.set_mode((display_width, display_height))

# Window header
pg.display.set_caption("Data Theatre")

clock = pg.time.Clock()
running = True

# game variables
started = False
event_name = "invited to start"
outcomes = []

# UI 
font = pg.font.SysFont("Courier", 40)
button_a = font.render("A", True, (0,0,0))
button_a_rect = button_a.get_rect(
    center = (display_width * 0.4, display_height * 0.9))

button_b = font.render("A", True, (0,0,0))
button_b_rect = button_a.get_rect(
    center = (display_width * 0.6, display_height * 0.9))


# Game
while running:
    # from template
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
                
        if started == False:        
            # start game prompt
            terminal_text = pg.image.load(text_files[0]).convert()

    # user starts game
        if event.type == pg.MOUSEBUTTONDOWN and started == False:
            started = True
            print("mouse button clicked")
            terminal_text = pg.image.load(text_files[1]).convert()
        # test click
        if event.type == pg.MOUSEBUTTONDOWN and started == True:
            terminal_text = pg.image.load(text_files[2]).convert()
            
            if button_a_rect.collidepoint(event.pos) == True:
                button_press("A", "meeting", event_key)

            if button_b_rect.collidepoint(event.pos) == True:
                button_press("B", "meeting", event_key)

        # output terminal text        
        background.blit(terminal_text, (display_width * 0.2, display_height * 0.2))
        
        # buttons
        pg.draw.rect(background, "grey", button_a_rect)  
        background.blit(button_a, button_a_rect)          

        pg.draw.rect(background, "grey", button_b_rect)  
        background.blit(button_a, button_b_rect)          
      
        
        # if rect.collidepoint(event.pos)
                
        # From here is template, don't understand, don't touch
        pg.display.update()

        # flip() the display to put your work on screen
        # pg.display.flip()

        clock.tick(60)  # limits FPS to 60

pg.quit()