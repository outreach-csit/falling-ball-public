"""
- Setup import modules
- Draw screen stage where things will happen
- Draw a circle in a position
"""
import os
import pygame  # we will use the Pygame library

pygame.init()  # initialize the library

# Set up consistent frame rate
clock = pygame.time.Clock()
FPS = 60  # Frames per second – how often the screen updates

# music
bounce_sound = pygame.mixer.Sound(
    os.path.join("sound", "bounce.wav")
)  # define bounce as the sound in the file bounce.wav
back_sound = pygame.mixer.Sound(
    os.path.join("sound", "back.mp3")
)  # define the background music


# Set up the screen
WIDTH = 1200
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the screen window
pygame.display.set_caption("Falling Ball Simulation :)")  # Window title

# load assets
ball_img = pygame.image.load(os.path.join("assets", "soccerball.png"))
back_img = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "basketball-netball-court.png")),
    (WIDTH, HEIGHT),
)

# Ball properties
ball_radius = 50  # size of the ball
ball_x = WIDTH // 2  # initial x position of the ball
ball_x = WIDTH // 2 - ball_img.get_width() // 2  # Centre the image

ball_y = HEIGHT // 2  # initial y position of the ball
ball_y = 50  # STEP 2


# STEP 4
FLOOR_HEIGHT = 200
FLOOR_Y = HEIGHT - FLOOR_HEIGHT

GRAVITY = 0.50  # STEP 5
ENERGY_LOSS = 0.1
ball_velocity = 0  # initial velocity of the ball

# Main game loop
back_sound.play(-1)  # play background music on loop
simulation_running = True  # Controls the main loop
while simulation_running:
    # if window is closed; set game_running = False to finish the game
    for event in pygame.event.get():
        # X / close button qwas pressed, exit!
        if event.type == pygame.QUIT:
            simulation_running = False

    # Move (not used yet – placeholder)
    # if not (ball_y) >= FLOOR_Y: # STEP 4
    if not (ball_y + ball_radius) > FLOOR_Y: # STEP 4
        # ball_y += 2  # STEP 3
        ball_y += ball_velocity  # STEP 5
    else:
        ball_y = FLOOR_Y - ball_radius  # STEP 5
        # ball_velocity = 0  # STEP 5
        ball_velocity = ball_velocity * -1  # STEP 6
        ball_velocity = ball_velocity * (1 - ENERGY_LOSS)
        if abs(ball_velocity) < 4:
            ball_velocity = 0
        else:
            bounce_sound.play()
        # print(ball_velocity)

    # apply gravity
    ball_velocity += GRAVITY  # STEP 5

    # Draw background and ball
    # SCREEN.fill("yellow")  # Fill the screen with a sky blue background
    # pygame.draw.circle(SCREEN, "blue", (ball_x, ball_y), ball_radius)  # Draw ball

    # STEP 8
    # pygame.draw.rect(SCREEN, "black", (0, FLOOR_Y, WIDTH, HEIGHT))  # STEP 4
    SCREEN.blit(back_img, (0, 0))
    SCREEN.blit(ball_img, (ball_x, ball_y))

    # Update display and wait to keep frame rate
    pygame.display.update()
    clock.tick(FPS)  # Delay to keep frame rate steady
