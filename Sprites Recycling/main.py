import pygame
import time
import random

from pygame.sprite import _Group

pygame.init()
screen_width = 900
screen_height = 700
screen= pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Recycle Game")

def set_background(image):
   bg = pygame.image.load(image)
   bg = pygame.transform.scale(image, (screen_width, screen_height))
   screen.blit(bg, (0,0))


class Bin(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load("bin.png")
      self.image = pygame.transform.scale(self.image, (40,60))
      self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
   def __init__(self, img):
      super().__init__()
      self.image = pygame.image.load(img)
      self.image = pygame.transform.scale(self.image, (30, 30))
      self.rect = self.image.get_rect()

class  Non_Recyclable(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load("Bag.png")
      self.image = pygame.transform.scale(self.image, (40,40))
      self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

bin = Bin()
allSprites.add(bin)

for i in range(20):
   plastic = Non_Recyclable()
   plastic.rect.x = random.randrange(screen_width)
   plastic.rect.y = random.randrange(screen_height)
   plastic_list.add(plastic)
   allSprites.add(plastic)

img = ["Match.png", "Box.png", "PaperBag.png"]

for i in range(50):
   item = Recyclable(random.choice(img))
   item.rect.x = random.randrange(screen_width)
   item.rect.y = random.randrange(screen_height)
   item_list.add(item)
   allSprites.add(item)

WHITE = (255, 255, 255)
RED = (255, 0 ,0)

playing = True
score= 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman")
text = myFont.render("Score = " + str(0), True, WHITE)