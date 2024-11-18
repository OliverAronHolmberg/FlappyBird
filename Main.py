import pygame
import sys
from playerScript import Player
from pipe import Pipe
from UI import ui
import random
import json
import os

class Game:
    def __init__(self):

    

        # Init
        pygame.init()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.timer = 0

        # Screen
        self.screen_width = 600
        self.screen_height = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  
        pygame.display.set_icon(pygame.image.load(self.resource_path("Images\Player\Flappy.png")).convert_alpha())
        pygame.display.set_caption("Flappy Bird")

        # Player
        
        self.player = Player(50, (self.screen_height/2), self.screen, self)
        self.down = False
        self.y_vel = 20
        self.keydown = False
        
        #Score
        self.file_name = "Values.txt"
        

        
        #State
        self.alive = True
        self.ui = ui(self.screen)
        self.play = False
        #Text
        self.pointfont = pygame.font.SysFont("Arial", 30)
        self.titleFont = pygame.font.SysFont("Arial", 50)
        #Button
        self.start_B_img = pygame.image.load(self.resource_path("Images\Buttons\Play.png")).convert_alpha()
        self.exit_b_img = pygame.image.load(self.resource_path("Images\Buttons\Exit.png")).convert_alpha()

        self.random_height_var = 0
        #Pipes
        self.pipegap = 200
        self.toppipes = [  Pipe(self.screen_width+100, self.screen, self, True, 0),
                        
                        Pipe(self.screen_width+400, self.screen, self, True, 1),
                        
                        Pipe(self.screen_width+700, self.screen, self, True, 2),
                        ]
        

                        
        self.bottompipes = [Pipe(self.screen_width+100, self.screen, self, False, 0),
                            
                            Pipe(self.screen_width+400, self.screen, self, False, 1),

                            Pipe(self.screen_width+700, self.screen, self, False, 2),
                            ]
        self.update_pipes()


        
    def resource_path(self, relative_path):
            
        try:
                # PyInstaller stores files in a temporary folder during runtime
            base_path = sys._MEIPASS
        except AttributeError:
                # During development, use the script directory
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

        
        
    def update_pipes(self):
        for i in range(len(self.toppipes)):
            top_pipe = self.toppipes[i]
            bottom_pipe = self.bottompipes[i]

            top_pipe.update()

            bottom_pipe.update_wdith_top_pipe(top_pipe, self.pipegap)

        
    def exitfunc(self):
        pygame.quit()
        sys.exit()



    

    def main_loop(self):
        while True:
            
            
                

            self.events = pygame.event.get()
            self.screen.fill((0,200,255)) 
            self.clock.tick(self.fps)
            
                
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.exitfunc()
                    
            if self.play:
                self.update_pipes()

                
            
            
                
                self.ui.draw_text(f"Points: {self.ui.points}", self.pointfont, (0,0,0), 20, self.screen_height//2-400)
            for pipe in self.toppipes + self.bottompipes:
                    self.screen.blit(pipe.image, pipe.rect)

            self.player.update()

            
            
            pygame.display.flip()

Game().main_loop()