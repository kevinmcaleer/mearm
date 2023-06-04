import time
import math
import random
from inventorhatmini import InventorHATMini, SERVO_1, SERVO_2, SERVO_3, SERVO_4
from time import sleep
"""
An example of how to move a servo smoothly between random positions.

Press "User" to exit the program.
"""

# Constants
UPDATES = 50            # How many times to update Servos per second
UPDATE_RATE = 1 / UPDATES
TIME_FOR_EACH_MOVE = 2  # The time to travel between each random value
UPDATES_PER_MOVE = TIME_FOR_EACH_MOVE * UPDATES

SERVO_EXTENT = 90       # How far from zero to move the servo

# Create a new InventorHATMini and get a servo from it
board = InventorHATMini(init_leds=False)
base = board.servos[SERVO_1]
arm = board.servos[SERVO_2]
wrist = board.servos[SERVO_3]
grip = board.servos[SERVO_4]

# Get the initial value and create a random end value between the extents
start_value = base.mid_value()
end_value = random.uniform(-SERVO_EXTENT, SERVO_EXTENT)

update = 0

# Sleep until a specific time in the future. Use this instead of time.sleep() to correct for
# inconsistent timings when dealing with complex operations or external communication
def sleep_until(end_time):
    time_to_sleep = end_time - time.monotonic()
    if time_to_sleep > 0.0:
        time.sleep(time_to_sleep)

# Continually move the servo until the user button is pressed
while not board.switch_pressed():

    # Record the start time of this loop
    start_time = time.monotonic()

    # Calculate how far along this movement to be
    percent_along = update / UPDATES_PER_MOVE

    # Move the servo between values using cosine
    base.to_percent(math.cos(percent_along * math.pi), 1.0, -1.0, start_value, end_value)
    
    sleep(0.5)
    arm.to_percent(math.cos(percent_along * math.pi), 1.0, -1.0, start_value, end_value)

    sleep(0.5)
    wrist.to_percent(math.cos(percent_along * math.pi), 1.0, -1.0, start_value, end_value)

    sleep(0.5)
    grip.to_percent(math.cos(percent_along * math.pi), 1.0, -1.0, start_value, end_value)

    # Print out the value the servo is now at
    print("Value = ", round(base.value(), 3), sep="")

    # Move along in time
    update += 1

    # Have we reached the end of this movement?
    if update >= UPDATES_PER_MOVE:
        # Reset the counter
        update = 0

        # Set the start as the last end and create a new random end value
        start_value = end_value
        end_value = random.uniform(-SERVO_EXTENT, SERVO_EXTENT)

    # Sleep until the next update, accounting for how long the above operations took to perform
    sleep_until(start_time + UPDATE_RATE)

# Disable the servos
base.disable()
arm.disable()
wrist.disable()
grip.disable()
