import pygame

pygame.init()


WIDTH = 1280
HEIGHT = 720

screen = pygame.display.setmode((WIDTH, HEIGHT))

pygame.display.setcaption("Square Chase")

x = 100
y = 100

enemyX = 300
enemyY = 300

vel = 5

enemyVel = 6

def gameWindow():
  
  screen.fill((0, 0, 0))
  
  pygame.draw.rect(screen, (0, 255, 0), (x, y, 30, 30))
  pygame.draw.rect(screen, (255, 0, 0), (enemyX, enemyY, 30, 30))
