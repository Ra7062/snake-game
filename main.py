import pygame
from pygame.locals import *
import time
import random
size=40
color=97,167,68
class apple:
    def __init__(self,parent_screen):
        self.apple=pygame.image.load("Resources/apple.jpg").convert()
        self.parent_screen=parent_screen
        self.x=size
        self.y=size
    def draw(self):
        self.parent_screen.blit(self.apple,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.x=random.randint(0,19)*size
        self.y=random.randint(0,19)*size
class snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=pygame.image.load("Resources/block.jpg").convert()
        self.x=[size]*self.length
        self.y=[size]*self.length
        self.direction="right"
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    def move_right(self):
        self.direction="right"
    def move_left(self):
        self.direction="left"
    def move_up(self):
        self.direction="up"
    def move_down(self):
        self.direction="down"
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=="right":
            self.x[0]=self.x[0]+size
            self.draw()
        elif self.direction=="left":
            self.x[0]-=size
            self.draw()
        elif self.direction=="up":
            self.y[0]-=size
            self.draw()
        elif self.direction=="down":
            self.y[0]+=size
            self.draw()
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

class game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((800,800))
        self.speed=0.2
        self.snake=snake(self.surface,1)
        self.point=apple(self.surface)
        self.point.draw()
        self.snake.draw()
        pygame.display.flip()
    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False
    def boundary(self,x,y):
        if x>800 or y>800:
            return False
        elif x<0 or y<0:
            return False
        return True
    def play(self):
        self.render_background()
        self.snake.walk()
        self.point.draw()
        pygame.display.flip()
    def run(self):
        running=True
        while running:
            for i in range(3,self.snake.length):
                if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                    self.game_over()
                    running = False
            if not self.boundary(self.snake.x[0],self.snake.y[0]):
                self.game_over()
                running=False
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.point.x,self.point.y):
                    self.speed-=0.01
                    self.snake.increase_length()
                    self.point.move()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running=False
                    pygame.quit()
                elif event.type==KEYDOWN:
                    if event.key==K_DOWN:
                        self.snake.move_down()
                    elif event.key==K_RIGHT:
                       self.snake.move_right()
                    elif event.key==K_LEFT:
                        self.snake.move_left()
                    elif event.key==K_UP:
                        self.snake.move_up()
            self.play()
            time.sleep(self.speed)


if __name__=="__main__":
    a=game()
    a.run()
    