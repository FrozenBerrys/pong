import pygame, sys, math, random
from collections import deque

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('pong')
clock = pygame.time.Clock()

largefont = pygame.font.Font("pixel.ttf", 50)
font = pygame.font.Font("pixel.ttf", 35)
smallfont = pygame.font.Font("pixel.ttf", 20)
tinyfont = pygame.font.Font("pixel.ttf", 15)
#####################################################################################

welcome_surf = largefont.render("PONG!", False, 'White')
welcome_rect = welcome_surf.get_rect(center = (300, 100))
menu_surf = pygame.Surface((600,400))
menu_rect = menu_surf.get_rect(topleft = (0,0))
menudir = [1,1]
top = pygame.Rect(0, -10, 600, 10)
bottom = pygame.Rect(0, 400, 600, 10)
left = pygame.Rect(-10, 0, 10, 400)
right = pygame.Rect(600, 0, 10, 400)

score1int = 0
score2int = 0
score1 = font.render(str(score1int), False, "White")
score1_rect = score1.get_rect(topright = (276, 10))
score1.set_alpha(169)
score2 = font.render(str(score2int), False, "White")
score2_rect = score2.get_rect(topleft = (330, 10))
score2.set_alpha(169)
#####################################################################################

game_surf = pygame.Surface((600,400))
game_rect = game_surf.get_rect(topleft = (0,0))
pygame.Surface.fill(game_surf, "Black")
pygame.draw.line(game_surf, "White", (300,20), (300,380), 4)

play = font.render("1P", False, "Lime")
play_rect = play.get_rect(center = (300, 210))
play2 = font.render("2P", False, "Lime")
play_rect2 = play2.get_rect(center = (300, 265))
quitgame = font.render("QUIT", False, "Red")
quit_rect = quitgame.get_rect(center = (300, 320))

temp = pygame.Surface((200, 200))
pygame.Surface.fill(temp, "Black")
temp.set_alpha(150)
pygame.draw.line(temp, "White", (0,0), (200,0), 6)
pygame.draw.line(temp, "White", (0,0), (0,200), 6)
pygame.draw.line(temp, "White", (200,200), (200,0), 6)
pygame.draw.line(temp, "White", (200,200), (0,200), 6)
temp_rect = temp.get_rect(center = (300, 270))

#####################################################################################
pause_surface = pygame.Surface((600,400))
pause_text = largefont.render("GAME PAUSED", False, 'White')
pause_text_rect = pause_text.get_rect(center = (300,200))

