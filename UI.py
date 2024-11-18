import pygame

class ui:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        




    def draw_text(self, text, font, col, x, y):
        self.text = str(text)
        self.x = x
        self.y = y
        self.col = col
        img = font.render(self.text, True, col)
        self.screen.blit(img, (x, y))

    def draw_button(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

        self.screen.blit(self.img, (self.rect.x, self.rect.y))
        return self.rect
        
