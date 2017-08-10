import pygame

class Control:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def mover(self, x):
        self.x += x
