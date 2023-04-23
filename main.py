import pygame
import sys
from debug import debug

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("JetlikVeszedelme")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

bg_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("Hello World!", False, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (100, 100))
    debug(pygame.mouse.get_pos(), 10, 10)

    pygame.display.update()
    clock.tick(60)
