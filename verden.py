import random 
import pygame
from figur import Figur

class Verden(Figur):
    def __init__(self, vindu_bredde: int, verdener: list) -> None:
        super().__init__("bilder/pixel.forrurensing.png")
        # flytter ballen til startposisjonen
        self.bilde = pygame.transform.scale_by(self.bilde, 0.15)
        self.ramme = self.bilde.get_rect()
        self.colliding = True
        while self.colliding == True:
            self.ramme.left = random.randint(0, vindu_bredde - self.ramme.width)
            for verden in verdener:
                if self.ramme.colliderect(verden.ramme):
                    self.colliding = True
                else:
                    self.colliding = False
        self.ramme.top = 10 



    def fall(self,vindu_bredde:  int, vindu_høyde: int, bil_poeng):
        if self.ramme.top >= vindu_høyde:
            bil_poeng += 1
        self.ramme.y +=3
        return bil_poeng
    

            
        
        




