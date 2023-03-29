import pygame
pygame.init()
screen = pygame.display.set_mode((700,500))
musiclist = [
    pygame.mixer.Sound("sounds/baribiled.mp3"),
    pygame.mixer.Sound("sounds/iwanna.mp3"),
    pygame.mixer.Sound("sounds/jaryq.mp3")
]

musnum = 0
rfalse = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if rfalse:
                musiclist[musnum].play()
            if not rfalse:
                musiclist[musnum].stop()
            rfalse = not rfalse    
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            musiclist[musnum].stop()
            musnum +=1
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            musnum -=1
    if musnum > len(musiclist)-1:
        musnum = 0
    if musnum < 0:
        musnum = len(musiclist)-1            