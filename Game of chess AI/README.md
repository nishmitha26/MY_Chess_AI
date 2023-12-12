

## References:
* Program Uses pygame: http://www.pygame.org/

  * Chess tile graphics were used from Wikimedia Commons: http://commons.wikimedia.org/wiki/File:Chess_tile_pd.png

  * alphaBeta Function was created based on the pseudocode Provided by wikipedia: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning


  * Used 'Fruit' values for rating material and similar values for other ratings from chessprogramming wikispace : https://chessprogramming.wikispaces.com/Point%20Value

  * Generating Move lists for each piece class was inspired by chessprogramming wikispace on move lists: https://chessprogramming.wikispaces.com/Move%20List

  * Board representation 'boardArray' is based off the 8x8 board array method: https://chessprogramming.wikispaces.com/8x8%20Board

  * Chess.com for descriptions of basic and special moves pieces can make:
  https://www.chess.com/learn-how-to-play-chess

#### The contents in the file include:
* assets folder: Contains all the chess piece sprites used for game’s graphics.
* chess.py : Main program used to run interface and game. Run this program when starting the game
* board.py: Contains board class and it’s methods. Also contains the alphabeta method that the computer uses to make moves
* pieces.py: Contains the master class ‘Peices’ as well as all individual piece classes that inheret the main class.
* ratings.py : Contains the ratings class with methods that evaluate the rating of a move.
* userInterface.py: Contains the userInterface class that is used to play the game and display the game using pygame.






 
 
