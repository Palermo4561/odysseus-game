"""
Created by Grayson Palermo 
10/29/2023
Literature Humanities 
Odessey Game 

TODO:
dynamically calculate the font size
add location bubbles 
make the game lol

"""

import pygame as pg
import run
from globals import *


def main() -> None:
    """Main function of the program"""

    pg.init()

    clock = pg.time.Clock()

    running = True

    pg.display.set_mode((1280,720))

    # for testing 
    #pg.display.set_mode(flags=pg.FULLSCREEN)

    while running:

        scene = 1

        run.opening(clock)

        while True:
            run.display_map(scene, clock)
            run.main_game(scene, clock)
            
            scene += 1

            if scene > 13:
                break

        run.ending()

if __name__ == "__main__":
    main()


"""
Credits: 


Font: https://www.1001freefonts.com/greek-freak.font

"""