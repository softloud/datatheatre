import pygame as pg

def make_ui():
    font = pg.font.SysFont("Courier", 40)



    button_a = font.render("A", True, (0,0,0))
    button_a_rect = button_a.get_rect(
    center = (display_width * 0.4, display_height * 0.9))

    button_b = font.render("A", True, (0,0,0))
    button_b_rect = button_a.get_rect(
    center = (display_width * 0.6, display_height * 0.9))

class Button:
    def __init__(self, x, y, img, background):
        
        # set self properties
        self.image = pg.image.load(img).convert()
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        
    def render(self, background):
        background.blit(self.image, (self.x, self.y))
            
 #       def img
        
            # get image conditional on which_button and status
            # need a dataframe indexed by which button and status
            # value is png location  
  #          img = # write code here        
