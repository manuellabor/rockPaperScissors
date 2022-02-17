import enum

from enum import Enum


class Move(Enum):
    """ The type of move a player can make.
    The value determines which move wins in cirular pattern:
    Rock < Paper < Scissors < Rock..

    Args:
        Enum (_type_): _description_
    """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
