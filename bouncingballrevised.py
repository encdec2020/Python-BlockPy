import pygame
import time
pygame.init()
# set up the drawing window
screen = pygame.display.set_mode((500, 300))
y = 0
x = 0
running = True
increment = 1
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
    else:
        while y <= 300:
            screen.fill((255, 255, 0))
            # draw a circle of colour (red=255,0,0 and x =255,y =0,1,.. radius=13,thickness=0
            pygame.draw.circle(screen, (255, 0, 0), (250, y), 13, 0)
            pygame.display.update()
            # increment y to move ahead
            y = y + increment
            # add sleep to reduce speed of ball
            time.sleep(0.006)
            # when y hits border decrement
            if y == 300:
                increment = -1
                break
            # else increment
            elif y == 0:
                increment = 1
                break
        else:
            y = y + increment
            break
    pygame.display.flip()
pygame.quit()




