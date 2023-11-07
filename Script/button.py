import pygame as pg
import draw

class Button():

    def __init__(self, label:str, pos:int, color:pg.Color) -> None:
        """Instanciates the Button class

Parameters: 
    label: label for the button, can be a kwarg for special buttons
    pos: numerical position of the button
    color: color of the button"""
        
        self.label = label
        self.pos = pos
        self.color = color
        self.win = pg.display.get_surface()


    def get_font_size(self) -> None:
        """Will eventually computer the correct font sized based on the window size"""
        return 50


    def __repr__(self) -> str:
        """Returns the specificities of the Button object"""

        return f"Rect: {self.rect}\nText: {self.label}"


    def draw(self) -> None:
        """Draws the button"""

        pg.draw.rect(self.win, self.color, self.rect)
        pg.draw.rect(self.win, pg.Color(0, 0, 0), self.rect, 2)
        self.win.blit(self.text, self.text_rect)
    

    def mouse_collides(self) -> int:
        """Checks to see if the mouse is colliding with the button 
Returns the position if it is, otherwise returns 0"""

        if self.rect.collidepoint(pg.mouse.get_pos()):
            return self.pos
        return 0



class Option_Button(Button):

    def __init__(self, label:str, pos:int, color:pg.Color) -> None:
        """Instanciates the Option_Button class

Parameters: 
    label: label for the button, can be a kwarg for special buttons
    pos: numerical position of the button
    color: color of the button"""

        self.screen_size = pg.display.get_window_size()

        super().__init__(label, pos, color)
        self.text = pg.font.Font(None, self.get_font_size()).render(self.label, True, 'black')
        self.rect = self.__get_rect()
        self.text_rect = self.text.get_rect(center=self.rect.center)


    def __get_rect(self) -> pg.Rect:
        """Calculates the rectangle for the button based off the screen size

Return: 
    pg.Rect: rectangle object for the Button"""

        sx, sy = self.screen_size
        x = sx / 6
        y = sy / 10

        rx = sx / 6
        ry = (sy / 5) + (2 * y * (self.pos - 1)) - 2

        return pg.Rect(5 * rx, ry, rx, y*2)



class Other_Button(Button):

    def __init__(self, label: str, pos: int, color: pg.Color, \
                 center: tuple, dimensions: tuple, *, action = None) -> None:
        
        """Instanciates the Special_Button class

Parameters: 
    label: label for the button, can be a kwarg for special buttons
    pos: numerical position of the button
    color: color of the button
    center: center cordinate for the button 
    dimensions: dimensions of the button
    action: optional parameter for buttons that have a special functionality"""

        super().__init__(label, pos, color)

        self.c = center
        self.text = pg.font.Font(None, self.get_font_size()).render(self.label, True, 'black')
        self.text_rect = self.text.get_rect(center=self.c)
        self.dim = dimensions
        self.rect = pg.Rect(center[0] - dimensions[0]//2, \
                            center[1] - dimensions[1]//2, \
                            dimensions[0], dimensions[1])
        if action:
            self.action = action


    def draw(self) -> None:
        """Draws the button, allowing for kwarg label to effect what is drawn"""


        if self.label not in draw.special_buttons:
            super().draw()
        else:
            draw.special_buttons[self.label](self)


    def __call__(self) -> None:
        """Calls the function of the Button (if specified)"""

        self.action()