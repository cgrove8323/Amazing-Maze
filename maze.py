# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (31, 94, 196)

# Fonts
MY_FONT = pygame.font.Font(None, 50)

# Stages
START = 0
PLAYING = 1
END = 2

def setup():
    global score, coins, win, lose, stage, player, player_vx, player_vy, player_speed, badguy, badguy_vx, badguy_vy, badguy_speed 

    stage = START
    win = False
    lose = False
    score = 0

    # Make a player
    player =  [525, 425, 25, 25]
    player_vx = 0
    player_vy = 0
    player_speed = 5

    # Make a Bad Guy
    badguy = [100, 0, 25, 25]
    badguy_vx = 0
    badguy_vy = 0
    badguy_speed = 5

    # Make coins
    coin1 = [500, 50, 25, 25]
    coin2 = [500, 125, 25, 25]
    coin3 = [350, 225, 25, 25]
    coin4 = [550, 225, 25, 25]
    coin5 = [650, 175, 25, 25]
    coin6 = [550, 375, 25, 25]
    coin7 = [375, 475, 25, 25]
    coin8 = [425, 625, 25, 25]
    coin9 = [525, 525, 25, 25]
    coin10 = [525, 750, 25, 25]
    coin11 = [600, 625, 25, 25]
    coin12 = [625, 725, 25, 25]
    coin13 = [625, 425, 25, 25]
    coin14 = [700, 350, 25, 25]
    coin15 = [700, 475, 25, 25]
    coin16 = [700, 575, 25, 25]
    coin17 = [700, 750, 25, 25]
    coin18 = [800, 475, 25, 25]
    coin19 = [825, 600, 25, 25]
    coin20 = [850, 75, 25, 25]
    coin21 = [850, 200, 25, 25]
    coin22 = [850, 300, 25, 25]
    coin23 = [900, 725, 25, 25]
    coin24 = [975, 275, 25, 25]
    coin25 = [975, 525, 25, 25]
    coin26 = [975, 750, 25, 25]
    coin27 = [1025, 150, 25, 25]
    coin28 = [1050, 25, 25, 25]
    coin29 = [1075, 225, 25, 25]
    coin30 = [1075, 575, 25, 25]
    coin31 = [1125, 450, 25, 25]
    coin32 = [1150, 725, 25, 25]
    coin33 = [100, 275, 25, 25]
    coin34 = [100, 525, 25, 25]
    coin35 = [200, 525, 25, 25]
    coin36 = [250, 125, 25, 25]
    coin37 = [125, 750, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9,
             coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17,
             coin18, coin19, coin20, coin21, coin22, coin23, coin24, coin25,
             coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33,
             coin34, coin35, coin36, coin37]

