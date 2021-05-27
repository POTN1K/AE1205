import pygame as pg

# Start pygame and close it
pg.init()

# Create a window
x_max = 600  # Coordinate from top-left to bottom-right
y_max = 600
reso = (x_max, y_max)  # Resolution
scr = pg.display.set_mode(reso)  # Surface object(contain image data)
scrrect = scr.get_rect()

bgcolor = (0, 0, 0)  # 0 to 255
scr.fill(bgcolor)  # Fill screen color

# Add an image
ufopng = pg.image.load("Data/Pygame_Learn/ufo.png")  # Use Paint 3D
ufoimg = pg.transform.scale(ufopng, (101, 59))  # Change image
uforect = ufoimg.get_rect()  # Rectangle object

# Put at a place
x = 300
uforect.centerx = x  # Position
# uforect.centery = 300
# scr.blit(ufoimg, uforect)   # Block image transfer (Copies a new image)

# Time the game
ticks_per_sec = 1000
start_time = pg.time.get_ticks() / ticks_per_sec
# Starts a timer and measures how much times passes, with which to calculate how to move


# Change velocities
star_y = 500
end_y = -100
velocity_y = -100
x_step = 0.10 # Pixels

# Make it move
running = True
while running:  # Move rocket

    # Use keys
    pg.event.pump() # Avoid spinning ball
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False
    if keys[pg.K_LEFT]:
        x -= x_step
    if keys[pg.K_RIGHT]:
        x += x_step

    time = pg.time.get_ticks() / ticks_per_sec - start_time  # Time passed
    y = star_y + velocity_y * time

    # Change y
    uforect.centery = y
    pg.draw.rect(scr, bgcolor, scrrect)
    scr.blit(ufoimg, uforect)

    # Change x

    uforect.centerx = x

    # Display
    pg.display.flip()  # Drawing happens in background, to avoid issues

    if y < end_y:
        running = False
pg.quit()
