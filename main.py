"""
Created by Grayson Palermo 
12/7/2023
Literature Humanities 
Odessey Game 

TODO:

troubleshoot and play test 
add docstrings 
format code better

"""

import pygame as pg
import run


def main() -> None:
    """Main function of the program"""

    pg.init()

    running = True

    pg.display.set_mode(flags=pg.FULLSCREEN)
    

    while running:

        
        scene = 1

        run.opening()
        run.tutorial()

        while running:
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