import pygame
import sys
import random

pygame.init()

#colous
playerColour = (0, 255, 0)
segmentColour = (playerColour)
foodColour = (255,0,0)
bgColour = (0,0,0)

#initialize window 
screenSize = 1000
screen = pygame.display.set_mode((screenSize, screenSize))
title = "Snake"
pygame.display.set_caption(title)
resolution = 20
pixelSize = screenSize / resolution

clock = pygame.time.Clock()
speed = 5

#initialize head
direction = 'up'
headPos = (screenSize/2, screenSize/2)

#list of segment positions
segmentPos = []

#dictionary for direction
directions = {
	'left' : (-1,0),
	'right' : (1,0),
	'up' : (0,-1),
	'down' : (0,1)
}

foodPres = False

running = True

while running:

	for event in pygame.event.get():
		#close window
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			#key inputs for direction
			if event.key == pygame.K_LEFT and direction != 'right':
				direction = 'left'
			elif event.key == pygame.K_RIGHT and direction != 'left':
				direction = 'right'
			elif event.key == pygame.K_UP and direction != 'down':
				direction = 'up'
			elif event.key == pygame.K_DOWN and direction != 'up':
				direction = 'down'
			
	if foodPres == False:
		foodx = random.randint(0,resolution-1)
		foody = random.randint(0,resolution-1)
		foodPos = (foodx*pixelSize, foody*pixelSize)
		foodPres = True


	segmentPos.append(headPos)

	#look up direction in movemt dictionary (line 31)
	movement = directions.get(direction)
	#calculate movemnet in relation to the screen
	movement = (movement[0]*pixelSize, movement[1]*pixelSize)

	#move the head the calculated distance
	headPos = (headPos[0]+movement[0], headPos[1]+movement[1])
	
	#remove last item
	segmentPos.remove(segmentPos[0])
	#Out of bounds detection
	if headPos[0] > screenSize-pixelSize or headPos[0] < 0\
	or headPos[1] >= screenSize or headPos[1] < 0:
		running = False

	#self intersection detection
	if headPos in segmentPos:
		running = False

	#food detection
	if headPos[0] == foodPos[0] and headPos[1] == foodPos[1]:
		foodPres = False
		segmentPos.append(foodPos)

	screen.fill(bgColour)

	#draw food
	pygame.draw.rect(screen,foodColour,(foodPos[0],foodPos[1], pixelSize, pixelSize))

	#draw segments
	for i, segments in enumerate(segmentPos):
		segment = segmentPos[i]
		pygame.draw.rect(screen,segmentColour,(segment[0],segment[1], pixelSize, pixelSize))

	#draw head
	pygame.draw.rect(screen,playerColour,(headPos[0],headPos[1], pixelSize, pixelSize))

	clock.tick(speed)

	pygame.display.update()