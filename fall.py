"""
- Setup import modules
- Draw screen stage where things will happen
- Draw a circle in a position
"""
import pygame  # we will use the Pygame library
pygame.init()  # initialize the library

# Set up consistent frame rate
clock = pygame.time.Clock()
FPS = 60  # Frames per second – how often the screen updates

# Set up the screen
WIDTH = 1200
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen window
pygame.display.set_caption('Falling Ball Simulation :)')  # Window title

# Constants
BALL_RADIUS = 50  # Size of the ball

# Variables
run = True  # Controls the main loop
ball_x = WIDTH // 2  # Horizontal position of the ball on the screen. 
ball_y = HEIGHT // 2  # Vertical position of the ball on the screen.

# Main game loop
while run:
    # Loop through all events
    for event in pygame.event.get():
        # If the X / close button is pressed, exit the loop
        if event.type == pygame.QUIT:
            run = False

    # Draw background and ball
    SCREEN.fill('sky blue')  # Fill the screen with a sky blue background
    pygame.draw.circle(SCREEN, (250, 160, 30), (ball_x, ball_y), BALL_RADIUS)  # Draw the ball

    # Move (not used yet – placeholder)

    # Update display and wait to maintain consistent frame rate
    pygame.display.update()
    clock.tick(FPS)  # Delay to keep frame rate steady

