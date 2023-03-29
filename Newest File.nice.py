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
screenX = 1000
fps = 30
screenY = 800
gameRunning = False

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
    screen = pygame.display.set_mode ((screenX, screenY))
    font = pygame.font.Font('freesansbold.ttf' , 24)
    titleText = font.render('Arcade Games Emulator Menu' , True, white)
    titleTextArea = titleText.get_rect().center = (0, 0)
    subtitleText = font.render('Choose your Game' , True, white)
    subtitleTextArea = subtitleText.get_rect().center = (0, 40)
    optionOneText = font.render('1 - Snake' , True, white)
    optionOneTextArea = titleText.get_rect().center = (0, 80)
    optionTwoText = font.render('2 - Tetris' , True, white)
    optionTwoTextArea = titleText.get_rect().center = (0, 120)
    optionThreeText = font.render('3 - Pacman' , True, white)
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
                    gameRunning = True
                    menuRunning = False
                    s = snake()
                    s.__init__()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    print("Tetris Launch")
                    pygame.quit
                    gameRunning = False
                    menuRunning = False
                    t = tetris
                    t.figure()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    print("Pacman Launch")
                    pygame.quit
                    gameRunning = False
                    menuRunning = False
                    p = pacman
                    p.pacman



#####################SNAKE##########################
class snake:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        snakeGameWindow = pygame.display.set_mode((screenX, screenY))
        snakeSpeed = 10
        snakePos = (100, 50)
        snakeBody = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
        score = 0
        direction = 'RIGHT'
        fruitX = round(random.randrange(0, screenX) /10) * 10
        fruitY = round(random.randrange(0, screenY) / 10) * 10
        fruitPos = [fruitX, fruitY]
        fruitSpawn = True
        print("snake init")
        s = snake
        s.snakeGameLoop
        


    def snakeGameOver():
     gameOverText = font.render('Your Score is  ; ' + int(score), True, white)
     gameOverArea = gameOverText.get_rect().center(((screenX / 10) * 10), ((screenY / 10) * 10))
     snakeGameWindow.blit(gameOverText, GameOverArea)
     pygame.display.update()
     sleep(5)
     snake()
        

    def snakeScore():
     scoreText = font.render('Your Score is  ; ' + int(score), True, blue)
     scoreRect = scoreText.get_rect()
     snakeGameWindow.blit(scoreText,scoreRect)
     snake()
        


    def snakeGameLoop():
            while gameRunning == True:
                print("snakegameloop")
            #Keydowns to handle Direction Changes
                for event in pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 'UP'
                    if event.key == pygame.K_DOWN:
                        direction = 'DOWN'
                    if event.key == pygame.K_RiGHT:
                        direction = 'RIGHT'
                    if event.key == pygame.K_LEFT:
                        direction = 'LEFT'

                        #Direction causing the movement to change
                    if direction == 'UP':
                        snakePos[1] -= 10
                    if direction == 'DOWN':
                        snakePos[1] += 10
                    if direction == 'RIGHT':
                        snakePos[0] += 10
                    if direction == 'LEFT':
                        snakePos[0] -= 10



          #Escape to go back to the Menu
            for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    m = menu
                                    m.screen(self)



              #Spawning of Fruit
            snakeBody.insert(0, list(snakePos))
            if snakePos[0] == fruitPos[0] and snakePos[1] == fruitPos[1]:
              snakeScore = snakeScore + 1
              fruitSpawn = False
            else:
                snakeBody.pop()
            if not fruitSpawn:
                fruitX = round(random.randrange(0, screenX) /10) * 10
                fruitY = round(random.randrange(0, screenY) / 10) * 10
                fruitPos = [fruitX, fruitY]

            fruitSpawn = True
            snakeGameWindow.fill(black)

            for pos in snakeBody:
               pygame.draw.rect((snakeGameWindow, White, pygame.rect(pos[0],pos[1],10,10)))

            if snakePos[0] < 0 or snakePos[0] >  screenX-10:
                                 snakeGameOver()
            if snakePos[1] < 0 or snakePos[1] > window_Y-10:
                                 snakeGameOver()



            show_score(1, white, 'times new roman', 20)
            pygame.display.update()
            fps.tick(snake_speed)
                
        
      
              



        
        




menu()
