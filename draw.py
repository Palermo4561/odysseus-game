import pygame as pg
from button import *
import dictionaries
from functions import *
from boat import Boat
from globals import *
from button import Button


def opening_screen() -> None:
    """Draws the opening screen of the game"""

    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    
    bg = pixel_scale(pg.image.load('./Assets/General/openingscreen.png').convert_alpha(), fullscreen=True)
    text_background = pg.Rect(21 * screenX // 32, screenY // 30, 5 * screenX // 16, 17 * screenY // 48)
    sub_text = pg.font.Font(None, screenX//30).render("Click anywhere to begin", True, 'black')
    
    win.blit(bg, (0, 0))
    pg.draw.rect(win, '#62401D', text_background)
    pg.draw.rect(win, '#281706', text_background, 6)

    multiline_text("Odysseus's\nJourney", screenX//15, color='black', center=(39 * screenX//48, screenY//6))
    win.blit(sub_text, sub_text.get_rect(center=(39 * screenX//48, screenY//3)))



def tutorial() -> None:
    """Draws the tutorial screen"""
    
    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    img = pixel_scale(pg.image.load('./Assets/General/tutorialscreen.png').convert_alpha(), fullscreen=True)
    title_text = pg.font.Font(None, screenX // 15).render('Basic Tutorial', True, 'black')
    
    with open('./Assets/General/tutorial.txt', 'r') as file:
        tutorial_text = ''.join(file.readlines())

    win.blit(img, (0,0))
    win.blit(title_text, title_text.get_rect(center=(screenX//2, screenY/12)))
    multiline_text(tutorial_text, screenX // 30, center=(screenX//2, screenY//1.7))



def map_screen(boat:Boat, img:pg.Surface, scene:int, waypoint_cords) -> None:
    """Draws the map screen of Achilelus's journey

Parameters: 
    boat: player character Boat object
    img: map image to draw
    scene: scene number, indicated by an integer"""

    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    
    win.fill(pg.Color(0, 0, 0))
    win.blit(img, (0, 0))

    thick_aa_circle(waypoint_cords, int(WAYPOINT_RADIUS * screenX / 1280), "#0C6C19", 2)
    draw_circle_alpha(pg.Color(0, 164, 69, 50), waypoint_cords, int(WAYPOINT_RADIUS * screenX / 1280))
    pg.draw.rect(win, 'red', pg.Rect(waypoint_cords[0] - screenX / 320, waypoint_cords[1] - screenY / 180, screenX / 160, screenY / 90))
    
    win.blit(boat.image, boat.rect)



def map_guide_text() -> None:
    """Displays the tutorial text for the map"""

    screenX, screenY = pg.display.get_window_size()

    text = pg.font.Font(None, 50).render("Use arrow keys or WASD to move to the next waypoint", True, 'black')

    rect = pg.Rect(screenX//8, screenY//48, 3*screenX//4, 5*screenY//72)
    pg.draw.rect(pg.display.get_surface(), '#6D715A', rect, border_radius=3)
    pg.draw.rect(pg.display.get_surface(), '#000000', rect, 2, 3)

    pg.display.get_surface().blit(text, text.get_rect(center=(screenX//2, screenY//18)))



def crew_counter(scene) -> None:
    """Displays the crew count of the current scene 

Parameters: 
    scene: scene number, indicated by an integer"""

    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    crew_number = str(dictionaries.crew_count[scene-1])
    text = pg.font.Font(None, screenX//30).render(f"Crew Count: {crew_number}", True, 'black')


    text_rect = text.get_rect(center=((7*screenX)//8, screenY // 18))
    border_padding = (screenX//120, screenY//100)
    border_rect = pg.Rect(text_rect.left-border_padding[0], text_rect.top-border_padding[1],\
                          text_rect.width+2*border_padding[0], text_rect.height+2*border_padding[1])

    pg.draw.rect(win, '#6D715A', border_rect, border_radius=3)
    pg.draw.rect(win, '#000000', border_rect, 2, 3)

    win.blit(text, text_rect)



def game_screen(buttons:list[Button], scene:int, description) -> None:
    """Draws the main game screen

Parameters:
    buttons: list of the buttons to be rendered to the screen
    scene: scene number, indicated by an integer
    description: the description to be displayed on the side screen"""

    pg.display.get_surface().fill((0, 0, 0))

    title_bar(scene)
    side_screen(description)
    main_screen(scene)
    
    for button in buttons:
        button.draw()



def title_bar(scene:int) -> None:
    """Draws the title bar for the game screen
    
Parameters: 
    scene: scene number, indicated by an integer"""

    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    title = dictionaries.scenes[scene]
    text = pg.font.Font('./Assets/General/Greek-Freak.ttf', screenX//14).render(title, True, 'black')

    img = pixel_scale(pg.image.load('./Assets/General/text_background.png').convert_alpha())

    win.blit(img, (0, 0))
    win.blit(text, text.get_rect(center=(screenX//2, screenY//10)))



def side_screen(description:str) -> None:
    """Draws the side screen with the description
    
Parameters:
    description: words to overlap the side rectangle"""

    win = pg.display.get_surface()
    screenX, screenY = pg.display.get_window_size()
    rect = pg.Rect(0, screenY//5 - 2, screenX // 6, 4 * screenY // 5)

    win.blit(pixel_scale(pg.image.load(f"Assets/General/Side.png")), (0, screenY//5))
    multiline_text(str(description), screenX // 42, screenX // 6 - 30, \
                   topleft=tuple(map(lambda z : z + screenX//100, rect.topleft)))



def main_screen(scene) -> None:
    """Draws the central screen of the scene

Parameters: 
    scene: scene number, indicated by an integer"""

    screenX, screenY = pg.display.get_window_size()
    bg = pg.transform.scale(pg.image.load(f"./Assets/Scene{scene}/background.png").convert_alpha(), (2*screenX/3, 4*screenY/5))

    pg.display.get_surface().blit(bg, (screenX / 6, screenY / 5))



def fade_out(clock:pg.time.Clock, next_screen_draw, *args) -> None:
    """Fades out of a screen being drawn

Parameters:
    clock: PyGame Clock object for regulating time 
    next_screen_draw: function for drawing the next screen 
    *args: arguments neccessary for drawing the next screen"""

    alpha = 0

    while True:

        clock.tick(FPS)

        next_screen_draw(*args)
        
        s = pg.Surface(pg.display.get_window_size())
        s.set_alpha(int(255 * alpha / (FADE_SECS * FPS)))
        s.fill((0, 0, 0))
        pg.display.get_surface().blit(s, (0, 0))

        alpha += 1

        pg.display.update()

        if alpha > FADE_SECS * FPS:
            pg.display.get_surface().fill((0, 0, 0))
            break



def fade_in(clock:pg.time.Clock, next_screen_draw, *args) -> None:
    """Fades into the next screen being drawn

Parameters:
    clock: PyGame Clock object for regulating time 
    next_screen_draw: function for drawing the next screen 
    *args: arguments neccessary for drawing the next screen"""

    alpha = FADE_SECS * FPS / 4

    while True:

        clock.tick(FPS)

        next_screen_draw(*args)
        
        s = pg.Surface(pg.display.get_window_size())
        s.set_alpha(int(255 * alpha / (FADE_SECS * FPS / 4)))
        s.fill((0, 0, 0))
        pg.display.get_surface().blit(s, (0, 0))
                
        alpha -= 1

        pg.display.update()

        if alpha <= 0:
            break