import asyncio
import json

import websockets
from app.objects.client_player import ClientPlayer
from app.objects.player import Player
from app.game.game import Game

players = []


def start_game(player1: Player, other_player: str):
    # TODO check if other player exists, add game to the players
    player2 = players[other_player]
    game = Game(player1, player2)


async def handler(websocket):
    print("websocket opened")
    player: ClientPlayer = None
    while player is None:
        message = await websocket.recv()
        msgObject = json.loads(message)
        if "name" in msgObject:
            player = ClientPlayer(msgObject["name"], websocket, start_game)
    players.append(player)
    await player.start_listening()


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
