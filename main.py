import pygame
import sys
import random
from pygame.locals import*
pygame.init()
screen_info=pygame.display.info()
size=(width, height)=(int(screen_info),int(screen_info,current_h))
screen=pygame.display.set_mode(size)
clock=pygame.time.clock()

blue = (0,127,255)
fish_image=pygame.image.load("fish")
fish_image=pygame.transform.smoothscale(fish_image(80,80))
fish_rect=fish_image.get_rect()peed
fish_rect.center=(width//2, height//2)
speed=pygame.math.vector2(0,10)
rotation=random.randit(0,350)
speed.rotate.ip(rotation)
fish_image=pygame.transform.rotate(fish_image,180-rotation)


def move_fish():
    global fish_image
    screen_info = pygame.display.Info()
    fish_rect.move_ip(speed)
    if fish_rect.left < 0 or fish_rect > screen_info.current_w:
        speed[0] '= -1
        fish_image = pygame.transform.flip(fish_image,True, False)
        fish_rect.move_ip(speed[0], 0)
     if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
        speed[1] *= -1
        fish_image = pygame.transform.flip(fish_image, False, True)
        fish_rect.move_ip(0, speed[1])
        
                
def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
         move_fish()
        screen.fill(blue)
        screen.blit(fish_image, fish_rect)
 pygame.display.flip()


if __name__== '__main__':
    main()
