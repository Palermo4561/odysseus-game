import pygame as pg
from globals import *
from functions import *
from math import dist


class Boat():

    def __init__(self, scene:int, map_surf:pg.Surface) -> None:
        """Instantiates an object of the Boat class
Parameters: 
    scene: scene number, indicated by an integer
    map_surf: surface (image) of the map to check collisions with the boat movement 
    """

        self.screenX, self.screenY = pg.display.get_window_size()
        self.map_surf = map_surf
        self.horizontal_direct = 1
        
        self.image = pixel_scale(pg.image.load('./Assets/MapScene/boat.png').convert_alpha(), scale=0.5)
        self.rect = self.image.get_rect(midbottom=calculate_boat_coords(scene))



    def move(self) -> None:
        """Moves the Boat object from pressed keys"""

        keys = pg.key.get_pressed()

        movementX = (int(keys[pg.K_d]) or int(keys[pg.K_RIGHT])) - (int(keys[pg.K_a]) or int(keys[pg.K_LEFT]))
        movementY = (int(keys[pg.K_s]) or int(keys[pg.K_DOWN])) - (int(keys[pg.K_w]) or int(keys[pg.K_UP]))

        if movementX or movementY:
            self.rect.center += pg.Vector2(self.__no_collide(movementX, movementY))
        
        if movementX and movementX != self.horizontal_direct:
            self.horizontal_direct = movementX
            self.image = pg.transform.flip(self.image, True, False)



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



    def __no_collide(self, movementX:int, movementY:int) -> tuple:
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
    

    def collide_waypoint(self, waypoint_cords:tuple) -> bool:
        """Checks if the boat is close enough with the waypoint to interact

Parameters: 
    waypoint_cords: a tuple with the adjusted cords of the location of the waypoint
    
Returns:
    bool: returns whether or not the boat is within the radius of the waypoint"""
        
        return dist(waypoint_cords, self.rect.center) <= int(WAYPOINT_RADIUS * self.screenX / 1280)