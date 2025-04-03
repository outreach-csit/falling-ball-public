# Falling Ball Simulation - Step-by-Step Tutorial

In this tutorial, we’ll use code to control what appears on the screen. Coding is how we tell the computer what to do, using a programming language—in this case, Python. Python is widely used because it’s easy to read (the code looks a bit like plain English) and can be used in many areas. It’s used by companies like Google, Netflix, Spotify, and NASA, and across fields like web development, data science, automation, scientific research, game design, and healthcare—for things like predictive analytics and image analysis. It works well for beginners and is powerful enough for complex projects.

We’ll write instructions using functions, which are named blocks of code that do something—like moving the ball or drawing on the screen. Functions can take variables as input, which are like labelled boxes that store information we want to use or change. Rather than writing everything from scratch, we can also use libraries—collections of functions written by others that we can bring into our own project. Pygame is one such library. It makes it easy to draw on the screen and build interactive projects like animations and simple games.

In this tutorial, we’ll simulate a ball falling and bouncing off the ground. We’ll adjust its motion to include gravity and make it lose energy with each bounce. As you go, you’ll learn how to use basic programming ideas like variables, functions, loops, and if-statements. These are building blocks that can be used to make a wide range of exciting projects.

The tutorial is organised into 10 steps. Each step adds a new idea and shows how we can use code to describe motion and animate the virtual ball. Each step adds a new idea, and you’ll see how we use code to show movement.

---

## Step 0: Setup VSCode and the code

To get started with this tutorial, you'll need to use VSCode, and get the starting python code file. To get underway:
1. Open VSCode
1. Open a new folder to place the code exercise
1. Create a new file called `fall.py`
1. Copy-and-paste the starting code from `fall01.py` example into the new file
1. Save the file
1. Run the file by pressing the "play" triangle button in the top-right corner of the VSCode window.

---

## Step 1: Set up the screen and draw a ball

In Pygame—and in most libraries designed for drawing or graphics—the screen is like a piece of graph paper. The top-left corner is (0, 0). Moving to the right increases x. Moving down increases y. So (100, 100) means 100 pixels across and 100 pixels down.

Here’s the basic code to open a window and draw a circle (our ball) in the middle. You just need to run it and test it.

In the code, you'll see lines that start with a `#` symbol — these are **comments**. They're not run by the computer. Comments are used to explain what each part of the code does, which makes it easier to read later.

You’ll also see **functions** and **variables** in action. For example:

```python
pygame.draw.circle(SCREEN, (250, 160, 30), (ball_x, ball_y), BALL_RADIUS)
```

This line draws a circle on the screen:

- `SCREEN` is where we're drawing it.
- `(250, 160, 30)` is the colour in RGB (red, green, blue).
- `(ball_x, ball_y)` gives the position.
- `BALL_RADIUS` is the size.

In this case, `pygame` is the library, `draw` is the module inside it, and `circle` is the function that does the actual drawing. If you're using VS Code, you can hover over the function name to see what inputs it takes. Or you can search online—typing something like “pygame draw circle” into your browser will often give you clear documentation and examples. You can also use the interactive Python shell to explore help functions if you're comfortable doing so.

Here’s the full code for this step:

```python
"""
- Setup import modules
- Draw screen stage where things will happen
- Draw a circle in a position
"""

import pygame  # Import the Pygame library
pygame.init()  # Set up Pygame

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
```

When you run this, you’ll see a circle drawn in a window.

---

## Step 2: Move the ball higher up

Now modify the code to move the ball higher up in the screen.

You can do this by changing these lines to tha number you like
```python
WIDTH = 1200
HEIGHT = 800
```

---

## Step 3: Make the ball fall at constant speed

Now let’s add motion to the ball so it falls down at a constant speed. Each time the loop runs (which happens 60 times per second), we’ll add a small amount to `ball_y`. This moves the ball lower on the screen.

You can write this as:

```python
ball_y = ball_y + 3
```

Or use the shortcut:

