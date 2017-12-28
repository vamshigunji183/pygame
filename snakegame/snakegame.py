import pygame
import time
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

block_size = 10

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SnakeGame')
clock = pygame.time.Clock()


def food(foodx, foody, foodw, foodh, color):
    pygame.draw.rect(gameDisplay, color, [foodx, foody, foodw, foodh])



def snakes(block_size,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1],block_size,block_size])



def game_loop():
    snake_startx = 400
    snake_starty = 300



    food_startx = round(random.randrange(0, display_width)/10.0)
    food_starty = round(random.randrange(0, display_height)/10.0)

    food_width = 10
    food_height = 10
    gameExit=False
    x_change=0
    y_change=0

    snakeList = []
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-1
                    y_change=0
                if event.key==pygame.K_RIGHT:
                    x_change= 1
                    y_change = 0
                if event.key==pygame.K_UP:
                    y_change= -1
                    x_change = 0
                if event.key==pygame.K_DOWN:
                    y_change= 1
                    x_change = 0

            '''if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change=0
                if event.key == pygame.K_RIGHT:
                    x_change=0
                if event.key == pygame.K_UP:
                    y_change=0
                if event.key == pygame.K_DOWN:
                    y_change=0'''

        snake_startx+=x_change
        snake_starty += y_change

        gameDisplay.fill(white)

        food(food_startx, food_starty, food_width, food_height, red)


        snakeHead=[]
        snakeHead.append(snake_startx)
        snakeHead.append(snake_starty)
        snakeList.append(snakeHead)
        snakes(block_size, snakeList)

        distance=((snake_startx-food_startx)**2+(snake_starty-food_starty)**2)**0.5
        if(distance<10):
            print("ate")
            food_startx = round(random.randrange(0, display_width))
            food_starty = round(random.randrange(0, display_height))




        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()