import pygame
import datetime
pygame.init()

WIDTH=1080
HEIGHT=720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.image.load("images/main-clock.png").convert()
scale_clock = pygame.transform.scale(
    clock, (clock.get_width() // 2,
              clock.get_height() // 2))
clockr=scale_clock.get_rect(center=(WIDTH/2, HEIGHT/2))

second=pygame.image.load("images/left-hand.png").convert_alpha()
scale_second=pygame.transform.scale(
    second, (second.get_width() // 2,
               second.get_height() // 2))

minute=pygame.image.load("images/right-hand.png").convert_alpha()
scale_minute=pygame.transform.scale(
    minute, (minute.get_width() // 2,
               minute.get_height() // 2))

done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255,255,255))
        screen.blit(scale_clock, clockr)
        t=datetime.datetime.now()
        minutes, seconds=t.minute, t.second
        rots = pygame.transform.rotate(scale_second, (-6*seconds)+90)
        rots_rect = rots.get_rect(center=(540, 360))
        screen.blit(rots, rots_rect)
        rotm = pygame.transform.rotate(scale_minute, (-6*minutes)+90) #(-6*minutes-0.1*seconds)+90
        rotm_rect = rotm.get_rect(center=(540, 360))
        screen.blit(rotm, rotm_rect)
        pygame.display.update()