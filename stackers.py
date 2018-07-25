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
		pygame.time.set_timer(USEREVENT +1, 200)
		while self.gaming:
			for event in pygame.event.get():			
				sense.set_pixel(x, y, (0, 0, 255))
				x = x + 1				
				if x > 1:
					sense.set_pixel(x-2, y, (0, 0, 0))						
					if x == 8:
						x = 0
				elif x == 1:		
					sense.set_pixel(7, y, (0, 0, 0))
			if  event.type == KEYDOWN:			
				self.gaming = False
				
										
				
				 
					
			
			
					

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
