from enum import Enum

class Figures(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
def string_to_figure(input):
    try:
        return Figures[input.upper()]
    except KeyError:
        return None