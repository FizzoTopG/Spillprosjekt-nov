import random 
import pygame
from figur import Figur

class Verden(Figur):
    def __init__(self, vindu_bredde: int) -> None:
        super().__init__("bilder/pixel.forrurensing.png")
        # flytter ballen til startposisjonen
        self.bilde = pygame.transform.scale_by(self.bilde, 0.2)
        self.ramme = self.bilde.get_rect()
        self.ramme.left = random.randint(0, vindu_bredde - self.ramme.width)
        self.ramme.top = 0
        
        

    def fall(self, vindu_høyde: int, bil_poeng):
        if self.ramme.top > vindu_høyde:
            bil_poeng += 1
            self.ramme.bottom = 0
        self.ramme.y +=3
        return bil_poeng

        