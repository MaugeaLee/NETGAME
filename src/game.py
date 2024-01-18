import pygame
import threading
import time
from config import constant

RETURNING = ""
class Game():
    def __init__(self):
        self.controlData = ""
        thread1 = threading.Thread(target=self.game)
        try:
            thread1.start()
        except KeyboardInterrupt as e:
            pass

    def returnData(self):
        while True:
            print(self.controlData)
            time.sleep(0.5)


    def game(self):
        # pygame init
        print("game open")
        pygame.init()

        width = constant.WINDOW_WIDTH
        height = constant.WINDOW_HEIGHT
        screen = pygame.display.set_mode(((width, height)))
        pygame.display.set_caption("Chat")
        clock = pygame.time.Clock()

        # 상태 변수
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    self.controlData = "blank"

                    if event.key == pygame.K_LEFT:
                        self.controlData = constant.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.controlData = constant.RIGHT
                    elif event.key == pygame.K_UP:
                        self.controlData = constant.UP
                    elif event.key == pygame.K_DOWN:
                        self.controlData = constant.DOWN
                    else:
                        self.controlData = ""
                elif event.type == pygame.KEYUP:
                    self.controlData = ""

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()