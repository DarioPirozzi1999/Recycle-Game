import pygame
import time
import random

pygame.init()
screen_width = 900
screen_height = 700
screen= pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Recycle Game")

def set_background(image):
   bg = pygame.image.load(image)
   bg = pygame.transform.scale(bg, [screen_width, screen_height])
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
GREEN = (0, 255, 0)

playing = True
score= 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman", 20)
text = myFont.render("Score = " + str(0), True, WHITE)

while True:
   clock.tick(60)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         playing = False
   timeElapsed = time.time()-start_time
   if timeElapsed >= 60:
      if score >= 20:
         screen.fill("green")
         text = myFont.render("Bin loot successful", True, RED)
      else:
         screen.fill("red")
         text = myFont.render("Bin loot unsuccessful", True, GREEN)
      screen.blit(text, (20, 10))
   else:
      set_background("Background.png")
      countDown = myFont.render("Time Left:" + str(60- int(timeElapsed)), True, WHITE)
      screen.blit(countDown, (20, 10))
   
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP]:
         if bin.rect.y > 0:
            bin.rect.y -= 5
      elif keys[pygame.K_DOWN]:
         if bin.rect.y<700:
            bin.rect.y += 5
      elif keys[pygame.K_LEFT]:
         if bin.rect.x>0:
            bin.rect.x -=5
      elif keys[pygame.K_RIGHT]:
         if bin.rect.x<900:
            bin.rect.x += 5

      item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)
      plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)

      for item in item_hit_list:
         score+=1
         text = myFont.render("Score ="+ str(score), True, WHITE)
      for item in plastic_hit_list:
         score -=5
         text = myFont.render("Score =" + str(score), True, WHITE)
   screen.blit(text, (20, 50))
   allSprites.draw(screen)
   pygame.display.update()

pygame.quit()   

