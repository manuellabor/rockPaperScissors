17:00
Starting the task

# General Plan
* functionality first
    * create a MVP first that creates a playable version of the game
    * iterate on the solution to make it work better and make it look nicer 
* first steps
    * implement basic gameplay, event based
        * need a game controller that
            * lets 2 people register
            * allows each player to make their move, once both players are connected
                * I am assuming that players are connecting from different devices, so as long as the server keeps the other players move secret the players do not need to make their move "simultaneous"
            * once both players made their move, decide which player won
            * notify players who won
    * test basic gameplay
        * register 2 players, make moves check if rules apply correctly -> success
            * test all combinations and draws
        * register 1 player, try to make move -> illegal
        * register 2 players, one player makes 2 moves -> illegal
        * try to register more than, two players -> illegal
    * make game (result?) savable to database
* next steps
    * implement computer player
        * computer player registers, waits for other player to register, makes move, wait for result
    * implement server functionality
        * websocket based communication during gameplay, so sending updates to players is easy
        * implement player class
            * name
            * games
        * implement registration, rest based
            * create new player
            * login as player
    * implement web-client
        * let player register
        * select opponent
            * other player
            * computer
        * start game
        * make move
        * display result

# Implementation
* since starting a game only makes sense with 2 players present, registration at the game controller is unneccesary
    * instead make game object with 2 dedicated fields for each player that is initialized when the game is started
            