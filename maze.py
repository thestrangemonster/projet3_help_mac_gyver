#!/usr/bin/python
# coding: utf-8
"""
Jeu => aider mac giver à s'échapper
Jeu dans lequel on doit déplacer mac giver jusqu'aux items puis au gaurdian à travers un labyrinthe.

Script Python
Fichiers : macgivermain.py, classes.py, constants.py, maze.txt, dossier pictures
"""
#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from random import randint
from constants import *


class Maze:  # class labyrinthe

    def __init__(self, files):  # initialiser
        pygame.init()
        self.data = 0
        self.files = files
        self.images = {}
        self.images["W"] = pygame.image.load(picture_wall).convert()
        self.images["M"] = pygame.image.load(picture_empty).convert()
        self.images["G"] = pygame.image.load(
            picture_guardian).convert_alpha()
        self.images["S"] = pygame.image.load(picture_syringe).convert_alpha()
        self.images["N"] = pygame.image.load(picture_needle).convert_alpha()
        self.images["T"] = pygame.image.load(picture_tube).convert_alpha()
        self.images["E"] = pygame.image.load(picture_empty).convert_alpha()
        self.images["I"] = pygame.image.load(picture_empty).convert_alpha()
        self.images["O"] = pygame.image.load(picture_empty).convert_alpha()
        self.images["B"] = pygame.image.load(picture_bag).convert_alpha()
        self.images["A"] = pygame.image.load(picture_bag2).convert_alpha()

    def generate(self):  # générer
        with open(self.files) as f:
            self.data = f.read()
            self.data = self.data.replace(" ", "").replace("\n", "")
            self.data = list(self.data)

    def draw(self, window):  # afficher
        # charger puis convertir les images
        
        x = 0  # ligne des abscisses
        y = 0  # ligne des ordonnées
        for k, tile in enumerate(self.data):
            window.blit(self.images[tile], (x, y))
            # lorsque je passe un sprite j'ajoute la longueur d'un sprite pour passer au suivant
            x += height_of_sprite
            if (k+1) % 15 == 0:
                # lorsque j'arrive à la fin d'une longueur total de sprite sur une ligne je remet
                # les compteur de l'abscisse à 0 et j'ajoute la longueur d'un sprite à l'ordonnée
                # afin de passer à la ligne suivante dans la modélisation graphique du labyrinthe 
                y += height_of_sprite
                x = 0

    def get_mc_pos(self):
        return self.data.index("M")
    
    def random_items(self):
        for item in ("S", "N", "T"):
            while True:
                pos = randint(0, 224)
                if self.data[pos] == "E":
                    self.data[pos] = item
                    break

    def get_item_pos(self):
        return self.data.index("O")
    
    
        
#algorithme de collision 
#algoritme aléatoire
#code avec la logique sans pygame pour s'affranchir de la gestion des graphismes
# petit pitch
# zen python
