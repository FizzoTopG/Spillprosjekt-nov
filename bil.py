from figur import Figur
import pygame

class Bil(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/pixel-r8.png")
        self.poeng = 0
        self.liv = 3
        self.bilde = pygame.transform.scale_by(self.bilde, 0.2)
        self.ramme = self.bilde.get_rect()
        
        #setter bilen i startposisjon
        self.ramme.centerx = vindu_bredde / 2
        self.ramme.bottom = vindu_høyde 

    def flytt(self, dx: int):
        self.ramme.x += dx

    def opp(self, dy):
        self.ramme.y -= dy

    def ned(self, dy):
        self.ramme.y += dy

   


    