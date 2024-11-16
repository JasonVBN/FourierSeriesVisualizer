import numpy as np
import pygame as pg
import time
import datetime

class Arrow():
    def __init__(self, r, angVel, parent = None):
        self.r = r
        self.angVel = angVel
        self.angle = 0
        self.parent = parent

    def step(self, dt):
        self.angle += dt * self.angVel

    def getpos(self):
        dx = self.r * np.cos(np.deg2rad(self.angle))
        dy = self.r * np.sin(np.deg2rad(self.angle))
        center = ANCHOR
        if self.parent:
            center = self.parent.getpos()
        x = center[0] + dx
        y = center[1] + dy
        
        return (x,y)

    def __str__(self):
        return f"arrow with r = {self.r}"

def display():
##    screen.fill((255,255,255))
    pg.draw.circle(screen, (255,0,0), ANCHOR, 4)
    
    pg.draw.circle(screen, (255,0,0), a1.getpos(), 1)
    pg.draw.circle(screen, (0,100,255), a2.getpos(), 2)
    pg.draw.circle(screen, (0,255,0), a3.getpos(), 2)
    pg.display.flip()

a1 = Arrow(150,15)
a2 = Arrow(50,-60,a1)
a3 = Arrow(25,15,a2)


SIMULTIME = 500
TIMESTEP = .001

t = 0

WIDTH = 600
HEIGHT = 600
ANCHOR = (WIDTH//2, HEIGHT//2)
screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,0,0))

while t < SIMULTIME:
##    print("t =", t)
    a1.step(TIMESTEP)
    a2.step(TIMESTEP)
    a3.step(TIMESTEP)
    
    display()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            fname = f"img{timestamp}.jpg"
            pg.image.save(screen, fname)
            print("saved!")
            pg.quit()
    t += TIMESTEP
##    time.sleep(TIMESTEP/2)

