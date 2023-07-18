import pygame

pygame.init()

screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    print(pygame.event.get())

pygame.quit()