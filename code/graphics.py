"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame as pg
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pg.init()
 
# Set the width and height of the screen [width, height]
s = 800
size = (s, s)
screen = pg.display.set_mode(size)
 
pg.display.set_caption("My Game Hangman")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pg.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    pg.draw.lines(screen, BLACK, False, [[200, 600], [500, 600], [350, 600], [350, 200], [500, 200], [500, 250]], 8)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pg.quit()