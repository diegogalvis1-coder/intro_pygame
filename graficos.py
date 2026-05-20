import pygame
import sys
import math

pygame.init()

ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption("Dibujar formas básicas")

negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0,255,255)

PI = math.pi
clock = pygame.time.Clock()

# FUENTE FUERA DEL LOOP
fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(negro)

    pygame.draw.line(ventana, rojo, (0,0), (400,400), 5)
    pygame.draw.line(ventana, rojo, (0,400), (400,0), 5)

    puntos_1 = [(0,0), (50,100), (100,50), (250,200), (400,400)]
    puntos_2 = [(200,0), (400,200), (200,400), (0,200)]

    pygame.draw.lines(ventana, naranja, False, puntos_1, 3)
    pygame.draw.lines(ventana, naranja, True, puntos_2, 3)

    pygame.draw.rect(ventana, azul, (150,150,50,50))
    pygame.draw.rect(ventana, verde, ((200,200), (50,50)), 3)

    puntos_3 = [(100,200), (200,300), (100,400), (0,300)]
    pygame.draw.polygon(ventana, amarillo, puntos_3, 3)

    puntos_4 = [(200,100), (300,200), (400,100), (300,0)]
    pygame.draw.polygon(ventana, amarillo, puntos_4, 3)

    puntos_5 = [(200,0), (150,150), (0,200), (150,250), (200,400),
                (250,250), (400,200), (250,150), (200,0)]
    pygame.draw.polygon(ventana, azul, puntos_5, 3)

    pygame.draw.circle(ventana, blanco, (300,300), 100, 0)

    pygame.draw.ellipse(ventana, naranja, (200,250,200,100), 3)
    pygame.draw.ellipse(ventana, naranja, (250,200,100,200), 3)

    pygame.draw.arc(ventana, cian, (200,0,200,200), PI/4, 7*PI/4, 3)

    texto = fuente_arial.render("diego alejandro", 1, blanco)
    ventana.blit(texto, (0,50))

    pygame.display.flip()