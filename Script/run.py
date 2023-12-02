import pygame as pg
import draw 
from globals import *
from button import Button
from functions import *
from dictionaries import *
from boat import Boat
import csv


def opening() -> None:
    """Runs the opening scene of the same"""

    running = True
    clock = pg.time.Clock()
    
    while running:
    
        clock.tick(FPS)

        draw.opening_screen()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
        
        pg.display.update()


def display_map(scene:int) -> None:
    """Runs the map of Achilleus
    
Parameters: 
    scene: scene number, indicated by an integer"""

    running = True
    clock = pg.time.Clock()
    
    img = pixel_scale(pg.image.load('./Assets/MapScene/map.png').convert_alpha(), fullscreen=True)

    boat = Boat(scene, img)

    waypoint_cords = calculate_waypoint_coords(scene)

    show_guide_text = True


    while running:
        
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                if event.key == pg.K_n:
                    running = False
            if event.type == pg.KEYDOWN:
                show_guide_text = False

        boat.move()

        draw.map_screen(boat, img, scene, waypoint_cords)

        if show_guide_text: 
            draw.map_guide_text()
        else:
            draw.crew_counter(scene)


        if boat.collide_waypoint(waypoint_cords):
            draw.fade_out(clock, draw.map_screen, boat, img, scene, waypoint_cords)
            running = False

        pg.display.update()


def main_game(scene:int) -> None:
    """Runs the main game
    
Parameters: 
    scene: scene number, indicated by an integer"""

    running = True
    clock = pg.time.Clock()


    with open("Assets/General/buttons.csv") as file:
        button_values = tuple(csv.reader(file))[scene-1]
    with open("Assets/General/descriptions.txt") as file:
        description = str(file.readlines()[scene-1])

    buttons = []
    for n in range(1, 5):
        buttons.append(Button(button_values[n-1], n, scene))

    
    draw.fade_in(clock, draw.game_screen, buttons, scene, description)

    while running:

        clock.tick(FPS)

        draw.game_screen(buttons, scene, description)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                if (b := check_button_collisions(buttons)):
                    play_option(buttons[b-1])
                    if b == int(button_values[4]):
                        running = False
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()

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
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()

        pg.display.get_surface().fill((44, 88, 120))

        end_text = """The end
        click anywhere to play again
        press q or esc to quit"""

        multiline_text(end_text, 100, center=tuple(map(lambda z : z //2, pg.display.get_window_size())))

        pg.display.update()


def play_option(button:Button):

    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()

        button.play_outcome()

        pg.display.update()