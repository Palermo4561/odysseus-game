import pygame as pg
from button import *
import dictionaries
from functions import *
from boat import Boat

def game_screen(buttons:list[Button], scene:int) -> None:
    """Draws the main game screen

Parameters:
    buttons: list of the buttons to be rendered to the screen
    scene: scene number, indicated by an integer"""
    
    title_bar(scene)
    side_screen("super awesome\ndesctiption")
    main_screen(scene)
    for button in buttons:
        button.draw()



def map_screen(boat:Boat, img:pg.Surface) -> None:
    """Draws the map screen of Achilelus's journey

Parameters: 
    boat: player character Boat object
    img: map image to draw"""


    pg.display.get_surface().fill(pg.Color(0, 0, 0))
    

    pg.display.get_surface().blit(img, (0, 0))
    pg.display.get_surface().blit(boat.image, boat.rect)



def opening_screen(start_button:Button) -> None:
    """Draws the opening screen of the game

Parameters:
    start_button: button to start the program"""

    pg.display.get_surface().fill((0, 0, 0))
    start_button.draw()



def title_bar(scene:int) -> None:
    """Draws the title bar for the game screen
    
Parameters: 
    scene: scene number, indicated by an integer"""

    win = pg.display.get_surface()
    x, y = pg.display.get_window_size()
    title = dictionaries.scenes[scene]
    text = pg.font.Font('./Assets/General/Greek-Freak.ttf', 80).render(title, True, 'black')

    img = pixel_scale(pg.image.load('./Assets/General/text_background.png').convert_alpha())

    win.blit(img, (0, 0))
    win.blit(text, text.get_rect(center=(x//2, y//12 + 15)))



def side_screen(description:str) -> None:
    """Draws the side screen with the description
    
Parameters:
    description: words to overlap the side rectangle"""

    win = pg.display.get_surface()

    x, y = pg.display.get_window_size()
    rect = pg.Rect(0, y//5 - 2, x // 6, 4 * y // 5)
    pg.draw.rect(win, 'orange', rect)
    pg.draw.rect(win, 'black', rect, 3)

    multiline_text(description, 40, topleft=tuple(map(lambda z : z + x//200, rect.topleft)))



def main_screen(scene) -> None:
    """Draws the central screen of the scene

Parameters: 
    scene: scene number, indicated by an integer"""

    bg = pg.image.load(f"./Assets/Scene{scene}/background.png").convert_alpha()
    x, y = pg.display.get_window_size()

    bg = pg.transform.scale(bg, (2*x/3, 4*y/5))

    pg.display.get_surface().blit(bg, (x // 6, y // 5))






# these are not used yet, to be implemented 

def full_screen(button:Other_Button) -> None:
    """Draws the full screen button
    
Parameters:
    button: full screen Button object"""
    
    pg.draw.rect(pg.display.get_surface(), 'pink', pg.Rect(*button.center, *button.dim))


def mute(button:Other_Button) -> None:
    """Draws the mute button
    
Parameters:
    button: full screen Button object"""

    pass 




# this is horrible but idk what else to do to combat circular import 
special_buttons = {
    'full_screen' : full_screen,
    'mute' : mute
}