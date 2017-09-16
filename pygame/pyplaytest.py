import pygame
pygame.init()

#define some colors
BLACK = (0,0,0,0)
WHITE = (255,255,255,255)
GREEN = (58, 140, 56)
BROWN = (89, 60, 29)
YELLOW = (255, 255, 0)
BLUE = (84, 229, 227)

#open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#the loop will carry on until the user exits the game (such as clicking the close button)
keepPlaying = True

#the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#----main program loop----
while keepPlaying:

	#--main event loop--
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #user clicked close
			keepPlaying = False #flag that we're done so we exit this loop

	#--game logic should go here

	#--drawing code should go here
	#first, clear the screen to blue, for the sky
	screen.fill(BLUE)
	#then you can draw different shapes and lines or add text to your background stage
	#the sun
	pygame.draw.ellipse(screen, YELLOW, [50,50,100,100], 0)
	pygame.draw.line(screen, YELLOW, [20,20], [50,50], 5)
	pygame.draw.line(screen, YELLOW, [100,10], [100,40], 5)
	#the tree
	pygame.draw.rect(screen, BROWN, [535,250,30,150], 0)
	pygame.draw.ellipse(screen, GREEN, [500,150,100,150], 0)
	#the grass
	pygame.draw.rect(screen, GREEN, [0,400,700,100], 0)

	#-- update the screen with what we've drawn
	pygame.display.flip()

	#--limit to 60 frames per secon
	clock.tick(60)

#after the main program loop runs, we can stop the game engine:
pygame.quit()
