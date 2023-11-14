import pygame
import random
from bil import Bil
from verden import Verden


# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 25)

bil = Bil(BREDDE, HOYDE)
verden = Verden(BREDDE)

bil.ramme.y = 475

bil.liv = 3


while True:

    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if bil.poeng == 110:
            pygame.quit()
            raise SystemExit
    
    if verden.ramme.colliderect(bil.ramme):
        bil.liv -= 1
        verden.ramme.bottom = 0



    

    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        bil.flytt(-3)
    if taster[pygame.K_RIGHT]:
        bil.flytt(3)
        

    # 3. Oppdater spill
    bil.poeng = verden.fall(BREDDE, bil.poeng)

    # 4. Tegn

    vindu.fill("white")
    bil.tegn(vindu)
    verden.tegn(vindu)

    poeng_surface = overskrift_font.render(str(bil.poeng), True, "black")
    liv_surface = overskrift_font.render(str(bil.liv), True, "black")
   
    

    vindu.blit(poeng_surface, (0,0))
    vindu.blit(liv_surface, (550,0))

    pygame.display.flip()
    klokke.tick(FPS)