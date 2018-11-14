import sys
import pygame
print(pygame.version)
print(sys.version)

#Initialize Pygame
pygame.init()
#Set the size of the window of the game
win = pygame.pygame.display.set_mode((800, 800))
pygame.display.set_caption('Atago.')
#This is the size of Atago
x = 50
y = 50
width, height = 40, 60
velocity = 5 #(Movement speed can increase with power ups)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False

pygame.quit()
