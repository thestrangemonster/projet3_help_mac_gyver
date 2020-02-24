import pygame
from pygame.locals import *
from constants import *

from game import Game
class Window_win_lose:

    def __init__(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fpsClock = pygame.time.Clock()
        self.loop = True
        self.exit = True
        self.choice = 0
        
        ##PICTURES##
        self.you_won_img = pygame.image.load(you_won).convert_alpha()
        self.you_lost_img = pygame.image.load(you_lost).convert_alpha()
        self.continue_big = pygame.image.load(continue_big).convert_alpha()
        self.continue_small = pygame.image.load(continue_small).convert_alpha()
        self.exit = pygame.image.load(exit).convert_alpha()
        self.exit_small = pygame.image.load(exit_small).convert_alpha()
        ##SIZE##
       
        self.size = [120, 100]
        self.size_continue_big = [100, 450]
        self.size_continue_small = [200, 465]
        self.size_exit = [200, 550]
        self.size_exit_small = [250, 565]
        

    #@property
    def run(self, result):
        
        while self.loop:
            self.window.fill((0, 0, 0))
            self.window.blit(
                self.you_won_img if result == "win" 
                else self.you_lost_img, 
                self.size
            )
            if self.choice == 0:
                self.window.blit(self.continue_big, self.size_continue_big)
                self.window.blit(self.exit_small, self.size_exit_small)
            if self.choice == 1:
                self.window.blit(self.continue_small, self.size_continue_small)
                self.window.blit(self.exit, self.size_exit)
            self.handle_events()
            pygame.display.update()
            self.fpsClock.tick(30)


        
    def handle_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def handle_event(self, event):
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.loop = False
            self.exit = False
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choice == 0:
                    self.loop = False
                if self.choice == 1:
                    self.choice = "exit"
                    self.loop = False
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choice = 0
            elif event.key == K_DOWN:
                self.choice = 1

    def re_init(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fpsClock = pygame.time.Clock()
        self.loop = True
        self.choice = 0
