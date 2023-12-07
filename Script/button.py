import pygame as pg
from functions import *
import csv
from dictionaries import outcome_text_colors

class Button():

    def __init__(self, label:str, pos:int, scene:int) -> None:
        """Instanciates the Button class

Parameters: 
    label: label for the button, can be a kwarg for special buttons
    pos: numerical position of the button
    color: color of the button
    scene: scene number, indicated by an integer"""
        
        self.label = label
        self.pos = pos
        self.scene = scene
        self.win = pg.display.get_surface()
        self.screenX, self.screenY = pg.display.get_window_size()

        self.image = self.__get_image()
        self.topleft = self.__get_topleft()
        self.collision_rect = self.__get_rect()
        
        self.outcome_image = self.__get_outcome_image()
        self.outcome_text = self.__get_outcome_text()
        #self.outcome_text_color = outcome_text_colors[scene][pos-1]
        self.outcome_text_color = 'black'


    def __get_image(self) -> pg.Surface:
        """Renders the button's image
        
Return: 
    pg.Surface: the surface rendered for the button's main image"""
        
        return pixel_scale(pg.image.load(f"Assets/General/Button{self.pos}.png"))


    def __get_rect(self) -> pg.Rect:
        """Calculates the rectangle for the button based off the screen size

Return: 
    pg.Rect: rectangle object for the Button"""

        return pg.Rect(5 * self.screenX / 6, self.topleft[1], self.screenX / 6, self.screenY / 5)


    def __get_topleft(self) -> tuple:
        """Calculates the topleft value of the button
        
Return: 
    tuple: cordinate of the topleft of the button"""

        return (5 * self.screenX / 6, self.pos * self.screenY / 5)


    def __get_outcome_image(self) -> pg.Surface:
        """Renders the button's outcome image
        
Return: 
    pg.Surface: the surface rendered for the button's outcome image"""
        
        return pixel_scale(pg.image.load(f"Assets/Scene{self.scene}/Choice{self.pos}.png"), fullscreen=True)


    def __get_outcome_text(self) -> str:
        """Loads the text associated with the button's outcome
        
Return: 
    str: the text associated with the button's outcome"""
        
        with open("Assets/General/outcomes.csv") as file:
            return tuple(csv.reader(file))[self.scene-1][self.pos-1]
        
    
    def __get_outcome_text_color(self) -> str:
        """Determines if the text color should be black or white based on the image
        
Return: 
    str: the string for the pygame color of the text"""
        
        if all(self.outcome_image.get_at((0, 0))) <= 50:
            return 'white'
        return 'black'


    def __repr__(self) -> str:
        """Returns the specificities of the Button object
        
Return: 
    str: string of the rect cords and the label"""

        return f"Rect: {self.collision_rect}\nText: {self.label}"
    

    def mouse_collides(self) -> int:
        """Checks to see if the mouse is colliding with the button 
        
Returns the position if it is, otherwise returns 0"""

        if self.collision_rect.collidepoint(pg.mouse.get_pos()):
            return self.pos
        return 0


    def draw(self) -> None:
        """Draws the button"""

        self.win.blit(self.image, self.topleft)
        multiline_text(self.label, self.win.get_size()[0]//30, self.win.get_size()[0]//6, center=self.collision_rect.center)


    def play_outcome(self) -> None:
        """Blits the outcome image and text of the button"""
        
        self.win.blit(self.outcome_image, (0, 0))
        multiline_text(self.outcome_text, self.screenX//16, color=self.outcome_text_color, center=(self.screenX//2, self.screenY//8))
        #multiline_text(self.outcome_text, self.screenX//16)
