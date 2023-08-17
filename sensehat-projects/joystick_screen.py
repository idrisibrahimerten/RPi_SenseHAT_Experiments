from pygame.locals import *
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

running = True

x = 0
y = 0
sense.set_pixel(x, y, 255, 255, 255)

while running:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF

            if event.direction == "down" and y < 7:
                y = y + 1
            elif event.direction == "up" and y > 0:
                y = y - 1
            elif event.direction == "right" and x < 7:
                x = x + 1
            elif event.direction == "left" and x > 0:
                x = x - 1

            sense.set_pixel(x, y, 255, 255, 255)

        if event.direction == "middle":
            running = False
            sense.clear()
            print("BYE")
            break
