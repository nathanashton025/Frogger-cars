# Programmer:Nathan Ashton 
# Date:
# Import functions for drawing gridlines and using sprites
import pygame 
pygame.init()
from pygame_grid import *
from sprite import *

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((640, 360))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("Frogger")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()


# Group that holds the vehicles
vehicles = pygame.sprite.Group()

# Background image
background = pygame.image.load("streets.png")

# Bus image
bus_image = pygame.image.load("bus.png")
bus_image = pygame.transform.rotozoom(bus_image, 0 , 0.30)

# Red car image
car_image = pygame.image.load("redcar.png")
car_image = pygame.transform.rotozoom(car_image, 0, 0.30)

# Taxi image
taxi_image = pygame.image.load("taxi.png")
taxi_image = pygame.transform.rotozoom(taxi_image, 0, 0.30)


# Frog image
frog_image = pygame.image.load("frog.png")

# Police image
police_image = pygame.image.load("police.png")
police_image = pygame.transform.rotozoom(police_image, 0, 0.13)

# Create the sprites
bus = Sprite(bus_image)
bus.position = (0,52)
bus.speed = 2 
bus.direction = 0
bus.add(all_sprites)
bus.add(all_sprites, vehicles)

police = Sprite(police_image)
police.position = (500,104)
police.speed = 5
police.direction = 180
police.add(all_sprites, vehicles)

car = Sprite(car_image)
car.position = (0,215)
car.speed = 5
car.direction = 180
car.add(all_sprites, vehicles)

taxi = Sprite(taxi_image)
taxi.position = (500, 260)
taxi.speed = 1
taxi.direction = 0
taxi.add(all_sprites, vehicles)

frogger = Sprite(frog_image)
frogger.mid_bottom = (320, 360)
frogger.direction = 0
frogger.add(all_sprites)

# Main Loop
while True:
    # Set the frame rate to 30 frames per second
    clock.tick(30)

    ### MANAGE IN-GAME EVENTS AND ANIMATIONS HERE
    # Check if vehicles are off screen
    for vehicle in vehicles:
        # Check it off right side
        if vehicle.left > 640:
            vehicle.right = 0
        # Check it off left side
        if vehicle.right < 0:
            vehicle.left = 640

    # Draw the background
    screen.blit(background, (0,0))


    # Update the sprites' locations
    all_sprites.update()

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()



