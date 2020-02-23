import pygame
from pygame.locals import *
from constants import *
from maze import Maze


class Game:

    def __init__(self):
        #Initialisation de la bibliothèque Pygame
        pygame.init()
        # Création de la fenêtre avec une taille variable en fonction de la taille que je dèsire donner aux sprites
        self.window = pygame.display.set_mode((height, height+40))
        # nomer la fenêtre
        pygame.display.set_caption('MAZE')

        # fichier du labyrinthe stocké dans une variable
        self.path = "maze"
        # Remplissage de l'arrière-plan sur toute la surface de ma fenêtre
        self.background = pygame.Surface(self.window.get_size())
        # convertir
        self.background = self.background.convert()
        # choix de la couleur
        self.background.fill((0, 0, 0))
        
        # création du labyrinthe

        # instance de la classe Maze avec mon fichier path à initialiser
        self.maze = Maze(self.path)
        # générer le labyrinthe
        self.maze.generate()
        self.maze.random_items()
        # création de mac giver
        # instance de class macgyver parent ou enfant l'instance de la class Maze (héritage)
        self.macgiver = self.maze.get_mc_pos()
        self.positon_picture = picture_macgiver
        self.pos_item = self.maze.get_item_pos()
        self.continued = 1
        self.nb = 0
        self.x = (self.macgiver % nb_of_sprite) * height_of_sprite
        self.y = (self.macgiver // nb_of_sprite) * height_of_sprite
        self.items = []
        self.result = None
        

    def run(self):

        #Boucle infinie
        while self.continued:
            #Limitation de vitesse de la boucle
            pygame.time.Clock().tick(60)

            self.handle_events()

            #Blitter le background dans la fenêtre
            
            self.window.blit(self.background, (0, 0))
            # afficher le labyrinthe
            self.draw()
            self.show_the_items()
            #Blitter la position de macgiver dans la fenêtre
            self.window.blit(pygame.image.load(self.positon_picture).convert_alpha(), (self.x, self.y))
            #Rafraichissement
            pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            self.handle_event(event)           

    def handle_event(self, event):
        if event.type == KEYDOWN:
            #Touches de déplacement de macgyver
            if event.key == K_RIGHT:
                self.positon_picture = picture_macgiver_right
                self.move(right)
            elif event.key == K_LEFT:
                self.positon_picture = picture_macgiver_left
                self.move(left)
            elif event.key == K_UP:
                self.positon_picture = picture_macgiver_back
                self.move(up)
            elif event.key == K_DOWN:
                self.positon_picture = picture_macgiver
                self.move(down)
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.continued = 0

    def draw(self):
        # afficher le labyrinthe
        self.maze.draw(self.window)

    def move(self, shift):
        if self.macgiver % 15 == 0 and shift == left:
            return
        if (self.macgiver+1) % 15 == 0 and shift == right:
            return
        if self.macgiver < 15 and shift == up:
            return
        if self.macgiver > 209 and shift == down:
            return
        if self.maze.data[self.macgiver+shift] == "W":
            return
        if self.maze.data[self.macgiver+shift] in ("S", "N", "T"):
            self.items += self.maze.data[self.macgiver+shift]
            self.maze.data[self.macgiver+shift] = "E" 
        if self.maze.data[self.macgiver+shift] == "G":
            self.maze.data[self.macgiver+shift] = "E"
            self.fight_guardian()
        if self.maze.data[self.macgiver+shift] in ("E", "M"):
            self.x = ((self.macgiver+shift) %
                      nb_of_sprite) * height_of_sprite
            self.y = ((self.macgiver+shift) //
                      nb_of_sprite) * height_of_sprite
            self.macgiver += shift



    def fight_guardian(self):
            if len(self.items) == 3:
                #print("you won!")
                self.result = "you won!"
                self.continued = 0
                
                
            else:
                #print("you lose!")
                self.result = "you lose!"
                self.continued = 0
                

    def show_the_items(self):
        if len(self.items) != self.nb:
            self.maze.data[self.pos_item+self.nb] = self.items[self.nb]
            self.nb +=1


    def re_init(self):
        #Initialisation de la bibliothèque Pygame
        pygame.init()
        # Création de la fenêtre avec une taille variable en fonction de la taille que je dèsire donner aux sprites
        self.window = pygame.display.set_mode((height, height+40))
        # nomer la fenêtre
        pygame.display.set_caption('MAZE')

        # fichier du labyrinthe stocké dans une variable
        self.path = "maze"
        # Remplissage de l'arrière-plan sur toute la surface de ma fenêtre
        self.background = pygame.Surface(self.window.get_size())
        # convertir
        self.background = self.background.convert()
        # choix de la couleur
        self.background.fill((0, 0, 0))

        # création du labyrinthe

        # instance de la classe Maze avec mon fichier path à initialiser
        self.maze = Maze(self.path)
        # générer le labyrinthe
        self.maze.generate()
        self.maze.random_items()
        # création de mac giver
        # instance de class macgyver parent ou enfant l'instance de la class Maze (héritage)
        self.macgiver = self.maze.get_mc_pos()
        self.positon_picture = picture_macgiver
        self.pos_item = self.maze.get_item_pos()
        self.continued = 1
        self.nb = 0
        self.x = (self.macgiver % nb_of_sprite) * height_of_sprite
        self.y = (self.macgiver // nb_of_sprite) * height_of_sprite
        self.items = []
        self.result = None
# interface se dessine et on peut lui specifier le sac

# le jeu est reponsable des trois etats win lose run 

# l'état change 
 
# sourcetree atlassian faire git push chaque jour master pas touch ... branche dev 
# trelo
