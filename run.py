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
    pg.mixer.music.set_volume(MUSIC_VOLUME)

    click_sound = pg.mixer.Sound("./Assets/General/click.mp3")
    click_sound.set_volume(CLICK_VOLUME)
    
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
                
                pg.mixer.music.load("./Assets/General/gameplay_music.mp3")
                pg.mixer.music.play(-1)
                pg.mixer.music.set_volume(MUSIC_VOLUME)
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()

        pg.display.update()



def tutorial() -> None:
    """Runs the tutorial scene"""
    
    running = True
    clock = pg.time.Clock()
    draw.fade_in(clock, draw.tutorial)

    click_sound = pg.mixer.Sound("./Assets/General/click.mp3")
    click_sound.set_volume(CLICK_VOLUME)

    first_load = True
    
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
                if not first_load:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if not first_load:
                    click_sound.play()
        
        first_load = False
        pg.display.update()



def display_map(scene:int) -> None:
    """Runs the map of Achilleus
    
Parameters: 
    scene: scene number, indicated by an integer"""

    clock = pg.time.Clock()
    running = True
    show_guide_text = True

    ocean_sound = pg.mixer.Sound("./Assets/General/ocean.wav")
    ocean_sound.play(-1)
    ocean_sound.set_volume(OCEAN_VOLUME)

    img = pixel_scale(pg.image.load('./Assets/MapScene/map.png').convert_alpha(), fullscreen=True)
    boat = Boat(scene, img)
    waypoint_cords = calculate_waypoint_coords(scene)

    while running:
        
        clock.tick(FPS)
        draw.map_screen(boat, img, scene, waypoint_cords)

        if show_guide_text: 
            draw.map_guide_text()
        else:
            draw.crew_counter(scene)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                    
            if event.type == pg.KEYDOWN:
                show_guide_text = False

        boat.move()

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
    click_sound = pg.mixer.Sound("./Assets/General/click.mp3")
    click_sound.set_volume(CLICK_VOLUME)

    with open("Assets/General/buttons.csv") as file:
        button_values = tuple(csv.reader(file))[scene-1]
    with open("Assets/General/descriptions.txt") as file:
        description = str(file.readlines()[scene-1])

    buttons = [Button(button_values[n-1], n, scene) for n in range(1, 5)]

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

    running = True
    screenX, screenY = pg.display.get_window_size()
    win = pg.display.get_surface()

    img = pixel_scale(pg.image.load('./Assets/General/endscreen.png').convert_alpha(), fullscreen=True)
    pg.mixer.music.stop()

    victory_sound = pg.mixer.Sound("./Assets/General/victory.wav")
    victory_sound.set_volume(VICTORY_VOLUME)
    victory_sound.play()

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
    click_sound = pg.mixer.Sound("./Assets/General/click.mp3")
    click_sound.set_volume(CLICK_VOLUME)
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end()
            if event.type == pg.MOUSEBUTTONUP:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()
            if event.type == pg.KEYUP:
                if event.key in (pg.K_ESCAPE, pg.K_q):
                    end()
                else:
                    running = False

        button.play_outcome()

        pg.display.update()