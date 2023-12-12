


import pygame
from board import ChessBoard
from userInterface import UserInterface

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode([800, 800], 0, 0)


    pygame.display.set_caption('Chess')

    Board = ChessBoard()

    UI = UserInterface(surface, Board)

    UI.playGame()

    pygame.quit()
