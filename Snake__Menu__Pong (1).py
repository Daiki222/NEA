import pygame
import random
import time
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (255, 255, 0)
green = (0, 255, 255)
orange = (255,100,0)
blue = (0, 0, 128)
purple = (148,0,211)
red = (205,38,38)
windowclock = pygame.time.Clock()
x = 500
y = 500
height = 0
width = 0
game = 'tetris'
gameRunning = False
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

class menu:
  #Init the menu
  def __init__(self):
    print("Creating Menu")
    pygame.init()
    pygame.display.set_caption('Arcade Games Emulator')
    self.x = x
    self.y = y
    menu.screen(self)

  #Display menu and handle user interaction
  def screen(self):
    print("Display Menu Screen")
    screen = pygame.display.set_mode ((x, y))
    font = pygame.font.Font('freesansbold.ttf' , 24)
    titleText = font.render('Arcade Games Emulator Menu' , True, white)
    titleTextArea = titleText.get_rect().center = (0, 0)
    subtitleText = font.render('Choose your Game' , True, white)
    subtitleTextArea = subtitleText.get_rect().center = (0, 40)
    optionOneText = font.render('1 - Snake' , True, white)
    optionOneTextArea = titleText.get_rect().center = (0, 80)
    optionTwoText = font.render('2 - Pong' , True, white)
    optionTwoTextArea = titleText.get_rect().center = (0, 120)
    optionThreeText = font.render('3 - Tetris' , True, white)
    optionThreeTextArea = titleText.get_rect().center = (0, 160)
    info = font.render('Please choose your game' , True, white)
    infoTextArea = titleText.get_rect().center = (0,  320)
    menuRunning = True
    gameRunning = True
    #Display menu and handle user interaction
    while menuRunning:
      screen.fill(black)
      screen.blit(titleText, titleTextArea)
      screen.blit(subtitleText, subtitleTextArea)
      screen.blit(optionOneText, optionOneTextArea)
      screen.blit(optionTwoText, optionTwoTextArea)
      screen.blit(optionThreeText, optionThreeTextArea)
      screen.blit(info, infoTextArea)
      pygame.display.update()
      print("here1")
      while gameRunning == True:
        for event in pygame.event.get():
            print("here3")
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Snake Launch")
                    pygame.quit
                    gameRunning = False
                    menuRunning = False
                    s = snake()
                    s.__init__()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    print("Pong Launch")
                    pygame.quit
                    gameRunning = False
                    menuRunning = False
                    pongGame()
                    


            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_3:
                      print("Tetris Launch")
                      pygame.quit
                      gameRunning = False
                      menuRunning = False
                      Tetris(height,width)

                    

