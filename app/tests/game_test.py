import unittest

from app.game.game import Game, Result
from app.objects.move import Move
from app.objects.player import Player


class GameTest(unittest.TestCase):
    player1 = Player("p1")
    player2 = Player("p2")

    listener_result = None
    listener_winner = None

    def test_paper_beats_rock(self):
        game = Game(self.player1, self.player2)
        game.move(self.player1, Move.ROCK)
        game.move(self.player2, Move.PAPER)
        self.assertEqual(game.result, Result.WIN)
        self.assertEqual(game.winner, self.player2)

    def test_scissors_beats_paper(self):
        game = Game(self.player1, self.player2)
        game.move(self.player1, Move.PAPER)
        game.move(self.player2, Move.SCISSORS)
        self.assertEqual(game.result, Result.WIN)
        self.assertEqual(game.winner, self.player2)

    def test_rock_beats_scissors(self):
        game = Game(self.player1, self.player2)
        game.move(self.player1, Move.SCISSORS)
        game.move(self.player2, Move.ROCK)
        self.assertEqual(game.result, Result.WIN)
        self.assertEqual(game.winner, self.player2)

    def test_change_move_fails(self):
        game = Game(self.player1, self.player2)
        game.move(self.player1, move=Move.ROCK)
        self.assertRaises(Exception, game.move, self.player1, Move.SCISSORS)

    def test_draws(self):
        game = Game(self.player1, self.player2)
        game.move(self.player1, Move.ROCK)
        game.move(self.player2, Move.ROCK)
        self.assertEqual(game.result, Result.DRAW)
        self.assertEqual(game.winner, None)

        game.move(self.player1, Move.PAPER)
        game.move(self.player2, Move.PAPER)
        self.assertEqual(game.result, Result.DRAW)
        self.assertEqual(game.winner, None)

        game.move(self.player1, Move.SCISSORS)
        game.move(self.player2, Move.SCISSORS)
        self.assertEqual(game.result, Result.DRAW)
        self.assertEqual(game.winner, None)

        game.move(self.player1, Move.ROCK)
        game.move(self.player2, Move.SCISSORS)
        self.assertEqual(game.result, Result.WIN)
        self.assertEqual(game.winner, self.player1)

    def result_listener(self, result: Result, winner: Player):
        self.listener_result = result
        self.listener_winner = winner

    def test_result_listener(self):
        game = Game(self.player1, self.player2)
        game.add_result_listener(self.result_listener)
        game.move(self.player1, Move.ROCK)
        game.move(self.player2, Move.SCISSORS)
        self.assertEqual(self.listener_result, Result.WIN)
        self.assertEqual(self.listener_winner, self.player1)
