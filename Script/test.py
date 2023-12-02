import pygame as pg


def multiline_text(text:str, size:int, width, /, color='black', split_char = "\n", **kwargs) -> None:
    """Renders and displays multiple lines of text for PyGame

Parameters:
    text: the text to be displayed
    size: the size of the text
    kwargs: must specify a center point with a coordinate, as you would with pg.Surface.get_rect()"""
   
    font = pg.font.Font(None, size)

    
    max_characters = width // (size / 2.9)

    if len(text) > max_characters:

        new_text = ""
        line = ""
        words = text.split(" ")

        while len(words) > 0:
            n = 0

            while n < len(words) and len(line + (word := f" {words[n]}")) < max_characters:
                line += word
                n += 1
            
            new_text += line + "\n"
            line = ""
            words = words[n:]
        
        text = new_text[:-1]
    

    if 'topleft' in kwargs:
        for n, line in enumerate(text.split(split_char)):
            line_text = font.render(line, True, color)
            pg.display.get_surface().blit(line_text, line_text.get_rect(topleft=(kwargs['topleft'][0], kwargs['topleft'][1] + size * n)))
   
    elif 'center' in kwargs:
        num_split = text.count("\n")
        for n, line in enumerate(text.split(split_char)):
            line_text = font.render(line, True, color)
            pg.display.get_surface().blit(line_text, line_text.get_rect(center=(kwargs['center'][0], kwargs['center'][1] + size * n - (num_split / 2) * size)))
   
    else:
        raise ValueError("No starting point for text specified")




def split_text(text:str, width, size):

    text_to_return = ""
    line = ""

    max_characters = width // (size / 2.9)

    words = text.split(" ")

    while len(words) > 0:

        n = 0
        
        while n < len(words) and len(line + (word := f" {words[n]}")) < max_characters:
            line += word
            n += 1
        
        
        text_to_return += line + "\n"
        line = ""
        words = words[n:]
    
    return text_to_return
