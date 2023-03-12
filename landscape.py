
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Mr Veknin helped me B)
def draw_cloud(x,y):
    pygame.draw.circle(screen,white,(x,y), cloud_radius)
    pygame.draw.circle(screen,white,(x + 15,y + 12), cloud_radius)
    pygame.draw.circle(screen,white,(x + 30,y), cloud_radius)


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
#  variables


cloud_x = 0
cloud_y = 0
cloud_radius = 19
circle_x = 21
circle_y = 10
light_blue = (142, 188, 229)
yellow = (255, 255, 0)
white  = (255, 255, 255)
green  = (0, 255, 0)
tree_green = (66, 105, 47)
black  = (0, 0, 0)
grey = (128, 128, 128)
shade = (100, 100, 100)
brown = (165, 42, 42)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            print (event.pos)

    # GAME STATE UPDATES
    cloud_x += 1
    if cloud_x - cloud_radius > WIDTH:
        cloud_x = - cloud_radius

    cloud_x += 1
    
# All game math and comparisons happen here

# DRAWING
    screen.fill((135, 206, 235))
#  Grass
    pygame.draw.rect(screen, green, [0, 400, 700, 100],0)
    # the sun
    pygame.draw.circle(screen, yellow, (circle_x, circle_y),      30)
    # mountain 
    pygame.draw.polygon (screen, grey, ([55, 398], [187, 126], [323, 399]), 0)
    # tree
    pygame.draw.polygon (screen, tree_green , ([365, 381], [435, 380], [402, 305]), 0)
    pygame.draw.polygon (screen, tree_green , ([0,380], [30, 320], [60, 380]), 0)
    pygame.draw.polygon (screen, tree_green , ([425,377], [493, 379], [451, 294]), 0)
    pygame.draw.rect(screen, brown, (25, 380, 10, 50))
    pygame.draw.rect(screen, brown, (400, 380, 10, 50))
    pygame.draw.rect(screen, brown, (450, 380, 10, 50))

    # shade
    pygame.draw.polygon (screen, shade, ([188, 129], [296, 399], [323, 401]), 0)               
    # clouds 




    draw_cloud(cloud_x + 348, cloud_y + 221 )
    draw_cloud(cloud_x + 93, cloud_y + 89 )
    draw_cloud(cloud_x + 550, cloud_y + 110 )







    
    # Must be the last two lines
    # of the game loop
    
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
