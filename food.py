from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_location_x = randint(-280, 280)
        food_location_y = randint(-280, 280)
        self.goto(food_location_x, food_location_y)
