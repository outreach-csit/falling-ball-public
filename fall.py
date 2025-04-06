"""
WORKSHOP Monday April 7th 2025 - SLDWC​ Young Women in Aerospace​

This is the first step in creating a falling ball simulation.
The code will be built up in steps, with each step adding more functionality.

The code is based on the Pygame library, which is a Python library for creating games and multimedia applications.

The template includes:
- Setup import modules.
- Draw screen stage where things will happen.
- Draw a circle in a position.

HAVE FUN!
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

# Ball properties
ball_radius = 50  # size of the ball
ball_x = WIDTH // 2  # initial x position of the ball
ball_y = HEIGHT // 2  # initial y position of the ball

# Main game loop
simulation_running = True  # Controls the main loop
while simulation_running:
    # if window is closed; set game_running = False to finish the game
    for event in pygame.event.get():
        # X / close button qwas pressed, exit!
        if event.type == pygame.QUIT:
            simulation_running = False

    # Move (not used yet – placeholder)

    # Draw background and ball
    SCREEN.fill('yellow')  # Fill the screen with a sky blue background
    pygame.draw.circle(SCREEN, 'blue', (ball_x, ball_y), ball_radius)  # Draw the ball

    # Update display and wait to keep frame rate
    pygame.display.update()
    clock.tick(FPS)  # Delay to keep frame rate steady
