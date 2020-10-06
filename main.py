import pygame
from message import display_message

pygame.init()

white = (255,255,255)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My first racing game')

# set the clock for the game (fps)
clock = pygame.time.Clock()

carImg = pygame.image.load('stupidCar2.png')
carImg_width = carImg.get_width()
carImg_height = carImg.get_height()
print(carImg_height)

def car(x,y):
    gameDisplay.blit(carImg,(x,y))




def game_loop():

    crashed = False
    x = display_width * 0.45
    y = display_height * 0.8

    x_change = 0
    vel = 7

    while not crashed:
        
        # pygame grabs events for us
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change = -5
            #     elif event.key == pygame.K_RIGHT:
            #         x_change = 5
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0
        
        keys_pressed = pygame.key.get_pressed()
        if(keys_pressed[pygame.K_LEFT] and x>0):
            x -= vel
        if(keys_pressed[pygame.K_RIGHT] and x<(display_width-carImg_width)):
            x += vel
        if(keys_pressed[pygame.K_UP] and y>0):
            y-=vel    
        if(keys_pressed[pygame.K_DOWN] and y<(display_height-carImg_height)):
            y += vel
        
        #x += x_change

        gameDisplay.fill(white)
        display_message('Hello world',gameDisplay,display_width,display_height)
        car(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
