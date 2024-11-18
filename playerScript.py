import pygame
import os
import sys


class Player:
    def __init__(self, x, y, screen, game):
        self.image = pygame.image.load(self.resource_path("Images\Player\Flappy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen
        self.keydown = False
        self.game = game
        self.pointcollider = False

        self.gravty = 0.5
        self.lift = -10
        self.vel = 0

    def resource_path(self, relative_path):
        """Get the absolute path to a resource, compatible with PyInstaller."""
        try:
            # PyInstaller stores files in a temporary folder during runtime
            base_path = sys._MEIPASS
        except AttributeError:
            # During development, use the script directory
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


    def add(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        
        if self.game.play:
            self.vel += self.gravty
        else:
            pos = pygame.mouse.get_pos()
            self.game.ui.draw_text(f"Flappy Fly", self.game.titleFont, (0,0,0), self.game.screen_width//2-120, self.game.screen_height//2-300)
            start_b = self.game.ui.draw_button(self.game.screen_width//2, self.game.screen_height//2, self.game.start_B_img)
            exit_b = self.game.ui.draw_button(self.game.screen_width//2, self.game.screen_height//2+100, self.game.exit_b_img)
            if exit_b.collidepoint(pos):
                 if pygame.mouse.get_pressed()[0] == 1:
                    self.game.exitfunc()

            if start_b.collidepoint(pos):
                 if pygame.mouse.get_pressed()[0] == 1:
                    self.game.play = True
                    self.game.alive = True
                    self.vel = -2
                    self.game.ui.points = 0
                    self.rect.y = self.game.screen_height/2
                    for pipe in self.game.toppipes + self.game.bottompipes:
                        pipe.creater()
                        pipe.vel = -2
                        
            

        if self.game.alive == True:
            for event in self.game.events:
                if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w and not self.keydown and self.game.play:
                                self.keydown = True
                                self.vel = self.lift
                                self.screen.blit(pygame.transform.rotate(self.image, 30), self.rect)
                                
                                    
                            
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w and self.keydown:
                                self.keydown = False
        
        self.rect.y += self.vel

        if self.rect.top < 0:
                self.rect.top = 0
                self.vel = 0

        for i in self.game.bottompipes + self.game.toppipes:
            if self.rect.colliderect(i):
                self.die()
            if self.rect.colliderect(i.point_rect):
                if not self.pointcollider:
                    self.pointcollider = True
                    if self.game.alive:
                        self.game.ui.points += 1
                    print(self.game.ui.points )
            else:
                if not any(self.rect.colliderect(pipe.point_rect) for pipe in self.game.bottompipes + self.game.toppipes):
                    self.pointcollider = False
            
                
        
        
                
        if self.rect.bottom > 900:
            self.die()
        else:  
            self.add()

    def die(self):
        if self.rect.bottom > 900:
            self.rect.bottom = 900
            
        
        self.game.alive = False
        self.vel += self.gravty
        self.game.ui.points = self.game.ui.points
        self.game.play = False
        self.screen.blit(pygame.transform.rotate(self.image, -30), self.rect)

        for pipe in self.game.toppipes + self.game.bottompipes:
            pipe.vel = 0
        
                            
        

                        
            

            
            
                
                    


