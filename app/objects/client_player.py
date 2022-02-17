import json
from app.objects.player import Player


class ClientPlayer(Player):

    def __init__(self, name, websocket, start_game) -> None:
        super().__init__(name)
        self.websocket = websocket
        self.start_game_callback = start_game

    async def start_listening(self):
        message_handlers = {
            "start_game": self.start_game
        }

        async for message in self.websocket:
            messageObject = json.loads(message)
            if "type" in messageObject:
                type = messageObject["type"]
                message_handlers[type](messageObject)

            print(message)

    def start_game(self, messageObject):
        other_player = messageObject["with"]
        self.start_game_callback(self, other_player)
