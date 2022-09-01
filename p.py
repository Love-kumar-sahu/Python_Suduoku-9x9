import pygame


pygame.init()
win = pygame.display.set_mode((200,75))
pygame.display.set_caption('example')
s = pygame.Color(0,0,0)
FONT = pygame.font.Font(None, 32)
win.blit(FONT.render('not',True,s),(200,75))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
