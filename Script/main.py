"""
Created by Grayson Palermo 
10/29/2023
Literature Humanities 
Odessey Game 

TODO:

troubleshoot and play test 

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
    pg.display.set_mode(flags=pg.FULLSCREEN)


    # for testing sanity 
    #pg.mixer.music.set_volume(0)


    while running:

        scene = 10

        run.opening()
        run.tutorial()

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
Trumpet: https://pixabay.com/sound-effects/success-fanfare-trumpets-6185/"
Click: https://pixabay.com/sound-effects/hitting-wood-6791/ 

Opening Music: 
Viking Intro (Loop) by Alexander Nakarada (CreatorChords) | https://creatorchords.com
Music promoted by https://www.free-stock-music.com
Creative Commons / Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/

Gameplay Music:
War Shout (Loop Ready) by Alexander Nakarada (CreatorChords) | https://creatorchords.com
Music promoted by https://www.free-stock-music.com
Creative Commons / Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/


"""