# make walls
wall1 = [75, 0, 25, 100]
wall2 = [0, 100, 175, 25]
wall3 = [175, 100, 25, 100]
wall4 = [175, 200, 100, 25]
wall5 = [275, 200, 25, 100]
wall6 = [200, 300, 100, 25]
wall7 = [175, 300, 25, 100]
wall8 = [175, 400, 100, 25]
wall9 = [250, 425, 25, 25]
wall10 = [125, 450, 150, 25]
wall11 = [125, 300, 25, 125]
wall12 = [75, 300, 50, 25]
wall13 = [75, 200, 25, 100]
wall14 = [100, 700, 25, 100]
wall15 = [75, 700, 25, 25]
wall16 = [50, 625, 25, 100]
wall17 = [50, 600, 50, 25]
wall18 = [175, 550, 25, 75]
wall19 = [175, 600, 50, 25]
wall20 = [200, 550, 150, 25]
wall21 = [350, 400, 25, 125]
wall22 = [375, 500, 25, 100]
wall23 = [350, 600, 75, 25]
wall24 = [400, 650, 25, 75]
wall25 = [350, 700, 50, 25]
wall26 = [350, 725, 25, 75]
wall27 = [375, 750, 150, 25]
wall28 = [500, 775, 25, 25]
wall29 = [400, 400, 25, 75]
wall30 = [425, 450, 25, 125]
wall31 = [450, 550, 25, 175]
wall32 = [475, 700, 100, 25]
wall33 = [550, 725, 25, 75]
wall34 = [575, 750, 100, 25]
wall35 = [675, 650, 25, 150]
wall36 = [700, 650, 50, 25]
wall37 = [725, 550, 25, 100]
wall38 = [375, 250, 25, 125]
wall39 = [400, 250, 100, 25]
wall40 = [500, 250, 25, 75]
wall41 = [425, 300, 75, 25]
wall42 = [400, 350, 125, 25]
wall43 = [400, 0, 25, 75]
wall44 = [425, 0, 25, 25]
wall45 = [425, 50, 25, 25]
wall46 = [325, 100, 125, 25]
wall47 = [475, 0, 25, 125]
wall48 = [500, 0, 175, 25]
wall49 = [500, 100, 150, 25]
wall50 = [650, 50, 25, 75]
wall51 = [525, 50, 125, 25]
wall52 = [700, 0, 25, 125]
wall53 = [725, 0, 325, 25]
wall54 = [1025, 25, 25, 50]
wall55 = [725, 50, 125, 25]
wall56 = [825, 75, 25, 50]
wall57 = [725, 100, 25, 75]
wall58 = [775, 100, 25, 50]
wall59 = [800, 125, 75, 25]
wall60 = [725, 175, 200, 25]
wall61 = [875, 50, 175, 25]
wall62 = [900, 100, 25, 75]
wall63 = [725, 700, 25, 100]
wall64 = [750, 750, 225, 25]
wall65 = [950, 775, 25, 25]
wall66 = [1075, 0, 100, 25]
wall67 = [1175, 0, 25, 100]
wall68 = [1075, 50, 75, 25]
wall69 = [1175, 125, 25, 250]
wall70 = [1000, 300, 175, 25]
wall71 = [1000, 325, 25, 25]
wall72 = [1150, 350, 25, 200]
wall73 = [1175, 525, 25, 25]
wall74 = [1050, 525, 25, 75]
wall75 = [1075, 525, 50, 25]
wall76 = [1100, 550, 25, 50]
wall77 = [1125, 575, 75, 25]
wall78 = [1150, 625, 25, 100]
wall79 = [1175, 625, 25, 25]
wall80 = [1175, 700, 25, 25]
wall81 = [1000, 750, 200, 25]
wall82 = [1000, 775, 25, 25]
wall83 = [350, 50, 25, 50]
wall84 = [150, 0, 250, 25]
wall85 = [275, 50, 75, 25]
wall86 = [275, 75, 25, 50]