```python
ball_y += 3
```

This line means: take the current value of `ball_y` and increase it by 3. It makes the ball move down smoothly in small steps each frame.

To try this, add `ball_y += 3` just below the `# Move` line in your code from Step 1. When you run it, the ball should now fall downward at a constant speed.

---

## Step 4: Add a floor and stop the ball when it reaches it

Let’s add a floor and stop the ball once it hits it. At the moment, the ball just keeps falling because there’s nothing telling it to stop.

First, we define some new constants:

```python
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
```

This means the floor is 100 pixels high, and it starts at the bottom of the screen.

We define these constants in the `# Constants` section of the code.

Then, just below the `pygame.draw.circle` line, we draw a rectangle to show the floor:

```python
pygame.draw.rect(SCREEN, (100, 100, 100), (0, FLOOR_Y, WIDTH, HEIGHT))
```

Then in the `move` section, we stop the ball when it hits the floor:

```python
if not (ball_y + BALL_RADIUS) > FLOOR_Y:
    ball_y += 3
```

This checks whether the bottom of the ball has passed the top of the floor. If it hasn’t, we keep it falling.

Now when you run the program, the ball drops and stops right on top of the floor.

---

## Step 5: Add gravity as acceleration

In real life, gravity speeds things up as they fall. We can copy that by gradually increasing the ball’s speed every frame.

In the `# constants` section add a constant to represent gravity and in the `# variables` section add a variable to represent velocity. The code should then read:

```python
# constants
GRAVITY = 0.50
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
BALL_RADIUS = 30 

# variables
run = True
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_velocity = 0
```

The `#move` section then becomes

```python
    # move
    if not (ball_y + BALL_RADIUS) > FLOOR_Y:
        ball_y += ball_velocity
    else:
        ball_velocity = 0
        ball_y = FLOOR_Y - BALL_RADIUS

    # physics
    ball_velocity += GRAVITY
```

Now when you Run the file the ball should fall faster and faster and then stop when it hits the floor

---

## Step 6: Make the ball bounce (no energy loss)

We’ll now make the ball bounce by flipping the direction of its velocity when it hits the floor.

```python
    # move
    if not (ball_y + BALL_RADIUS) > FLOOR_Y:
        ball_y += ball_velocity
    else:
        ball_velocity = ball_velocity * -1 # Reverse the velocity 
        ball_y = FLOOR_Y - BALL_RADIUS

    # physics
    ball_velocity += GRAVITY
```

The ball now bounces back up with the same speed it had when falling.

---

## Step 7: Add energy loss when bouncing

In real life, each bounce loses a bit of energy. We can copy that by reducing the velocity a little each time the ball hits the floor.

First we need to define an energy loss constant:

```python
# constants
GRAVITY = 0.50
FLOOR_HEIGHT = 100
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
ENERGY_LOSS = 2
```

Then we update the code that moves the ball:

```python
    # move
    if not (ball_y + BALL_RADIUS) > FLOOR_Y:
        ball_y += ball_velocity
    else:
        ball_velocity = (ball_velocity * -1) + ENERGY_LOSS
        ball_y = FLOOR_Y - BALL_RADIUS

    # physics
    ball_velocity += GRAVITY
```

Now when you run the code, the ball will bounce lower and lower each time, eventually settling.

---

## Step 8: Change circle to an image, add floor/background

We’ll now replace the circle with an image of a ball, and add a background. For this, we need to load another Python package:

```python
import os
```

This helps us find and load files stored in folders.

Right after setting up the screen, add the following code to load the images:

```python
# load assets
ball_img = pygame.image.load(os.path.join("assets", "soccerball.png"))
back_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "soccer tennis court.png")), (WIDTH, HEIGHT))
```

To work with the new images, we’ll also increase the floor height so the ball can bounce higher and look right against the background:

```python
FLOOR_HEIGHT = 200  # Adjusted to suit the background image
FLOOR_Y = HEIGHT - FLOOR_HEIGHT
```

