import pygame
import math
from random import randint
import sys

"""This class stores all the random elements in the game that I can think of. Of course, there will be more random elements, however this should suffice for now."""
class Random_Elements:

    def __init__(self, coin_sideup, d12_side_up, d6_side_up, d20_side_up):
        self.coin_sideup = "Heads"
        self.d6_side_up = "6"
        self.d12_side_up = "12"
        self.d20_side_up = "20"

    def flip_coin(self):
        for i in range(randint(0, 1)):
            if i == 0:
                self.sideup = 'Heads'
            else:
                self.sideup = 'Tails'

    def get_coin_side_up(self):
        return self.sideup
    
    #Dice Rolling Elements
    def toss_d12(self):
        for i in range(1, 13):
            if i == 1:
                self.d12_side_up = '1'
            elif i == 2:
                self.d12_side_up = '2'
            elif i == 3:
                self.d12_side_up = '3'
            elif i == 4:
                self.d12_side_up = '4'
            elif i == 5:
                self.d12_side_up = '5'
            elif i == 6:
                self.d12_side_up = '6'
            elif i == 7:
                self.d12_side_up = '7'
            elif i == 8:
                self.d12_side_up = '8'
            elif i == 9:
                self.d12_side_up = '9'
            elif i == 10:
                self.d12_side_up = '10'
            elif i == 11:
                self.d12_side_up = '11'
            else:
                self.d12_side_up = '12'
    
    def get_d12_sideup(self):
        return self.d12_side_up
    
    def toss_d6(self):
        for i in range(1, 7):
            if i == 1:
                self.d6_side_up = '1'
            elif i == 2:
                self.d6_side_up = '2'
            elif i == 3:
                self.d6_side_up = '3'
            elif i == 4:
                self.d6_side_up = '4'
            elif i == 5:
                self.d6_side_up = '5'
            else:
                self.d6_side_up = '6'
            
    def get_d6_sideup(self):
        return self.d6_side_up
    
    def toss_d20(self):
        for i in range(1, 20):
            if i == 1:
                self.d20_side_up = '1'
            elif i == 2:
                self.d20_side_up = '2'
            elif i == 3:
                self.d20_side_up = '3'
            elif i == 4:
                self.d20_side_up = '4'
            elif i == 5:
                self.d20_side_up = '5'
            elif i == 6:
                self.d20_side_up = '6'
            elif i == 7:
                self.d20_side_up = '7'
            elif i == 8:
                self.d20_side_up = '8'
            elif i == 9:
                self.d20_side_up = '9'
            elif i == 10:
                self.d20_side_up = '10'
            elif i == 11:
                self.d20_side_up = '11'
            elif i == 12:
                self.d20_side_up = '12'
            elif i == 13:
                self.d20_side_up = '13'
            elif i == 14:
                self.d20_side_up = '14'
            elif i == 15:
                self.d20_side_up = '15'
            elif i == 16:
                self.d20_side_up = '16'
            elif i == 17:
                self.d20_side_up = '17'
            elif i == 18:
                self.d20_side_up = '18'
            elif i == 19:
                self.d20_side_up = '19'
            else:
                self.d20_side_up = '20'
    
    def get_d20_sideup(self):
        return self.d20_side_up

#Use complex numbers to represent the motion of the object?

#First let's create some characters!
#Very short story, fight a few minions, then fight a boss and you win.
#You also need to include possible actions for your character.

class Character():
    #I define the characters here. But I'm not sure how to proceed here
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
    img = pygame.image.load(os.path.join('images','hero.png')).convert()
    self.images.append(img)
    self.image = self.images[0]
    self.rect  = self.image.get_rect()

    def __init__(self, health, attack, defense, movement_speed):
        pygame.sprite.Sprite.__init(self)
        self.images = []
        img = pygame.image.load(os.path.join('images')).convert
        self.health = health
        self.attack = attack
        self.defense = defense
        self.movement_speed

        #Defense works by a scale multiplier of 10. So base attack for the hero is 100, and when you attack a basic enemey it kills them in 2 shots
        #Harder opponents such as semi_basic_Enemy have 4 attacks to kill.
        #Boss takes 30 shots to kill.
        #Defense for basic is 10. So they take 10% less damage. Basic enemy will have 180 hp
        #Defense for Semi_basic_Enemy is 350

    def stat_returner(self):
        return health
        return attack
        return defense
        return movement_speed

    def 
    
class Atago(Character):
    def __init__(self):
        pygame.spriteSprite.__init__(self):
        
        self.image = pygame.Surface[(40, 40)];
        pygame.sprite.Sprite.update()
        
        
#Kinda Stuck here Gonna have to read on how to use super classes
class Basic_Enemy(Character):
    super.__init()

class Bullets(pygame.sprite.Sprite):
    #I really don't want to use globals here so I will just probably use localized variables.
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self):

        self.image = pygame.Surface[(15, 15)]
        
