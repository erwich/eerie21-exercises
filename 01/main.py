# Lines starting with # are comments, not code

# Import packages
from time import sleep
from sense_hat import SenseHat

# Link to the external Sense HAT sensor
sense = SenseHat()

# Show a hello message
sense.show_message("Hello, Erie21!")

# Pause
sleep(5)


# Show a goodbye message
