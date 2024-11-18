import pygame
import random
import os
import sys

class Pipe:
    def __init__(self, spawnx, screen, game, flipped, num):
        self.image = pygame.image.load(self.resource_path("Images\Pipes\pipe.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = spawnx
        self.screen = screen
        self.game = game
        self.flipped = flipped
        if self.flipped:
            self.image = pygame.transform.flip(self.image, False, True)
        self.image = pygame.transform.scale(self.image, (self.rect.width*3, self.rect.height*3))
        self.rect.width *= 3
        self.rect.height *= 3
        self.vel = -2
        self.num = num
        self.creater()


    def resource_path(self, relative_path):
        
        try:
            # PyInstaller stores files in a temporary folder during runtime
            base_path = sys._MEIPASS
        except AttributeError:
            # During development, use the script directory
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
        

        
    def creater(self):
        if self.flipped:
            self.rect.y = random.randint(-600, -200)
            if self.num == 0:
                self.rect.x = self.game.screen_width+100
            if self.num == 1: 
                self.rect.x = self.game.screen_width+400
            if self.num == 2:
                self.rect.x = self.game.screen_width+700
        else:
            if self.num == 0:
                self.rect.y = self.game.toppipes[self.num].rect.y + self.game.toppipes[self.num].rect.height + self.game.pipegap
                self.rect.x = self.game.screen_width+100
            if self.num == 1: 
                self.rect.y = self.game.toppipes[self.num].rect.y + self.game.toppipes[self.num].rect.height + self.game.pipegap
                self.rect.x = self.game.screen_width+400
            if self.num == 2:
                self.rect.y = self.game.toppipes[self.num].rect.y + self.game.toppipes[self.num].rect.height + self.game.pipegap
                self.rect.x = self.game.screen_width+700
        self.point_rect = pygame.Rect(self.rect.left+self.rect.width//2, 0, self.rect.width//2, self.game.screen_height) 
        
        

    def update(self):
        self.point_rect.x += self.vel
        self.rect.x += self.vel
        if self.rect.x <= -100:
            self.rect.x = self.game.screen_width+200
            self.point_rect.x = self.game.screen_width+200
            if self.flipped:
                self.rect.y = random.randint(-600, -200)
        
        return self.rect
                            
    def update_wdith_top_pipe(self, toppipe, gap):
        self.rect.x += self.vel
        if self.rect.x <= -100:
            
            self.rect.x = toppipe.rect.x
            if self.flipped:
                self.rect.y = random.randint(-600, -200)
            else:
                self.rect.y = toppipe.rect.y + toppipe.rect.height + gap
            
        return self.rect               