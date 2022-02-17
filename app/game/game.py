from enum import Enum
from typing import Callable, List
from app.objects.move import Move
from app.objects.player import Player


class Result(Enum):
    DRAW = 0
    WIN = 1


class Game(object):

    player1Move = None
    player2Move = None
    result_listeners: List[Callable[[Result, Player], None]] = []
    winner = None

    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        pass

    def add_result_listener(self, result_listener: Callable[[Result, Player], None]):
        self.result_listeners.append(result_listener)

    def move(self, player: Player, move: Move):
        if player == self.player1:
            if self.player1Move != None:
                raise Exception("Player 1 already made their move")
            self.player1Move = move
        elif player == self.player2:
            if self.player2Move != None:
                raise Exception("Player 2 already made their move")
            self.player2Move = move
        else:
            raise Exception(f'Unknown player: {player.name}')

        if self.player1Move != None and self.player2Move != None:
            self.determine_result()

    def determine_result(self):
        if self.player1Move == None or self.player2Move == None:
            raise Exception("Not all players have made their move!")

        result = self.player1Move.value - self.player2Move.value
        sign = result > 0

        if result == 0:
            self.result = Result.DRAW
            self.winner = None
            self.reset()
        else:
            self.result = Result.WIN
            if result % 2 == 0:
                if result < 0:
                    self.winner = self.player1
                else:
                    self.winner = self.player2
            else:
                if result > 0:
                    self.winner = self.player1
                else:
                    self.winner = self.player2

        for listener in self.result_listeners:
            listener(self.result, self.winner)

    def reset(self):
        self.player1Move = None
        self.player2Move = None
