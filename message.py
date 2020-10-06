import pygame


def display_message(text,gameDisplay,display_width,display_height):
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render('Start the game',True,(0,0,255))
    textRect = text.get_rect()
    textRect.center = (display_width//2,display_height//2)
    gameDisplay.blit(text,textRect)