def paused():
    global pause
    pause = True
    while pause:
        screen.blit(pause_text, pause_text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
        pygame.display.flip()
        clock.tick(10)  

def getdest(x, y, dir):
    left = 580 - x
    if dir == -1:
        left -= y
        if left < 0: return 0 - left - 25

        if left > 400: left -= 400 - y; return left - 25

        return left - 25
    else: 
        left -= 400 - y; 
        if left < 0: return 400 - 0 - left - 25

        if left > 400: left -= y; return left - 25

        return 400 - left - 25


def gameover(loser):
    global lose, time
    lose = True
    time = 0
    def roast():
        id = math.floor(random.randrange(10))
        if id == 0:
            id = " sucks at video games"
        if id == 1:
            id = ", GET PONGED BITCH!"
        if id == 2:
            id = " sucks at video games"
        if id == 3:
            id = " sucks at video games"
        if id == 4:
            id = " sucks at video games"
        if id == 5:
            id = " sucks at video games"
        if id == 6:
            id = " sucks at video games"
        if id == 7:
            id = " sucks at video games"
        if id == 8:
            id = " sucks at video games"
        if id == 9:
            id = " sucks at video games"
        return id
    
    gameover_surface = pygame.Surface((600,400))
    gameover_surface.set_alpha(60)
    gameover_text = smallfont.render(loser + roast() , False, 'Red')
    gameover_text_rect = gameover_text.get_rect(center = (300,200))
    while lose:
        screen.blit(gameover_surface, (0,0))
        screen.blit(gameover_text,gameover_text_rect)

        pygame.display.flip()
        clock.tick(5)  
        time += 1
        if time == 20:
            lose = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def color():
    id = math.floor(random.randrange(6))
    if id == 0:
        id = "Red"
    if id == 1:
        id = "Orange"
    if id == 2:
        id = "Yellow"
    if id == 3:
        id = "Green"
    if id == 4:
        id = "Blue"
    if id == 5:
        id = "Purple"
    return id

Menu = True; Singleplayer = False; Multiplayer = False

while True:
    while Menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(pos):

                    Singleplayer = True
                    Menu = False
                    initialize = 1
                    break
                if play_rect2.collidepoint(pos):
                    Multiplayer = True
                    Menu = False
                    initialize = 1
                    # INTIALIZE GAME            
                    break
                if quit_rect.collidepoint(pos):
                    pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(pos):
                    play = font.render("1P", False, "White")
                    screen.blit(play, play_rect)
                if play_rect2.collidepoint(pos):
                    play2 = font.render("2P", False, "White")
                    screen.blit(play2, play_rect2)
                if quit_rect.collidepoint(pos):
                    quitgame = font.render("QUIT", False, "White")
                    screen.blit(quitgame, quit_rect)
                if play_rect.collidepoint(pos) == False:
                    play = font.render("1P", False, "Lime")
                    screen.blit(play, play_rect)
                if play_rect2.collidepoint(pos) == False:
                    play2 = font.render("2P", False, "Lime")
                    screen.blit(play2, play_rect2)
                if quit_rect.collidepoint(pos) == False:
                    quitgame = font.render("QUIT", False, "Red")
                    screen.blit(quitgame, quit_rect)

        welcome_rect[0] += 5 * menudir[0]
        welcome_rect[1] += 5 * menudir[1]
        if welcome_rect.colliderect(top) or welcome_rect.colliderect(bottom):
            welcome_rect[1] -= 5 * menudir[1]
            menudir[1] = 0 - menudir[1]
            welcome_surf = largefont.render("PONG!", False, color())
        if welcome_rect.colliderect(right) or welcome_rect.colliderect(left):
            welcome_rect[1] -= 5 * menudir[1]
            menudir[0] = 0 - menudir[0]
            welcome_surf = largefont.render("PONG!", False, color())
        screen.blit(menu_surf, menu_rect)
        screen.blit(welcome_surf, welcome_rect)
        screen.blit(temp, temp_rect)
        screen.blit(play, play_rect)
        screen.blit(play2, play_rect2)
        screen.blit(quitgame, quit_rect)
        clock.tick(30)
        pygame.display.flip()


#####################################################################################

    while Singleplayer:
        if initialize:
            id = "White"
            menudir = [-1,-1]
            ball = pygame.Rect(300,200,20,20)
            racket1 = pygame.Rect(10,10,10,50)
            racket2 = pygame.Rect(580,10,10,50)
            initialize = 0
            score1int = 0
            score2int = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and racket1.colliderect(top) == False:
            racket1[1] -= 5
        if keys[pygame.K_s] and racket1.colliderect(bottom) == False:
            racket1[1] += 5

        ball[0] += 3 * menudir[0]
        ball[1] += 3 * menudir[1]


#CHECKING FOR BOUND COLLISIONS
        if ball.colliderect(top) or ball.colliderect(bottom):
            ball[1] -= 3 * menudir[1]
            menudir[1] = 0 - menudir[1]
            id = color()
        if ball.colliderect(left):
            ball = pygame.Rect(300,200,20,20)
            score2int += 1
            if racket2[1] > 200:
                menudir = [1,1]
            else:
                menudir = [1,-1]
            Bob = getdest(ball[0], ball[1], menudir[1])
        if ball.colliderect(right):
            ball = pygame.Rect(300,200,20,20)
            score1int += 1
            if racket1[1] > 200:
                menudir = [-1,1]
            else:
                menudir = [-1,-1]

#CHECKING FOR RACKET BALL COLLISIONS
        if ball.colliderect(racket1):
            if ball[0]-20 > racket1[0] or ball[0] > racket1[0]-50:
                ball[0] -= 6 * menudir[0]
                menudir[0] = 0 - menudir[0]
            #ball[1] -= 6 * menudir[1]
            #menudir[1] = 0 - menudir[1]
            Bob = getdest(ball[0], ball[1], menudir[1])
        
        if ball.colliderect(racket2):
            if ball[0]-20 > racket2[0] or ball[0] > racket2[0]-50:
                ball[0] -= 6 * menudir[0]
                menudir[0] = 0 - menudir[0]
            #ball[1] -= 6 * menudir[1]
            #menudir[1] = 0 - menudir[1]
  
#AI MOVING TOWARDS DESIGNATED POSITION

        if menudir[0] == 1 and racket2[1] != Bob: #WTF?
            if Bob > racket2[1]:
                racket2[1] += 3
            else: racket2[1] -= 3

        score1 = font.render(str(score1int), False, id)
        score2 = font.render(str(score2int), False, id)
        screen.blit(game_surf, game_rect)
        pygame.draw.line(game_surf, id, (300,20), (300,380), 4)
        pygame.draw.rect(screen, id, racket1)
        pygame.draw.rect(screen, id, racket2)
        pygame.draw.rect(screen, id, ball)
        screen.blit(score1, score1_rect)
        screen.blit(score2, score2_rect)

#LOSE WIN CONDITION
        if score1int > 9:
            gameover("Bob "); Singleplayer = False; Menu = True
        if score2int > 9: 
            gameover("Player 1 "); Singleplayer = False; Menu = True

        clock.tick(120)
        pygame.display.flip()

#####################################################################################

    while Multiplayer:
        if initialize:
            id = "White"
            menudir = [-1,-1]
            ball = pygame.Rect(300,200,20,20)
            racket1 = pygame.Rect(10,10,10,50)
            racket2 = pygame.Rect(580,10,10,50)
            initialize = 0
            score1int = 0
            score2int = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and racket2.colliderect(top) == False:
            racket2[1] -= 5
        if keys[pygame.K_DOWN] and racket2.colliderect(bottom) == False:
            racket2[1] += 5
        if keys[pygame.K_s] and racket1.colliderect(bottom) == False:
            racket1[1] += 5
        if keys[pygame.K_w] and racket1.colliderect(top) == False:
            racket1[1] -= 5
        
        ball[0] += 3 * menudir[0]
        ball[1] += 3 * menudir[1]


#CHECKING FOR BOUND COLLISIONS
        if ball.colliderect(top) or ball.colliderect(bottom):
            ball[1] -= 3 * menudir[1]
            menudir[1] = 0 - menudir[1]
            id = color()
        if ball.colliderect(left):
            ball = pygame.Rect(300,200,20,20)
            score2int += 1
            if racket2[1] > 200:
                menudir = [1,1]
            else:
                menudir = [1,-1]
        if ball.colliderect(right):
            ball = pygame.Rect(300,200,20,20)
            score1int += 1
            #damage control
            print(racket2[1])
            print(Bob)
            if racket1[1] > 200:
                menudir = [-1,1]
            else:
                menudir = [-1,-1]

#CHECKING FOR RACKET BALL COLLISIONS
        if ball.colliderect(racket1):
            if ball[0]-20 > racket1[0] or ball[0] > racket1[0]-50:
                ball[0] -= 6 * menudir[0]
                menudir[0] = 0 - menudir[0]
            #ball[1] -= 6 * menudir[1]
            #menudir[1] = 0 - menudir[1]
        
        if ball.colliderect(racket2):
            if ball[0]-20 > racket2[0] or ball[0] > racket2[0]-50:
                ball[0] -= 6 * menudir[0]
                menudir[0] = 0 - menudir[0]
            #ball[1] -= 6 * menudir[1]
            #menudir[1] = 0 - menudir[1]
        
        score1 = font.render(str(score1int), False, id)
        score2 = font.render(str(score2int), False, id)
        screen.blit(game_surf, game_rect)
        pygame.draw.line(game_surf, id, (300,20), (300,380), 4)
        pygame.draw.rect(screen, id, racket1)
        pygame.draw.rect(screen, id, racket2)
        pygame.draw.rect(screen, id, ball)
        screen.blit(score1, score1_rect)
        screen.blit(score2, score2_rect)

#LOSE WIN CONDITION
        if score1int > 9:
            gameover("Player 2 "); Multiplayer = False; Menu = True
        if score2int > 9: 
            gameover("Player 1 "); Multiplayer = False; Menu = True

        clock.tick(120)
        pygame.display.flip()
