import pygame
from pygame.locals import *
from constants import *
from game import Game


class Menu:
    
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fpsClock = pygame.time.Clock()
        self.loop = True
        self.choice = 0
        ##PICTURES##
        self.mac = pygame.image.load(mac).convert_alpha()
        self.gyver = pygame.image.load(gyver).convert_alpha()
        self.logo = pygame.image.load(logo).convert_alpha()
        self.macgyver = pygame.image.load(macgyver_menu).convert_alpha()
        self.select_get_into_the_game = pygame.image.load(
            get_into_the_game).convert_alpha()
        self.chevron_select_left = pygame.image.load(
            chevron_left).convert_alpha()
        self.chevron_select_right = pygame.image.load(
            chevron_right).convert_alpha()
        self.enter = pygame.image.load(enter).convert_alpha()
        self.enter_small = pygame.image.load(enter_small).convert_alpha()
        self.exit = pygame.image.load(exit).convert_alpha()
        self.exit_small = pygame.image.load(exit_small).convert_alpha()
        self.info_menu = pygame.image.load(info_menu).convert_alpha()
        ##SIZE##
        self.size_banner_mac = [600, 20]
        self.size_banner_gyver = [-174, 20]
        self.size_banner_macgyver = [147.5, 120]
        self.size_banner_logo = [50, 125]
        self.size_get_into_the_game = [120, -20]
        self.size_chevron_select_left = [-30, 320]
        self.size_chevron_select_right = [600, 320]
        self.size_enter = [175, 450]
        self.size_enter_small = [232.5, 465]
        self.size_exit = [200, 550]
        self.size_exit_small = [250, 565]
        self.size_info_menu = [125, 375]

    #@property   
    def run(self):
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.play()
        while self.loop:
            if self.size_banner_mac[0] != 160:
                self.size_banner_mac[0] -= 2
            if self.size_banner_gyver[0] != 266:
                self.size_banner_gyver[0] += 2
            if self.size_get_into_the_game[1] != 320:
                self.size_get_into_the_game[1] += 2
            if self.size_chevron_select_left[0] != 80:
                self.size_chevron_select_left[0] += 1
            if self.size_chevron_select_right[0] != 490:
                self.size_chevron_select_right[0] -= 1        
            self.window.fill((0, 0, 0))
            self.window.blit(self.mac, self.size_banner_mac)        
            self.window.blit(self.gyver, self.size_banner_gyver)
            self.window.blit(self.logo, self.size_banner_logo)
            self.window.blit(self.macgyver, self.size_banner_macgyver)
            self.window.blit(self.select_get_into_the_game,
                            self.size_get_into_the_game)        
            self.window.blit(self.chevron_select_left,
                            self.size_chevron_select_left)
            self.window.blit(self.chevron_select_right,
                            self.size_chevron_select_right)        
            self.window.blit(self.info_menu, self.size_info_menu)
            if self.choice == 0:
                self.window.blit(self.enter,self.size_enter)
                self.window.blit(self.exit_small, self.size_exit_small)
            if self.choice == 1:
                self.window.blit(self.enter_small, self.size_enter_small)
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
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choice == 0:
                    self.choice = "run the game" 
                    self.loop = False
                if self.choice == 1:
                    self.loop = False
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choice = 0
            elif event.key == K_DOWN:
                self.choice = 1
                
