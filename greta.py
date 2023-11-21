from figur import Figur
import pygame
import random

class Greta(Figur):
    def __init__(self, vindu_bredde) -> None:
        super().__init__("bilder/pixel.greta.png")
        self.bilde = pygame.transform.scale_by(self.bilde, 0.2)
        self.ramme = self.bilde.get_rect()
        self.ramme.left = (vindu_bredde - self.ramme.width) / 2
        self.ramme.top = 10
        
        