class snake:
    def __init__(self):
            pygame.init()
            snake_speed = 15
            window_x = 720
            window_y = 480
            pygame.display.set_caption('Snake')
            game_window = pygame.display.set_mode((window_x, window_y))
            fps = pygame.time.Clock()
            snake_position = [100, 50]
            snake_body = [[100, 50],
                                    [90, 50],
                                    [80, 50],
                                    [70, 50]
                                    ]
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                            random.randrange(1, (window_y//10)) * 10]
            fruit_spawn = True
            direction = 'RIGHT'
            change_to = direction
            score = 0
            def show_score(choice, color, font, size):
                    score_font = pygame.font.SysFont(font, size)
                    score_surface = score_font.render('Score : ' + str(score), True, color)
                    score_rect = score_surface.get_rect()

            def game_over():
                    my_font = pygame.font.SysFont('times new roman', 50)
                    game_over_surface = my_font.render(
                            'Your Score is : ' + str(score), True, red)
                    game_over_rect = game_over_surface.get_rect()
                    game_over_rect.midtop = (window_x/2, window_y/4)
                    game_window.blit(game_over_surface, game_over_rect)
                    pygame.display.flip()
                    time.sleep(2)
                    m = menu()
                    m.screen()
                    
                    for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    m = menu
                                    m.screen(self)
                    
   
                    


            # Main Function
            while True:
                    
                    # handling key events
                    for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP:
                                            change_to = 'UP'
                                    if event.key == pygame.K_DOWN:
                                            change_to = 'DOWN'
                                    if event.key == pygame.K_LEFT:
                                            change_to = 'LEFT'
                                    if event.key == pygame.K_RIGHT:
                                            change_to = 'RIGHT'
                                    if event.key == pygame.K_ESCAPE:
                                            m = menu
                                            m.screen(self)

                    # If two keys pressed simultaneously
                    # we don't want snake to move into two
                    # directions simultaneously
                    if change_to == 'UP' and direction != 'DOWN':
                            direction = 'UP'
                    if change_to == 'DOWN' and direction != 'UP':
                            direction = 'DOWN'
                    if change_to == 'LEFT' and direction != 'RIGHT':
                            direction = 'LEFT'
                    if change_to == 'RIGHT' and direction != 'LEFT':
                            direction = 'RIGHT'

                    # Moving the snake
                    if direction == 'UP':
                            snake_position[1] -= 10
                    if direction == 'DOWN':
                            snake_position[1] += 10
                    if direction == 'LEFT':
                            snake_position[0] -= 10
                    if direction == 'RIGHT':
                            snake_position[0] += 10

                    # Snake body growing mechanism
                    # if fruits and snakes collide then scores
                    # will be incremented by 10
                    snake_body.insert(0, list(snake_position))
                    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                            score += 10
                            fruit_spawn = False
                    else:
                            snake_body.pop()
                            
                    if not fruit_spawn:
                            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                                            random.randrange(1, (window_y//10)) * 10]
                            
                    fruit_spawn = True
                    game_window.fill(black)
                    
                    for pos in snake_body:
                            pygame.draw.rect(game_window, green,
                                                            pygame.Rect(pos[0], pos[1], 10, 10))
                    pygame.draw.rect(game_window, white, pygame.Rect(
                            fruit_position[0], fruit_position[1], 10, 10))

                    # Game Over conditions
                    if snake_position[0] < 0 or snake_position[0] > window_x-10:
                            game_over()
                    if snake_position[1] < 0 or snake_position[1] > window_y-10:
                            game_over()

                    # Touching the snake body
                    for block in snake_body[1:]:
                            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                                    game_over()

                    # displaying score countinuously
                    show_score(1, white, 'times new roman', 20)

                    # Refresh game screen
                    pygame.display.update()

                    # Frame Per Second /Refresh Rate
                    fps.tick(snake_speed)

####################################################################################################################################################################################

class pongGame:
    def __init__(self):
        # Initialize Pygame
        print("pong")
        pygame.init()

        # Set up the game window
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Pong")

        # Set up the game clock
        self.clock = pygame.time.Clock()

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Define the ball
        self.BALL_RADIUS = 10
        self.ball_x = self.window_width // 2
        self.ball_y = self.window_height // 2
        self.ball_dx = random.choice([-5, 5])
        self.ball_dy = random.choice([-5, 5])

        # Define the paddles
        self.PADDLE_WIDTH = 15
        self.PADDLE_HEIGHT = 100
        self.paddle_left_x = 50
        self.paddle_left_y = self.window_height // 2 - self.PADDLE_HEIGHT // 2
        self.paddle_right_x = self.window_width - 50 - self.PADDLE_WIDTH
        self.paddle_right_y = self.window_height // 2 - self.PADDLE_HEIGHT // 2

        # Set up the score
        self.score_left = 0
        self.score_right = 0
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        print("pong2")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def move_paddles(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.paddle_left_y > 0:
            self.paddle_left_y -= 5
        if keys[pygame.K_s] and self.paddle_left_y < self.window_height - self.PADDLE_HEIGHT:
            self.paddle_left_y += 5
        if keys[pygame.K_UP] and self.paddle_right_y > 0:
            self.paddle_right_y -= 5
        if keys[pygame.K_DOWN] and self.paddle_right_y < self.window_height - self.PADDLE_HEIGHT:
            self.paddle_right_y += 5

    def move_ball(self):
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Check for collisions with walls
        if self.ball_y - self.BALL_RADIUS < 0 or self.ball_y + self.BALL_RADIUS > self.window_height:
            self.ball_dy = -self.ball_dy
        if self.ball_x - self.BALL_RADIUS < 0:
            self.ball_dx = -self.ball_dx
            self.score_right += 1
            self.ball_x = self.window_width // 2
            self.ball_y = self.window_height // 2
        if self.ball_x + self.BALL_RADIUS > self.window_width:
            self.ball_dx = -self.ball_dx
            self.score_left += 1
            self.ball_x = self.window_width // 2
            self.ball_y = self.window_height // 2

        # Check for collisions with paddles
        if self.ball_x - self.BALL_RADIUS < self.paddle_left_x + self.PADDLE_WIDTH and \
                self.paddle_left_y < self.ball_y < self.paddle_left_y + self.PADDLE_HEIGHT:
            self.ball_dx = -self.ball_dx
        if ball_x + BALL_RADIUS > paddle_right_x and \
            self.paddle_right_y < ball_y < paddle_right_y + PADDLE_HEIGHT:
                ball_dx = -ball_dx


    def draw_objects(self):
        window.fill(BLACK)
        pygame.draw.rect(window, WHITE, (paddle_left_x, paddle_left_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(window, WHITE, (paddle_right_x, paddle_right_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)
            # Draw the score
        score_text = font.render(f"{score_left} : {score_right}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, 30))
        window.blit(score_text, score_rect)

        # Update the display
        pygame.display.update()

        # Set the game's FPS
        clock.tick(60)
    pygame.quit()



################################################
import pygame
import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
            def __init__(self, height, width):
                self.level = 2
                self.score = 0
                self.state = "start"
                self.field = []
                self.height = 0
                self.width = 0
                self.x = 100
                self.y = 60
                self.zoom = 20
                self.figure = None
            
                self.height = height
                self.width = width
                self.field = []
                self.score = 0
                self.state = "start"
                for i in range(height):
                    new_line = []
                    for j in range(width):
                        new_line.append(0)
                    self.field.append(new_line)

            def new_figure(self):
                self.figure = Figure(3, 0)

            def intersects(self):
                intersection = False
                for i in range(4):
                    for j in range(4):
                        if i * 4 + j in self.figure.image():
                            if i + self.figure.y > self.height - 1 or \
                                    j + self.figure.x > self.width - 1 or \
                                    j + self.figure.x < 0 or \
                                    self.field[i + self.figure.y][j + self.figure.x] > 0:
                                intersection = True
                return intersection

            def break_lines(self):
                lines = 0
                for i in range(1, self.height):
                    zeros = 0
                    for j in range(self.width):
                        if self.field[i][j] == 0:
                            zeros += 1
                    if zeros == 0:
                        lines += 1
                        for i1 in range(i, 1, -1):
                            for j in range(self.width):
                                self.field[i1][j] = self.field[i1 - 1][j]
                self.score += lines ** 2

            def go_space(self):
                while not self.intersects():
                    self.figure.y += 1
                self.figure.y -= 1
                self.freeze()

            def go_down(self):
                self.figure.y += 1
                if self.intersects():
                    self.figure.y -= 1
                    self.freeze()

            def freeze(self):
                for i in range(4):
                    for j in range(4):
                        if i * 4 + j in self.figure.image():
                            self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
                self.break_lines()
                self.new_figure()
                if self.intersects():
                    self.state = "gameover"

            def go_side(self, dx):
                old_x = self.figure.x
                self.figure.x += dx
                if self.intersects():
                    self.figure.x = old_x

            def rotate(self):
                old_rotation = self.figure.rotation
                self.figure.rotate()
                if self.intersects():
                    self.figure.rotation = old_rotation


        # Initialize the game engine
            pygame.init()

            # Define some colors
            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GRAY = (128, 128, 128)

            size = (400, 500)
            screen = pygame.display.set_mode(size)

            pygame.display.set_caption("Tetris")

            # Loop until the user clicks the close button.
            done = False
            clock = pygame.time.Clock()
            fps = 25
            self.game = Tetris(20, 10)
            counter = 0

            pressing_down = False

            while not done:
                if game.figure is None:
                    game.new_figure()
                counter += 1
                if counter > 100000:
                    counter = 0

                if counter % (fps // game.level // 2) == 0 or pressing_down:
                    if game.state == "start":
                        game.go_down()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            game.rotate()
                        if event.key == pygame.K_DOWN:
                            pressing_down = True
                        if event.key == pygame.K_LEFT:
                            game.go_side(-1)
                        if event.key == pygame.K_RIGHT:
                            game.go_side(1)
                        if event.key == pygame.K_SPACE:
                            game.go_space()
                        if event.key == pygame.K_ESCAPE:
                            game.__init__(20, 10)

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            pressing_down = False

                screen.fill(WHITE)

                for i in range(game.height):
                    for j in range(game.width):
                        pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        if game.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game.field[i][j]],
                                             [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

                if game.figure is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game.figure.image():
                                pygame.draw.rect(screen, colors[game.figure.color],
                                                 [game.x + game.zoom * (j + game.figure.x) + 1,
                                                  game.y + game.zoom * (i + game.figure.y) + 1,
                                                  game.zoom - 2, game.zoom - 2])

                font = pygame.font.SysFont('Calibri', 25, True, False)
                font1 = pygame.font.SysFont('Calibri', 65, True, False)
                text = font.render("Score: " + str(game.score), True, BLACK)
                text_game_over = font1.render("Game Over", True, (255, 125, 0))
                text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

                screen.blit(text, [0, 0])
                if game.state == "gameover":
                    screen.blit(text_game_over, [20, 200])
                    screen.blit(text_game_over1, [25, 265])

                pygame.display.flip()
                clock.tick(fps)

            pygame.quit()



menu()
