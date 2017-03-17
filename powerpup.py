import pygame, sys, random, math
import player, ball
from enemygroup import EnemyGroup

pygame.init()

W = 1280
H = 720
screen = pygame.display.set_mode((W,H),pygame.FULLSCREEN)

font = pygame.font.Font(None, 24)
            
clock = pygame.time.Clock()

mainLoop = True
while mainLoop:
    enemies = EnemyGroup((W,H))
    enemies.make_enemies(20,1,10)
    p1 = player.Player(50, 50, 8, 8, (100,200,255))
    
    playing = True
    level = 1
    
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    p1.shoot()

        #Draw background
        screen.fill((0,0,0))
        
        #Draw score
        screen.blit(font.render("Level: "+str(level),1,(255,255,255)),(10,10))
        screen.blit(font.render("Health: "+str(p1.health),1,(255,255,255)),(10,30))
        
        #Draw player to screen
        p1.draw(screen)
        
        #Draw goal line
        pygame.draw.line(screen, (255,255,100),(W-5,0),(W-5,H-5),10)

        #Draw all enemies to screen
        enemies.draw(screen)

        #move player
        p1.move()

        #Check for win and begin new level
        if p1.x > W:
            level+=1
            enemies.make_enemies(20+level,1,10+level) #bad guy list, 20 in level 1
            p1 = player.Player(50, 50, 8, 8, (100,200,255))

        if p1.health <= 0:
            pygame.quit()
            sys.exit()
            
        #Move enemies, also checks for collision with player
        enemies.move(p1)

        
        pygame.display.flip()
        clock.tick(30)
