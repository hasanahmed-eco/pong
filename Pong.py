import pygame
from Paddle import Paddle
from Ball import Ball
import random as rand
from Bubble import Bubble

clock = pygame.time.Clock()

# Open a window
size = (700,500)
width = 700
height = 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Define some colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

def startScreen():
    
    intro = True
    bubble_sprites_list = pygame.sprite.Group()
    for i in range(0,50):
        bubble_sprites_list.add(Bubble(WHITE,5,[rand.randint(width/4,3*width/4),rand.randint(height/4,3*height/4)],width,height))

    while(intro):
        screen.fill(BLACK)
        
        font = pygame.font.Font(None, 100)
        text = font.render("PONG", 1, WHITE)
        screen.blit(text,(250,10))
        

        pygame.draw.rect(screen,BLACK,(225,150,250,50))       
        pygame.draw.rect(screen,BLACK,(225,250,250,50))
        pygame.draw.rect(screen,BLACK,(225,350,250,50))

        # Draw the rectangles which will hold the game options
        font = pygame.font.Font(None, 35)
        text = font.render("Player vs Computer", 1, WHITE)
        screen.blit(text,(235,175,250,50))
        
        # Draw the rectangles which will hold the game options
        font = pygame.font.Font(None, 35)
        text = font.render("Player vs Player", 1, WHITE)
        screen.blit(text,(250,264,250,50))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
        
                if(475>mouse_pos[0]>225 and 200>mouse_pos[1]>150):
                    isHumanPlaying = False
                    isComputerPlaying = True
            
                if(475>mouse_pos[0]>225 and 300>mouse_pos[1]>250):
                    isHumanPlaying = True
                    isComputerPlaying = False
                    
                gameloop(isHumanPlaying,isComputerPlaying)
                break
        
        bubble_sprites_list.update()
    
        bubble_sprites_list.draw(screen)
    
        pygame.display.flip()

        clock.tick(15)

def gameloop(isHumanPlaying,isComputerPlaying):
    
    height = 100
    PaddleA = Paddle(WHITE,10,height)
    PaddleB = Paddle(WHITE,10,height)
    
    PaddleA.rect.x = 20
    PaddleA.rect.y = 200
    
    PaddleB.rect.x = 670
    PaddleB.rect.y = 200
    
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195
    
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(PaddleA)
    all_sprites_list.add(PaddleB)
    all_sprites_list.add(ball)
    
    scoreA = 0
    scoreB = 0
    multiplierA = 0
    multiplierB = 0
    
    carryOn = True
    
    #---- MAIN PROGRAM LOOP ----
    while carryOn:
        frame_count = 0
        # ---- MAIN EVENT LOOP ----
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Exit the loop
    
        # ---- GAME LOGIC ------------------
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            PaddleA.moveUp(5)
        if keys[pygame.K_s]:
            PaddleA.moveDown(5) 
            
        if keys[pygame.K_UP]:
            if(isHumanPlaying):
                PaddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            if(isHumanPlaying):
                PaddleB.moveDown(5)
          
        if(isComputerPlaying):  
            if(ball.rect.y > PaddleB.rect.y + 1/2*height):
                PaddleB.moveDown(rand.randint(0,7))
            if(ball.rect.y < PaddleB.rect.y + 1/2*height):
                PaddleB.moveUp(rand.randint(0,7))
        
        all_sprites_list.update()
    
        if ball.rect.x>=690:
            multiplierA += 1
            multiplierB = 0
            
            if(multiplierA <= 3):
                scoreA += 1
            elif(5 > multiplierA > 3):
                scoreA += 2
            else:
                scoreA += 5
            
            ball.reset()
            ball.velocity[0] = -ball.velocity[0]
            
        if ball.rect.x<=0:
            multiplierB += 1
            multiplierA = 0
            
            if(multiplierB <= 3):
                scoreB += 1
            elif(5 > multiplierB > 3):
                scoreB += 2
            else:
                scoreB += 5
                
            ball.reset()
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]
    
        if pygame.sprite.collide_mask(ball,PaddleA) or pygame.sprite.collide_mask(ball,PaddleB):
            ball.bounce()
    
        # ---- DRAWING THE CODE ------------
        screen.fill(BLACK)
        pygame.draw.line(screen,WHITE,[349,0],[349,500],5)
        all_sprites_list.draw(screen)
    
        if(multiplierA <= 3):
            colorA = WHITE
        elif(5>multiplierA>3):
            colorA = YELLOW
        elif(multiplierA >=5):
            colorA = RED 
            
        if(multiplierB <= 3):
            colorB = WHITE
        elif(5>multiplierB>3):
            colorB = YELLOW
        elif(multiplierB >=5):
            colorB = RED 
        
    
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, colorA)
        screen.blit(text,(250,10))
        text = font.render(str(scoreB), 1, colorB)
        screen.blit(text,(420,10))
    
        # Update the screen with what we have drawn
        pygame.display.flip()
    
        if(frame_count == 60):
            frame_count = 0
        else:
            frame_count += 1
    
        # Limit to 60 frames per second
        clock.tick(60)
    pygame.quit()
    
pygame.init()
startScreen()
