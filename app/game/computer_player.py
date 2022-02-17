import math
from random import Random
from app.objects.player import Player
from app.objects.move import Move


class ComputerPlayer(Player):

    def __init__(self) -> None:
        super().__init__("Computer")

    def make_move(self) -> Move:
        return Random.choice(list(Move))
