import time
from sense_hat import SenseHat
from pygame.locals import *
import pygame


sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))	
		self.gaming = True

	def startGame(self):
		x = 0
		y = 7
		speed = 0.3
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			for event in pygame.event.get():
				if  event.type == KEYDOWN:
					if y == -1:
						exit()
					if x == 0:
						x = 8
						sense.set_pixel(x-1, y, (0, 255, 255))					
						y = y - 1
						x = 0
					else:
						sense.set_pixel(x-1, y, (0, 255, 255))
						y = y - 1
						 										
				else:
					if y == -1:
						exit()							
					sense.set_pixel(x, y, (0, 0, 255))
					time.sleep(speed)
					sense.set_pixel(x, y, (0, 0, 0))	
					time.sleep(speed)	
					x += 1
				
					if x == 8:
						x = 0
					
			
				
										
				
				 
					
			
			
					

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
