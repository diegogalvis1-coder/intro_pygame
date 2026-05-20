import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ciudad de Hierro - Nivel Básico")

# Colores
CIELO = (135, 206, 235)
PASTO = (34, 139, 34)
GRIS = (100, 100, 100)
ROJO = (200, 0, 0)
AMARILLO = (255, 223, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 165, 0)

font = pygame.font.SysFont("Arial", 30)

#  Pac-Man (VISIBLE Y SIMPLE)
def dibujar_pacman(x, y):
    pygame.draw.circle(screen, AMARILLO, (x, y), 25)

    boca = [
        (x, y),
        (x + 37, y - 15),
        (x + 37, y + 15)
    ]
    pygame.draw.polygon(screen, NEGRO , boca)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fondo
    screen.fill( CIELO)

    # pasto
    pygame.draw.rect(screen, PASTO, (0, 450, 800, 150))

    # camino
    pygame.draw.rect(screen, GRIS, (0, 500, 800, 40))

    # taquilla
    pygame.draw.rect(screen, ROJO, (50, 350, 100, 100))
    pygame.draw.rect(screen, NEGRO, (50, 350, 100, 100), 2)
    pygame.draw.rect(screen, BLANCO, (75, 370, 50, 40))

    # rueda
    pygame.draw.circle(screen, NEGRO, (500, 250), 150, 3)
    pygame.draw.circle(screen, NARANJA, (500, 250), 10)

    pygame.draw.line(screen, GRIS, (500, 250), (650, 250), 3)
    pygame.draw.line(screen, GRIS, (500, 250), (350, 250), 3)
    pygame.draw.line(screen, GRIS, (500, 250), (500, 100), 3)
    pygame.draw.line(screen, GRIS, (500, 250), (500, 400), 3)

    # castillo
    pygame.draw.polygon(screen, NEGRO, [(180, 350), (280, 250), (380, 350)])
    pygame.draw.rect(screen, GRIS, (200, 350, 160, 100))

    # sol
    pygame.draw.circle(screen, AMARILLO, (700, 80), 40)

    # texto
    texto = font.render("CIUDAD DE HIERRO", True, NEGRO)
    screen.blit(texto, (200, 20))

    #  PAC-MAN (IMPORTANTE: AL FINAL)
    dibujar_pacman(150, 520)
    dibujar_pacman(250, 520)
    dibujar_pacman(350, 520)

    pygame.display.flip()


