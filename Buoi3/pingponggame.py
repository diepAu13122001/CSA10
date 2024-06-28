import pygame

# khai bao cua so tro choi
pygame.init()
pygame.display.set_caption("Ping Pongggggggg")
SIZE = (600, 600)
canvas = pygame.display.set_mode(SIZE)
BG_COLOR = (252, 16, 140)
clock = pygame.time.Clock()

# chen tai nguyen
ball_img = pygame.image.load("Buoi13/assets/ball.png")
paddle_img = pygame.image.load("Buoi13/assets/paddle.png")

# setup toa do
paddle_1_x = 0
paddle_1_y = 250
paddle_2_x = 570
paddle_2_y = 250
ball_x = 285
ball_y = 300
# setup bien danh cho nut bam
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
# speed
speed_x = 1.5
speed_y = 3.5

loop = True
while loop: # play game
    events = pygame.event.get() # bat su kien
    for e in events:
        # quit
        if e.type == pygame.QUIT:
            loop = False
        # keyboard check
        elif e.type == pygame.KEYDOWN:  # nhan phim
            if e.key == pygame.K_w:
                w_pressed = True
            elif e.key == pygame.K_s:
                s_pressed = True
            elif e.key == pygame.K_UP:
                up_pressed = True
            elif e.key == pygame.K_DOWN:
                down_pressed = True

        elif e.type == pygame.KEYUP:  # khong nhan phim
            if e.key == pygame.K_w:
                w_pressed = False
            elif e.key == pygame.K_s:
                s_pressed = False
            elif e.key == pygame.K_UP:
                up_pressed = False
            elif e.key == pygame.K_DOWN:
                down_pressed = False

    # Ball movement
    ball_x += speed_x
    ball_y += speed_y

    # Check collision with paddles and edges
    # >< paddles
    if ball_x <= (paddle_1_x + 30) and paddle_1_y <= ball_y <= (paddle_1_y + 120): 
        speed_x = -speed_x
    if ball_x <= (paddle_2_x - 30) and paddle_2_y <= ball_y <= (paddle_2_y + 120): 
        speed_x = -speed_x
    # >< edges
    if ball_x <= 0 or ball_x >= 570:
        speed_x = -speed_x
    if ball_y <= 0 or ball_y >= 570:
        speed_y = -speed_y
    
    # paddles >< edges => paddles stop
    if paddle_1_y <= 0:
        w_pressed = False
    if paddle_2_y <= 0:
        up_pressed = False
    if paddle_1_y >= 480:
        s_pressed = False
    if paddle_2_y >= 480:
        down_pressed = False

    # paddles movement
    if w_pressed:
        paddle_1_y -= 5
    elif s_pressed: 
        paddle_1_y += 5
    elif up_pressed:
        paddle_2_y -= 5
    elif down_pressed:
        paddle_2_y += 5

    canvas.fill(BG_COLOR)
    canvas.blit(ball_img, (ball_x, ball_y))
    canvas.blit(paddle_img, (paddle_1_x, paddle_1_y))
    canvas.blit(paddle_img, (paddle_2_x, paddle_2_y))
    clock.tick(60)
    pygame.display.flip()


    def m (a, b):
        print(a)
