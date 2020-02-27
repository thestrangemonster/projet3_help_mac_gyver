#!/usr/bin/python
# coding: utf-8

# importation du fichier game.py, puis on cible la class Game 

from gui import Gui
from game import Game

def main():
    game = Game()
    gui = Gui()
    runGame = True
    while runGame:
        gui.runGuiMenu()
        if gui.choiceGuiMenu == "run the game":
            game.run()
            if game.result == "you won!":
                gui.runGuiMessage("win")
                if gui.choiceGuiMessage == "exit" or gui.exit == False:  
                    return
            if game.result == "you lose!":
                gui.runGuiMessage("lose")
                if gui.choiceGuiMessage == "exit" or gui.exit == False:  
                    return
            gui.reInit()
            game.reInit()
            if game.exit == False:
                runGame = False
        else:
            runGame = False

if __name__ == "__main__":
    main()
# window rename message => mettre run en menu utiliser le camelcase pour les méthode et les class elle sont en 
# etat préjeu starsed etat win etat lose regrouper menu et message dans une seul class  GUI
# gestion des evenement gestion du draw 
# faire une analyse avant de coder => étude fonctionel => solution technique 
# impact mapping à la place d uml 
# tuto math stat moyenne ecart type variance prob et variable aléatoire mooc MàN math 
# https://www.udemy.com/course/probabilites-pour-filieres-technico-commerciales/learn/lecture/10157802?start=0#overview 

# pas de hors sujet et préparer des questions sur le projet 4 