#!/usr/bin/python
# coding: utf-8

# importation du fichier game.py, puis on cible la class Game 

from menu import Menu
from game import Game
from window import Window_win_lose


def main():
    game = Game()
    menu = Menu()
    window = Window_win_lose()
    menu.run()
    if menu.choice == "run the game":
        run_game = True
        while run_game:
            game.run()
            if game.result == "you won!":
                window.run("win")
                if window.choice == "exit":    
                    run_game = False 
            if game.result == "you lose!":
                window.run("lose")
                if window.choice == "exit":
                    run_game = False
            window.re_init()
            game.re_init()
   
if __name__ == "__main__":
    main()
