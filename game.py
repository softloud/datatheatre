import pygame as pg
import pygame_menu
from pygame_menu import themes
import pandas as pd
import numpy as np
from janitor import clean_names


# game modules
import game_fns
import ui_fns

# Set win conditions
completion_key = game_fns.set_completion_params(3,3)


# Get game text images
text_img = pd.read_csv("game-data/game-text-meta.csv")
text_img.head()
text_files = text_img.file_path.to_list()

# get game event meta information
event_key = clean_names(pd.read_csv("things-to-fiddle-with/game-event-key.csv"))

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
# ui_fns.make_ui()

button_a = ui_fns.Button(int(display_width * 0.4),
                         int(display_height * 0.9),
                         text_files[0],
                         background
)

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
            
            if button_a.rect.collidepoint(event.pos) == True:
                # update terminal text
                # update event name to outcome
                game_fns.button_press("A", "meeting", event_key)

            #if button_b_rect.collidepoint(event.pos) == True:
                # update terminal text
             #   button_press("B", "meeting", event_key)

        # output terminal text        
        background.blit(terminal_text, (display_width * 0.2, display_height * 0.2))
        
        # buttons
        button_a.render(background)
      
        
        # if rect.collidepoint(event.pos)
                
        # From here is template, don't understand, don't touch
        pg.display.update()

        # flip() the display to put your work on screen
        # pg.display.flip()

        clock.tick(60)  # limits FPS to 60

pg.quit()