wall101 = [125, 0, 25, 75]
wall102 = [150, 50, 100, 25]
wall103 = [225, 75, 25, 100]
wall104 = [250, 150, 200, 25]
wall105 = [325, 200, 25, 150]
wall106 = [225, 350, 125, 25]
wall107 = [350, 200, 100, 25]
wall108 = [300, 400, 25, 125]
wall109 = [125, 500, 175, 25]
wall110 = [75, 350, 25, 175]
wall111 = [25, 350, 50, 25]
wall112 = [25, 175, 25, 175]
wall113 = [0, 150, 150, 25]
wall114 = [125, 175, 25, 100]
wall115 = [125, 250, 125, 25]
wall116 = [0, 500, 75, 25]
wall117 = [0, 550, 25, 225]
wall118 = [25, 750, 100, 25]
wall119 = [50, 550, 50, 25]
wall120 = [125, 500, 25, 150]
wall121 = [100, 650, 75, 25]
wall122 = [200, 600, 25, 100]
wall123 = [150, 700, 125, 25]
wall124 = [150, 750, 125, 25]
wall125 = [300, 675, 25, 125]
wall126 = [250, 600, 75, 25]
wall127 = [250, 650, 150, 25]
wall128 = [275, 575, 25, 25]
wall129 = [450, 400, 100, 25]
wall130 = [475, 450, 150, 25]
wall131 = [475, 500, 50, 25]
wall132 = [525, 475, 25, 50]
wall133 = [575, 475, 25, 75]
wall134 = [550, 550, 150, 25]
wall135 = [625, 575, 25, 25]
wall136 = [550, 600, 150, 25]
wall137 = [500, 550, 25, 100]
wall138 = [500, 650, 100, 25]
wall139 = [625, 650, 25, 75]
wall140 = [600, 700, 25, 25]
wall141 = [475, 150, 25, 75]
wall142 = [525, 150, 25, 75]
wall143 = [550, 150, 50, 25]
wall144 = [575, 175, 25, 50]
wall145 = [600, 200, 50, 25]
wall146 = [625, 150, 25, 50]
wall147 = [675, 150, 25, 75]
wall148 = [550, 250, 25, 125]
wall149 = [575, 350, 25, 75]
wall150 = [600, 250, 75, 25]
wall151 = [600, 300, 25, 25]
wall152 = [625, 300, 25, 125]
wall153 = [650, 350, 50, 25]
wall154 = [650, 400, 50, 25]
wall155 = [650, 425, 25, 75]
wall156 = [625, 500, 125, 25]
wall157 = [700, 275, 25, 25]
wall158 = [700, 250, 50, 25]
wall159 = [725, 225, 175, 25]
wall160 = [900, 225, 25, 125]
wall161 = [775, 275, 100, 25]
wall162 = [675, 300, 125, 25]
wall163 = [825, 325, 75, 25]
wall164 = [800, 350, 25, 75]
wall165 = [725, 350, 75, 25]
wall166 = [725, 375, 25, 100]
wall167 = [700, 450, 25, 25]
wall168 = [775, 400, 25, 150]
wall169 = [950, 100, 25, 175]
wall170 = [975, 250, 175, 25]
wall171 = [1000, 100, 125, 25]
wall172 = [1000, 125, 25, 100]
wall173 = [1025, 200, 125, 25]
wall174 = [1125, 100, 25, 50]
wall175 = [1050, 150, 100, 25]
wall176 = [950, 300, 25, 75]
wall177 = [925, 375, 75, 25]
wall178 = [900, 375, 25, 75]
wall179 = [1000, 375, 25, 50]
wall180 = [850, 375, 25, 75]
wall181 = [825, 450, 100, 25]
wall182 = [1050, 350, 25, 75]
wall183 = [1100, 350, 25, 75]
wall184 = [975, 425, 150, 25]
wall185 = [950, 425, 25, 75]
wall186 = [850, 500, 125, 25]
wall187 = [825, 500, 25, 75]
wall188 = [775, 575, 75, 25]
wall189 = [775, 600, 25, 125]
wall190 = [800, 700, 100, 25]
wall191 = [825, 625, 25, 75]
wall192 = [875, 600, 25, 100]
wall193 = [875, 550, 75, 25]
wall194 = [925, 575, 25, 75]
wall195 = [975, 550, 25, 125]
wall196 = [1000, 475, 25, 100]
wall197 = [1025, 475, 100, 25]
wall198 = [925, 675, 25, 50]
wall199 = [950, 700, 150, 25]
wall200 = [1100, 675, 25, 50]
wall201 = [1025, 625, 25, 75]
wall202 = [1050, 625, 75, 25]
wall203 = [150, 750, 25, 50]
wall204 = [250, 750, 25, 50]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7,
         wall8, wall9, wall10, wall11,wall12, wall13, wall14, wall15, wall16,
         wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25,
         wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34,
         wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43,
         wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52,
         wall53, wall54, wall55, wall56, wall57, wall58, wall59, wall60, wall61,
         wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70,
         wall71, wall72, wall73, wall74, wall75, wall76, wall77, wall78, wall79,
         wall80, wall81, wall82, wall83, wall84, wall85, wall86, 
         wall101, wall102, wall103, wall104, wall105,
         wall106, wall107, wall108, wall109, wall110, wall111,
         wall112, wall113, wall114, wall115, wall116, wall117, wall118, wall119,
         wall120, wall121, wall122, wall123, wall124, wall125, wall126, wall127,
         wall128, wall129, wall130, wall131, wall132, wall133, wall134, wall135,
         wall136, wall137, wall138, wall139, wall140, wall141, wall142, wall143,
         wall144, wall145, wall146, wall147, wall148, wall149, wall150, wall151,
         wall152, wall153, wall154, wall155, wall156, wall157, wall158, wall159,
         wall160, wall161, wall162, wall163, wall164, wall165, wall166, wall167,
         wall168, wall169, wall170, wall171, wall172, wall173, wall174, wall175,
         wall176, wall177, wall178, wall179, wall180, wall181, wall182, wall183,
         wall184, wall185, wall186, wall187, wall188, wall189, wall190, wall191,
         wall192, wall193, wall194, wall195, wall196, wall197, wall198, wall199,
         wall200, wall201, wall202, wall203, wall204]



# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_RETURN:
                    stage = PLAYING
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    if stage == PLAYING:

        pressed = pygame.key.get_pressed()

        player_up = pressed[pygame.K_UP]
        player_down = pressed[pygame.K_DOWN]
        player_left = pressed[pygame.K_LEFT]
        player_right = pressed[pygame.K_RIGHT]

        badguy_up = pressed[pygame.K_w]
        badguy_down = pressed[pygame.K_s]
        badguy_left = pressed[pygame.K_a]
        badguy_right = pressed[pygame.K_d]

        if player_up:
            player_vy = -player_speed
        elif player_down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if player_left:
            player_vx = -player_speed
        elif player_right:
            player_vx = player_speed
        else:
            player_vx = 0

        if badguy_up:
            badguy_vy = -badguy_speed
        elif badguy_down:
            badguy_vy = badguy_speed
        else:
            badguy_vy = 0

        if badguy_left:
            badguy_vx = -badguy_speed
        elif badguy_right:
            badguy_vx = badguy_speed
        else:
            badguy_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx
        badguy[0] += badguy_vx
        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

        for w in walls:
            if intersects.rect_rect(badguy, w):
                if badguy_vx > 0:
                    badguy[0] = w[0] - badguy[2]
                elif badguy_vx < 0:
                    badguy[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        badguy[1] += badguy_vy
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

        for w in walls:
            if intersects.rect_rect(badguy, w):                    
                if badguy_vy > 0:
                    badguy[1] = w[1] - badguy[3]
                if badguy_vy < 0:
                    badguy[1] = w[1] + w[3]

        if intersects.rect_rect(player, badguy):
            stage = END
            lose = True


    ''' here is where you should resolve player collisions with screen edges '''
    '''if player[0] < 0:
        player[0] = 0
    if player[0] + player[2] > WIDTH:
        player[0] = WIDTH - player[2]
    if player[1] < 0:
        player[1] = 0
    if player[1] + player[3] > HEIGHT:
        player[1] = HEIGHT - player[3]'''

    if badguy[0] < 0:
        badguy[0] = 0
    if badguy[0] + badguy[2] > WIDTH:
        badguy[0] = WIDTH - badguy[2]
    if badguy[1] < 0:
        badguy[1] = 0
    if badguy[1] + badguy[3] > HEIGHT:
        badguy[1] = HEIGHT - badguy[3]
    
    if player[0] == 1200 and player[2] == 100:
        player[0] = 125
        player[1] = 800

    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]

    for hit in hit_list:
        coins.remove(hit)
        score += 1
        
    if len(hit_list) == len(coins) + 1:
        stage = END
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, BLUE, badguy)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
   

    '''begin/end game text'''
    if stage == START:
        text1 = MY_FONT.render("THE AMAZING MAZE", True, WHITE)
        text2 = MY_FONT.render("Press ENTER to play!", True, WHITE)
        screen.blit(text1, [400, 400])
        screen.blit(text2, [400, 500])
    if stage == PLAYING:
        font = pygame.font.Font(None, 30)
        text1 = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text1, [1050, 775])
    if stage == END:
        text1 = MY_FONT.render("Press SPACE to restart.", True, WHITE)
        screen.blit(text1, [400, 500])     
        if win:
            player_speed = 0
            badguy_speed = 0
            font = pygame.font.Font(None, 48)
            text = font.render("YOU WIN!", 1, GREEN)
            screen.blit(text, [500, 200])
        if lose:
            font = pygame.font.Font(None, 48)
            text = font.render("YOU LOSE", 1, GREEN)
            screen.blit(text, [500, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
