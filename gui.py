import pygame
from pygame.locals import *
from constants import *
from game import Game


class Gui:
    
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fpsClock = pygame.time.Clock()
        self.loopGuiMenu = True
        self.loopGuiMessage = True
        self.exit = True
        self.choiceGuiMenu = 0
        self.choiceGuiMessage = 0

                ##PICTURES OF GUI MENU##
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

                ##PICTURES OF GUI MESSAGE##
        self.you_won_img = pygame.image.load(you_won).convert_alpha()
        self.you_lost_img = pygame.image.load(you_lost).convert_alpha()
        self.continue_big = pygame.image.load(continue_big).convert_alpha()
        self.continue_small = pygame.image.load(continue_small).convert_alpha()
        

                ##SIZE OF GUI MENU##
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

                ##SIZE OF GUI MESSAGE##
        self.size = [120, 100]
        self.size_continue_big = [100, 450]
        self.size_continue_small = [200, 465]
       

     
    def runGuiMenu(self):
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.play()
        while self.loopGuiMenu:
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
            self.drawGuiMenu()
            self.handleEventsGuiMenu()
            pygame.display.update()
            self.fpsClock.tick(30)

    def drawGuiMenu(self):
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
        if self.choiceGuiMenu == 0:
            self.window.blit(self.enter,self.size_enter)
            self.window.blit(self.exit_small, self.size_exit_small)
        if self.choiceGuiMenu == 1:
            self.window.blit(self.enter_small, self.size_enter_small)
            self.window.blit(self.exit, self.size_exit) 
    
    def runGuiMessage(self, result):
        while self.loopGuiMessage:
            self.window.fill((0, 0, 0))
            self.window.blit(
                self.you_won_img if result == "win" 
                else self.you_lost_img, 
                self.size
            )
            if self.choiceGuiMessage == 0:
                self.window.blit(self.continue_big, self.size_continue_big)
                self.window.blit(self.exit_small, self.size_exit_small)
            if self.choiceGuiMessage == 1:
                self.window.blit(self.continue_small, self.size_continue_small)
                self.window.blit(self.exit, self.size_exit)
            self.handleEventsGuiMessage()
            pygame.display.update()
            self.fpsClock.tick(30)

    def handleEventsGuiMenu(self):
        for event in pygame.event.get():
            self.handleEventGuiMenu(event)

    def handleEventGuiMenu(self, event):
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.loopGuiMenu = False
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choiceGuiMenu == 0:
                    self.choiceGuiMenu = "enter" 
                    self.loopGuiMenu = False
                if self.choiceGuiMenu == 1:
                    self.loopGuiMenu = False
                
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choiceGuiMenu = 0
            elif event.key == K_DOWN:
                self.choiceGuiMenu = 1

    def handleEventsGuiMessage(self):
        for event in pygame.event.get():
            self.handleEventGuiMessage(event)
                
    def handleEventGuiMessage(self, event):
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.loopGuiMessage = False
            self.exit = False
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choiceGuiMessage == 0:
                    self.loopGuiMessage = False
                if self.choiceGuiMessage == 1:
                    self.choiceGuiMessage = "exit"
                    self.loopGuiMessage = False
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choiceGuiMessage = 0
            elif event.key == K_DOWN:
                self.choiceGuiMessage = 1


    def reInit(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fpsClock = pygame.time.Clock()
        self.loopGuiMenu = True
        self.loopGuiMessage = True
        self.choiceGuiMenu = 0
        self.choiceGuiMessage = 0