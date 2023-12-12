# MY_Chess_AI
Person VS AI chess game

Person vs. AI Chess Game
Overview
This document provides an overview of a chess game that pits a human player against an artificial intelligence (AI) opponent. The game leverages code to facilitate the interaction between the player and the AI, creating an engaging and challenging chess-playing experience.
Features
1. User Interface
The game features a user-friendly interface that allows the human player to interact with the chessboard seamlessly. The interface should display the current board position, highlight legal moves, To initiate the game, the initial step involves selecting the pawn's color and provide a clear indication of whose turn it is. The individual who opted for the white pieces is required to make the initial move, granting them the chance to launch the first attack.
2. Technologies
Position Evaluation
Position evaluation is the mechanism by which the AI assigns a numerical value to a chess position, reflecting the advantage or disadvantage of each side. Various factors contribute to the evaluation, including piece activity, pawn structure, king safety, and material balance. A well-tuned evaluation function guides the AI in making informed decisions about the desirability of a given position.
Search Tree Using Minimax
Minimax is a decision-making algorithm employed in game theory, particularly for two-player, zero-sum games like chess. The algorithm explores the game tree by considering all possible moves and their resulting positions. It alternates between maximizing and minimizing players, aiming to find the best move that maximizes the evaluating function for the current player and minimizes it for the opponent.
Alpha-Beta Pruning
Alpha-beta pruning is an optimization technique applied to the minimax algorithm to reduce the number of nodes evaluated in the search tree. By eliminating branches that are guaranteed not to influence the final decision, alpha-beta pruning significantly improves the efficiency of the search. The algorithm maintains two values, alpha and beta, representing the minimum score the maximizing player is assured of and the maximum score the minimizing player is assured of, respectively.
3. Move Validation
The code ensures that all moves made by the human player and the AI adhere to the rules of chess. This includes checking for legal moves, identifying check and checkmate situations, and handling special moves like castling and en passant.
4. Game Logic
The game logic manages the flow of the game, determining when it's the human player's turn and when the AI should make a move. It also detects the game's conclusion, whether it be a checkmate, stalemate, or a draw.
5. User Input
The program accepts human player input by dragging the mouse  on the graphical interface . The input system ensures a smooth and intuitive experience for the player.
How to Play
1.	Start the Game:
•	Run the chess program  to initialize the chessboard and set up the pieces by typing the command "python chess.py" in the terminal with being in the directory.
•	The player get to choose the colour of the coin.
2.	Make Moves:
•	On the player's turn, they can select a piece and choose a legal move.
•	The AI will then respond with its move.
3.	Game Progression:
•	The game continues with alternating moves between the player and the AI until it reaches a conclusion.
4.	End of Game:
•	The game concludes when one player is checkmated, a draw is declared, or the player chooses to resign.
5. Evaluation Metrics

* The main aim of the project is AI agent should generate optimal moves within less times. This has been shown during the code execution.
  After every turn of AI a time has been displayed in seconds which indicates how much time AI has taken to make its moves.

  It's mostly less than 1sec.

6. Validating Moves

    Another most important aspect of chess is each piece has it's own rule for moving along the board.
    These rules are described in project presentation and evaluation can be made by manually trying to move each piece in the board

* Default depth is set to 3, project can be evaluated by changing the deptth to different values and measure its performance.
  Depth can be changed in board.py --> init constructor --> self.MAXDEPTH
Implementation & software libraries
The implementation of the person vs. AI chess game can be achieved using a programming language such as Python with a  library, like PyGame. The AI component can be developed using algorithms like minimax with alpha-beta pruning.
Libraries that needs to be installed
-Python 3.10 version
-PIP
-PyGame
Conclusion
This person vs. AI chess game provides an enjoyable and challenging experience for chess enthusiasts of all skill levels. Whether you're a casual player looking for a friendly match or a seasoned player seeking a tough opponent, this game offers a flexible and engaging platform for honing your chess skills.
