import pygame as pg 
from button import Button
import sys

def check_button_collisions(buttons:list[Button]) -> int:
    """Checks all buttons to see if any of them are colliding with the mouse

Parameters:
    buttons: list of buttons for be iterated over
    
Return: 
    int: self.pos value of the button, or 0 if no button is colliding"""

    for button in buttons:
        if (pos := button.mouse_collides()):
            return pos
    
    return 0


def end() -> None:
    """Ends the program"""
    
    pg.quit()
    sys.exit()



def multiline_text(text:str, size:int, **kwargs) -> None:
    """Renders and displays multiple lines of text for PyGame

Parameters:
    text: the text to be displayed
    size: the size of the text
    kwargs: must specify a center point with a coordinate, as you would with pg.Surface.get_rect()"""
   
    font = pg.font.Font(None, size)


    if 'topleft' in kwargs:
        for n, line in enumerate(text.split("\n")):
            line_text = font.render(line, True, 'black')
            pg.display.get_surface().blit(line_text, line_text.get_rect(topleft=(kwargs['topleft'][0], kwargs['topleft'][1] + size * n)))
   
    elif 'center' in kwargs:
        for n, line in enumerate(text.split("\n")):
            line_text = font.render(line, True, 'black')
            pg.display.get_surface().blit(line_text, line_text.get_rect(center=(kwargs['center'][0], kwargs['center'][1] + size * n)))
   
    else:
        raise ValueError("No starting point for text specified")


def pixel_scale(surface:pg.Surface, *, fullscreen:bool=False, scale:float=1) -> pg.Surface:
    """Returns a surface with the adjusted scale based on the screen size 
    
Parameters: 
    surface: surface to be adjusted
    fullscreen: optional boolean indicating if the image is the entire screen or not
    scane: optional float to allow the surface to not be limited to a 1:1 ratio
    
Return:
    pg.Surface: new scaled surface from the origional surface"""

    screenX, screenY = pg.display.get_window_size()

    if fullscreen: 
        return pg.transform.scale(surface, (screenX, screenY))
    
    factorX = (surface.get_width() / 160) * scale
    factorY = (surface.get_height() / 90) * scale
    
    return pg.transform.scale(surface, (screenX * factorX, screenY * factorY))
