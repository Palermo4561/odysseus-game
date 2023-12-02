import pygame as pg 
import sys
from pygame import gfxdraw
from dictionaries import *

def check_button_collisions(buttons:list) -> int:
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


def multiline_text(text:str, size:int, width:int=False, /, \
                    font_type:str=None, color:str='black', **kwargs) -> None:
    """Renders and displays multiple lines of text for PyGame

Parameters:
    text: the text to be displayed
    size: the size of the text
    width: width of the text lines before a new line starts 
    font_type: type of font to be rendered, default of None
    color: color of the text 
    kwargs: must specify a center point with a coordinate, as you would with pg.Surface.get_rect()"""


    if not width: 
        width = pg.display.get_window_size()[0]

    font = pg.font.Font(font_type, size)
    
    max_characters = width // (size / 2.9)

    if len(text) > max_characters:

        new_text = ""
        line = ""
        words = text.split(" ")

        while len(words) > 0:
            n = 0

            while n < len(words) and len(line + (word := f" {words[n]}")) < max_characters:
                line += word
                n += 1
            
            new_text += line + '\n'
            line = ""
            words = words[n:]
        
        text = new_text[:-1]
    
    if 'topleft' in kwargs:
        for n, line in enumerate(text.split('\n')):
            line_text = font.render(line, True, color)
            pg.display.get_surface().blit(line_text, line_text.get_rect(topleft=(kwargs['topleft'][0], kwargs['topleft'][1] + size * n)))
   
    elif 'center' in kwargs:
        num_split = text.count('\n')
        for n, line in enumerate(text.split('\n')):
            line_text = font.render(line, True, color)
            pg.display.get_surface().blit(line_text, line_text.get_rect(center=(kwargs['center'][0], kwargs['center'][1] + size * n - (num_split / 2) * size)))
   
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



def draw_circle_alpha(color:str, center:tuple, radius:int|float) -> None:
    target_rect = pg.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pg.Surface(target_rect.size, pg.SRCALPHA)
    pg.draw.circle(shape_surf, color, (radius, radius), radius)
    pg.display.get_surface().blit(shape_surf, target_rect)



def thick_aa_circle(center:tuple|list, radius:float, color_hex_value:str, thickness:int) -> None:
    """Draws multiple aacircles to make one thick aacircle

Parameters:
    center: center point
    radius: radius of the circle
    color_hex_value: hex color of the circle
    thickness: thickness of the line"""

    screen = pg.display.get_surface()

    for i in range(-thickness // 2, thickness // 2):
        if (r := int(radius + i)) > 0 :
            for __ in range(10):
                gfxdraw.aacircle(screen, *(map(lambda x : int(x), center)), r, pg.Color(color_hex_value))



def calculate_waypoint_coords(scene:int) -> tuple:

    screenX, screenY = pg.display.get_window_size()

    loc = scene_locations[scene]

    cx = int(loc[0] / 160 * screenX) + screenX / 320
    cy = int(loc[1] / 90 * screenY) + screenY / 180

    return cx, cy



def calculate_boat_coords(scene:int) -> tuple:

    screenX, screenY = pg.display.get_window_size()

    loc = spawn_locations[scene]

    cx = int(loc[0] / 160 * screenX) + screenX / 320
    cy = int(loc[1] / 90 * screenY) + screenY / 180

    return cx, cy