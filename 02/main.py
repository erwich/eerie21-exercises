from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

# Constant values for colors
# These are variables that represent color values using (red, green, blue)
GREEN = (50, 164, 49)
YELLOW = (247, 181, 0)
RED = (187, 30, 16)
BLACK = (0, 0, 0)

# Green light, traffic can go!
sense.clear(GREEN)


# Forever loop
while True:
  # Set all lights to Green
  sense.clear(GREEN)
  sleep(7)
  sense.clear(YELLOW)
  sleep(2)
  sense.clear(RED)
  sleep(10)