Update the variables to include:

```python
ball_x = WIDTH // 2 - ball_img.get_width() // 2  # Centre the image
ball_y = 100  # We moved the ball higher up the screen to give it room to fall and bounce
ball_velocity = 0
ball_rect = pygame.Rect(ball_x, ball_y, ball_img.get_width(), ball_img.get_height())
floor_rect = pygame.Rect(0, FLOOR_Y, WIDTH, FLOOR_HEIGHT)
```

When drawing the ball image, make sure to position it correctly using:

```python
SCREEN.blit(ball_img, (ball_x, ball_y))
```

This will make the ball look like a soccer ball and add a themed background.

---

## Step 9: Add music

In this step we add music. We’ll include background music and a bounce sound effect each time the ball hits the floor.

First, we need to import Pygame’s mixer, which lets us play audio:

```python
import pygame
from pygame import mixer
import os
pygame.init()
mixer.init()
```

Next we load the music and sound files. You can add this after setting up the clock and frame rate:

```python
# setup consistent frame rate
clock = pygame.time.Clock()
FPS = 60

# music
bounce = pygame.mixer.Sound(os.path.join("sound", "bounce.wav")) #define bounce as the sound in the file bounce.wav
back = pygame.mixer.Sound(os.path.join("sound", "back.mp3")) #define the background music
back.play(-1) # play background music on loop
```

Then, in the main loop where the ball bounces, play the sound when it hits the floor, but not when the ball is settling.

```python
    # move
    if not (ball_y + BALL_RADIUS) > FLOOR_Y:
        ball_y += ball_velocity

    else:
        ball_velocity = (ball_velocity * -1) + ENERGY_LOSS
        ball_y = FLOOR_Y - BALL_RADIUS

        if not (ball_velocity >  -3 and ball_velocity < 3):
            bounce.play()
```

---

## Step 10: Use Pygame's built-in collision detection (advanced)

If you want to go a bit further, Pygame has built-in tools to detect when objects bump into each other—this is called collision detection. Pygame uses something called a `Rect` (short for rectangle) to represent the position and size of things on the screen.

We can create a rectangle around the ball and check if it overlaps with another rectangle (like the floor).

The rectangles for the ball and floor need to be defined in the `variables` code block

```python
# variables

run = True
ball_x = WIDTH // 2 - ball_img.get_width() // 2
ball_y = 100
ball_velocity = 0
ball_rect = pygame.Rect(ball_x, ball_y, ball_img.get_width(), ball_img.get_height())
floor_rect = pygame.Rect(0, FLOOR_Y, WIDTH, FLOOR_HEIGHT)
```

Then in the main game loop, we check if the rectangle representing the ball has collided with the rectangle representing the floor, if not we update the velocity of the ball. Otherwise we reflect the balls velocity and add energy loss. We need to then reset the rectangle representing the ball to be analogous with the balls new position. The main game loop then looks like:

```python
# main game loop

while run:

    # loop through all events
    for event in pygame.event.get():

        # if the X / close button is pressed then exit the loop
        if event.type == pygame.QUIT:
            run = False

    # draw

    SCREEN.blit(back_img, (0, 0))
    SCREEN.blit(ball_img, (ball_x, ball_y))
    
    # move
    
    if not pygame.Rect.colliderect(ball_rect, floor_rect):
        ball_y += ball_velocity
        
    else:
        ball_y = FLOOR_Y - ball_img.get_height()
        ball_velocity = (ball_velocity * -1) + ENERGY_LOSS
  
        if not (ball_velocity >  -3 and ball_velocity < 3):
            bounce.play()
```

This is a more advanced technique, but it's useful if you want to check collisions between different objects—like bouncing off walls, hitting targets, or building a game.

---

## Summary

You’ve now built a full animation using python! You’ve used concepts like:

- Coordinate systems
- Velocity and acceleration
- Conditional logic (if statements)
- Image and audio assets

Feel free to experiment with different sizes, speeds, colours, or even make your own version
