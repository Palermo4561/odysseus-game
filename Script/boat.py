import pygame as pg
from dictionaries import boat_positions
from globals import *
from functions import *

class Boat():
    def __init__(self, scene, map_surf) -> None:

        self.screenX, self.screenY = pg.display.get_window_size()
        
        self.map_surf = map_surf

        self.image = pixel_scale(pg.image.load('./Assets/MapScene/boat.png').convert_alpha(), scale=0.5)
        self.rect = self.image.get_rect(center=boat_positions[scene])

    def move(self) -> None:
        """Moves the Boat object from pressed keys 

Parameters: None"""

        keys = pg.key.get_pressed()

        movementX = (int(keys[pg.K_d]) or int(keys[pg.K_RIGHT])) - (int(keys[pg.K_a]) or int(keys[pg.K_LEFT]))
        movementY = (int(keys[pg.K_s]) or int(keys[pg.K_DOWN])) - (int(keys[pg.K_w]) or int(keys[pg.K_UP]))

        if movementX or movementY:
            
            self.rect.center += pg.Vector2(self.__no_collide(movementX, movementY))


    def __land_collide(self, movementX:int, movementY:int) -> bool:
        """Checks to see if the bottom of the boat will collide with the land from the movement
        
Parameters:
    movementX: integer indicating movement in the x direction
    movementY: integer indicating movement in the y direction

Return:
    bool: boolean indicating if the next cordinate if land"""
        
        rect = self.rect
        y_cord = self.rect.bottom + movementY

        x_cords = (rect.left + rect.width // 3 + movementX,
                   rect.left + rect.width // 2 + movementX,
                   rect.left + 2 * rect.width // 3 + movementX)

        for x_cord in x_cords:
            if self.map_surf.get_at((x_cord, y_cord - 1)) != (132, 172, 212, 255):
                return True
        
        return False 



    def __no_collide(self, movementX, movementY) -> tuple:
        """Checks to see if the bottom of the boat collides with the land
        
Parameters:
    movementX: integer indicating movement in the x direction
    movementY: integer indicating movement in the y direction

Return: 
    tuple: adjusted movement to prohibit collisions"""

        newX, newY = movementX, movementY

        if movementX > 0 and self.rect.right >= self.screenX:
            newX = 0
        elif movementX < 0 and self.rect.left <= 0:
            newX = 0

        if movementY > 0 and self.rect.bottom >= self.screenY:
            newY = 0
        elif movementY < 0 and self.rect.top <= 0:
            newY = 0


        if self.__land_collide(newX, newY):
            return 0, 0
        
        return newX, newY