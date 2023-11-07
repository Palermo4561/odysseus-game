import pygame as pg
import random
import draw 
from globals import *
from button import *
from functions import *
from dictionaries import *
import button_details as bd
import functions
from boat import Boat


def opening(clock:pg.time.Clock) -> None:
    """Runs the opening scene of the same

Parameters:
    clock: clock object for keeping consistent time"""

    running = True
    
    x, y = pg.display.get_window_size()

    start_button = Other_Button('Start', 1, 'red', (x//2, 3*y//4), (150, 100))
    fs_button = Other_Button('full_screen', 1, 'red', (300, 300), (100, 100))

    while running:
    
        clock.tick(FPS)

        draw.opening_screen(start_button)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    end()
            if event.type == pg.MOUSEBUTTONUP:
                if start_button.mouse_collides():
                    running = False
        
        pg.display.update()


def display_map(scene:int, clock:pg.time.Clock) -> None:
    """Runs the map of Achilleus
    
Parameters: 
    scene: scene number, indicated by an integer
    clock: clock object for keeping consistent time"""

    running = True

    screenX, screenY = pg.display.get_window_size()
    
    img = pixel_scale(pg.image.load('./Assets/MapScene/map.png').convert_alpha(), fullscreen=True)
    img = pg.transform.scale(img, (screenX, screenY))

    boat = Boat(scene, img)


    while running:
        
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    end()

        boat.move()

        draw.map_screen(boat, img)
        pg.display.update()


def main_game(scene:int, clock:pg.time.Clock) -> None:
    """Runs the main game
    
Parameters: 
    scene: scene number, indicated by an integer
    clock: clock object for keeping consistent time"""

    running = True


    buttons = []
    for n in range(1, 5):
        buttons.append(Option_Button(bd.names[scene][n-1], n, pg.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    while running:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                if check_button_collisions(buttons) == 2:
                    running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    end()

        draw.game_screen(buttons, scene)

        pg.display.update()
        
    
def ending() -> None:
    """Runs the end screen"""
   
    running = True

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    end()

        pg.display.get_surface().fill((44, 88, 120))

        end_text = """The end
        click anywhere to play again
        press q or esc to quit"""

        functions.multiline_text(end_text, 100, center=tuple(map(lambda z : z //2, pg.display.get_window_size())))

        pg.display.update()