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

#I need a way to handle events in pygame

class HandleEvent:
	def init

run = True
while run:
    #Movement in game.
    for event in pygame.event.get():
        #This part is the movement of the character (You can hold buttons and shit too)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('down')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up stop')
            if event.key == pygame.K_DOWN  or event.key == ord('s'):
                print('down stop')
		if event.type == pygame.
                
        if event.type == 
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
           
