from turtle import Turtle, Screen
from random import randint

class Food(Turtle):
	"""docstring for Food"""
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.color("blue")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		randx = randint(-270, 270)
		randy = randint(-270, 270)
		self.goto(randx, randy)