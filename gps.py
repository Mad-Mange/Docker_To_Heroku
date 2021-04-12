import pygame, sys

pygame.init()

pygame.display.set_caption("Gps Tracker")
SCREEN = pygame.display.set_mode((407, 785))

BG = pygame.image.load("assets/gps.png")

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.blit(BG, (0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()