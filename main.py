#!/usr/bin/python
# coding: utf-8

# importation du fichier gui.py, puis on cible la class Gui()
from gui import Gui
# importation du fichier game.py, puis on cible la class Game()
from game import Game


def main():
    # instance de class
    game = Game()
    gui = Gui()
    # variable pour la boucle while
    runGame = True
    # tant que runGame == True la boucle s'effectue
    while runGame:
        # dans mon fichier gui.py j'appel à l'aide de mon instance gui la méthode runGuiMenu 
        # qui s'execute en lançant le menu
        gui.runGuiMenu()
        # dans mon menu SI je choisi entrer:
        if gui.choiceGuiMenu == "enter":
            # dans mon fichier game.py j'appel à l'aide de mon instance game la méthode run
            # qui lance le jeu
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

"""
if __name__ == '__main__' est un un idiome

"""
# window rename message => mettre run en menu utiliser le camelcase pour les méthode et les class elle sont en 
# etat préjeu starsed etat win etat lose regrouper menu et message dans une seul class  GUI
# gestion des evenement gestion du draw 
# faire une analyse avant de coder => étude fonctionel => solution technique 
# impact mapping à la place d uml 
# tuto math stat moyenne ecart type variance prob et variable aléatoire mooc MàN math 
# https://www.udemy.com/course/probabilites-pour-filieres-technico-commerciales/learn/lecture/10157802?start=0#overview 

# pas de hors sujet et préparer des questions sur le projet 4 