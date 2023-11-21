import pygame, random

#Klasser
from bil import Bil
from verden import Verden
from greta import Greta


# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# keegas = pygame.image.load("bilder/keegas.jpg")
# keegas = pygame.transform.scale_by(keegas, 0.8)
# keegasramme = keegas.get_rect()
# keegasramme.topleft = (0,0)

overskrift_font = pygame.font.SysFont("Arial", 25)
underskrift_font = pygame.font.SysFont("Arial", 16)

bil = Bil(BREDDE, HOYDE)
verdener = []

verden = Verden(BREDDE)
verden2 = Verden(BREDDE )
verden3 = Verden(BREDDE)
greta = Greta(BREDDE)



bil.ramme.y = 475
bil.liv = 3

verden.ramme.top = greta.ramme.bottom 
verden2.ramme.top = greta.ramme.bottom
verden3.ramme.top = greta.ramme.bottom

verdener.append(verden)
verdener.append(verden2)
verdener.append(verden3)



tape = pygame.display.set_mode((BREDDE, HOYDE))
vinne = pygame.display.set_mode((BREDDE, HOYDE))



def Gameover(tape):
    font = pygame.font.SysFont(None, 100)
    text = font.render("GAME OVER", True, "red")
    tape.blit(text, (90, 250))
    pygame.display.update()
    
def Won(vinne):
    font = pygame.font.SysFont(None, 100)
    text = font.render("GRATULERER", True, "green")
    vinne.blit(text, (70, 250))
    pygame.display.update()


while True:

    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        

    if bil.poeng == 30:
        Won(vinne)
        pygame.time.delay(2000) 
        pygame.quit()
        raise SystemExit
    elif bil.liv == 0:
        Gameover(tape)
        pygame.time.delay(2000) 
        pygame.quit()
        raise SystemExit 
  
    


    

    for i in verdener:
        if i.ramme.colliderect(bil.ramme):
            bil.liv -= 1
            i.ramme.bottom = 0
            i.ramme.top = greta.ramme.bottom
            while True:
                i.ramme.left = random.randint(0, BREDDE - i.ramme.width)
                collides = any(i.ramme.colliderect(v.ramme) for v in verdener if v != i)
                if not collides:
                  break

    for i in verdener:
        if i.ramme.top > HOYDE:
            i.ramme.top = greta.ramme.bottom
            bil.poeng += 1
            while True:
                i.ramme.left = random.randint(0, BREDDE - i.ramme.width)
                
                collides = any(i.ramme.colliderect(v.ramme) for v in verdener if v != i)
                if not collides:
                    break


    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        bil.flytt(-5)
    if taster[pygame.K_RIGHT]:
        bil.flytt(5)
    if taster[pygame.K_UP]:
        bil.opp(5) 
    if taster[pygame.K_DOWN]:
        bil.ned(5)  





    # 3. Oppdater spill
    bil.poeng = verden.fall(40, BREDDE, bil.poeng)
    bil.poeng = verden2.fall(40, BREDDE, bil.poeng)
    bil.poeng = verden3.fall(40, BREDDE, bil.poeng)
   
    
    

    # 4. Tegn

    vindu.fill("white")
    # vindu.blit(keegas,keegasramme)
    bil.tegn(vindu)
    verden.tegn(vindu )
    verden2.tegn(vindu)
    verden3.tegn(vindu)
    greta.tegn(vindu)
    


    poeng_surface = overskrift_font.render("POENG: "+str(bil.poeng), True, "black")
    liv_surface = overskrift_font.render("LIV: "+str(bil.liv), True, "black")
    regler_surface = underskrift_font.render("Du kan bevege deg med alle 4 piltaster, du trenger 30 poeng for å vinne!  Lykke til ", True, "red")
   
    

    vindu.blit(poeng_surface, (0,0))
    vindu.blit(liv_surface, (0,25))
    vindu.blit(regler_surface, (15,570))


    pygame.display.flip()
    klokke.tick(FPS)