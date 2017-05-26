"""
Ongkon is a simple drawing application  created in python 3.6 using the pygame package.
Controls: 
	Draw:	Left-click and drag.
	Erase:	Right-click and drag.
IMPORTANT: pygame and python 3.x must be installed in the system to run Ongkon. 
--- Galib, Giti ------
"""


import pygame
from pygame import *



pygame.init()





#---rong berong -----------------------
darkgray = (50,50,50)
white = (255,255,255)
black = (0,0,0)
red = (186,40,7)
blue = (0,70,255)
green = (72, 145, 75)
yellow = (244,206,66)
violet = (129,7,86)
pink = (255,122,175)
chocolate = (114,61,20)
orange = (224, 116, 33)
magenda = (178, 14, 58)

currentColor = white
tulirSize = 7


#---janalar bornona-----------------------
window_horizontal = 950
window_verticle = 550

bgcolor = darkgray
amaderWindow = pygame.display.set_mode((window_horizontal,window_verticle))
amaderWindow.fill(darkgray)
pygame.display.set_caption("Ongkon")



rongbarta = pygame.image.load("colordirection.png")
amaderWindow.blit(rongbarta,(0,100))

icon = pygame.image.load("amadericon.png")
pygame.display.set_icon(icon)


#---main gameloop er shuru----------------
while True:
	
	for ghotona in pygame.event.get():
		print(ghotona)
		
		
		


		if ghotona.type == QUIT:
			pygame.quit()
			exit()

		if ghotona.type == KEYDOWN: 
			if ghotona.key == K_r:
				currentColor = red

			elif ghotona.key == K_b:
				currentColor = blue

			elif ghotona.key == K_g:
				currentColor = green

			elif ghotona.key == K_y:
				currentColor = yellow

			elif ghotona.key == K_v:
				currentColor = violet

			elif ghotona.key == K_p:
				currentColor = pink

			elif ghotona.key == K_h:
				currentColor = chocolate

			elif ghotona.key == K_o:
				currentColor = orange

			elif ghotona.key == K_m:
				currentColor = magenda


			else:
				currentColor = white
					
				
	

		if ghotona.type == MOUSEBUTTONDOWN:
			if ghotona.button == 1:
				pygame.draw.circle(amaderWindow,currentColor,[ ghotona.pos[0],ghotona.pos[1] ],tulirSize)

		if ghotona.type == MOUSEMOTION:
			
			if ghotona.buttons[0] == 1:
				pygame.draw.circle(amaderWindow,currentColor,[ ghotona.pos[0],ghotona.pos[1] ],tulirSize)

			if ghotona.buttons[2] == 1:
				pygame.draw.circle(amaderWindow,bgcolor,[ ghotona.pos[0],ghotona.pos[1] ],tulirSize)



	pygame.display.update()