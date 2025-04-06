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

    # Draw background and ball
    SCREEN.fill('sky blue')  # Fill the screen with a sky blue background
    pygame.draw.circle(SCREEN, (250, 160, 30), (ball_x, ball_y), ball_radius)  # Draw the ball


    # Move (not used yet – placeholder)

    # Update display and wait to keep frame rate
    pygame.display.update()
    clock.tick(FPS)  # Delay to keep frame rate steady
