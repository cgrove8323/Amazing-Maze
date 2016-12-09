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

# Fonts
MY_FONT = pygame.font.Font(None, 50)

# Stages
START = 0
PLAYING = 1
END = 2

def setup():
    global block_pos, block_vel, size, stage

    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START

# Make a player
player =  [100, 0, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
wall1 = [75, 0, 25, 100]
wall2 = [25, 100, 150, 25]
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
wall14 = [100, 700, 25, 75]
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
wall112 = [25, 125, 25, 225]
wall113 = [25, 150, 125, 25]
wall114 = [125, 175, 25, 100]
wall115 = [125, 250, 125, 25]
wall116 = [0, 500, 75, 25]
wall117 = [0, 525, 25, 250]
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

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7,
         wall8, wall9, wall10, wall11,wall12, wall13, wall14, wall15, wall16,
         wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25,
         wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34,
         wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43,
         wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, 
         wall101, wall102, wall103, wall104, wall105,
         wall106, wall107, wall108, wall109, wall110, wall111,
         wall112, wall113, wall114, wall115, wall116, wall117, wall118, wall119,
         wall120, wall121, wall122, wall123, wall124, wall125, wall126, wall127,
         wall128, wall129, wall130, wall131, wall132, wall133, wall134, wall135,
         wall136, wall137, wall138, wall139, wall140, wall141, wall142, wall143,
         wall144, wall145, wall146, wall147, wall148, wall149, wall150, wall151,
         wall152, wall153, wall154, wall155, wall156]

# Make coins
coin1 = [325, 500, 25, 25]
coin2 = [400, 175, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
setup()
win = False
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

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''
    if player[0] < 0:
        player[0] = 0
    if player[0] + player[2] > WIDTH:
        player[0] = WIDTH - player[2]
    if player[1] < 0:
        player[1] = 0
    if player[1] + player[3] > HEIGHT:
        player[1] = HEIGHT - player[3]
    


    ''' get the coins '''
    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
   
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [500, 200])

    '''begin/end game text'''
    if stage == START:
        text1 = MY_FONT.render("THE AMAZING MAZE", True, WHITE)
        text2 = MY_FONT.render("Press ENTER to play!", True, WHITE)
        screen.blit(text1, [400, 400])
        screen.blit(text2, [400, 500])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("Press SPACE to restart.", True, WHITE)
        screen.blit(text1, [400, 400])
        screen.blit(text2, [400, 500])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
