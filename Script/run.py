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
    pg.mixer.music.load("./Assets/General/opening_music.mp3")
    pg.mixer.music.play(-1)
    
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
                pg.mixer.music.fadeout(FADE_SECS * 1000 + 500)
                draw.fade_out(clock, draw.opening_screen)
                running = False
                pg.mixer.music.load("./Assets/General/gameplay_music.mp3")
                pg.mixer.music.play(-1)
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.mixer.Sound("./Assets/General/click.mp3").play()


        
        pg.display.update()


def tutorial():
    running = True
    clock = pg.time.Clock()

    draw.fade_in(clock, draw.tutorial)
    
    while running:
    
        clock.tick(FPS)

        draw.tutorial()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                else:
                    running = False
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.mixer.Sound("./Assets/General/click.mp3").play()
        
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

    ocean_sound = pg.mixer.Sound("./Assets/General/ocean.wav")
    ocean_sound.play(-1)
    ocean_sound.set_volume(.5)


    while running:
        
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                    
            if event.type == pg.KEYDOWN:
                show_guide_text = False

        boat.move()

        draw.map_screen(boat, img, scene, waypoint_cords)

        if show_guide_text: 
            draw.map_guide_text()
        else:
            draw.crew_counter(scene)


        if boat.collide_waypoint(waypoint_cords):
            ocean_sound.fadeout(FADE_SECS * 1000 + 500)
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

    click_sound = pg.mixer.Sound("./Assets/General/click.mp3")

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
            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()

        pg.display.update()
        
    
def ending() -> None:
    """Runs the end screen"""


    screenX, screenY = pg.display.get_window_size()
    win = pg.display.get_surface()

    running = True

    img = pixel_scale(pg.image.load('./Assets/General/endscreen.png').convert_alpha(), fullscreen=True)
    pg.mixer.music.stop()

    pg.mixer.Sound("./Assets/General/victory.mp3").play()

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()

        win.blit(img, (0, 0))

        text = pg.font.Font(None, screenX//16).render('Click anywhere to play again', True, 'black')
        win.blit(text, text.get_rect(center=(screenX//2, screenY//24)))

        pg.display.update()


def play_option(button:Button):

    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pg.mixer.Sound("./Assets/General/click.mp3").play()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                else:
                    running = False

        button.play_outcome()

        pg.display.update()