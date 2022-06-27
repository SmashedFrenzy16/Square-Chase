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
  pygame.display.update()
  
run = True

while run:
  
  pygame.time.delay(100)
  
  if enemyX < x - 10:
    
    enemyX = enemyX + enemyVel
    
  elif enemyX > x + 10:
    
    enemyX = enemyX - enemyVel
    
   if enemyY < y - 10:
    
    enemyY = enemyY - enemyVel
    
  elif enemyY > y + 10:
    
    enemyY = enemyY + enemyVel
    
  else:
    
    run = False
    
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      
      run = False
  
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
            x -= vel

  if keys[pygame.K_RIGHT]:
        x += vel
      
  if keys[pygame.K_UP]:
        y += vel
      
  if keys[pygame.K_DOWN]:
        y -= vel
      
  gameWindow()
  
pygame.quit()
