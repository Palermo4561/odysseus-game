"""
Created by Grayson Palermo 
10/29/2023
Literature Humanities 
Odessey Game 

TODO:
intro scene 
make the crew counter accurate 
end scene 
create art for each button variation

"""

import pygame as pg
import run
from globals import *


def main() -> None:
    """Main function of the program"""

    pg.init()

    running = True

    pg.display.set_mode((1280,720))

    # for testing 
    #pg.display.set_mode(flags=pg.FULLSCREEN)

    while running:

        scene = 1

        run.opening()

        while True:
            run.display_map(scene)
            run.main_game(scene)
            
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