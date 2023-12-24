"""
Created by Grayson Palermo 
12/23/2023
Literature Humanities 
Odessey Game 

TODO:

fix multiline_text()
combine calculate_waypoint_coords() and calculate_boat_coords() into one function   

"""

import pygame as pg
import run


def main() -> None:
    """Main function of the program"""

    pg.init()
    pg.display.set_mode(flags=pg.FULLSCREEN)
    running = True

    while running:

        scene = 9

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
Trumpet sound: https://pixabay.com/sound-effects/success-fanfare-trumpets-6185/"
Click sound: https://pixabay.com/sound-effects/hitting-wood-6791/ 

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

All pixel artwork was created by me 

"""