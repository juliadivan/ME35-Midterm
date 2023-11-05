from servo import ContinuousServo
import time

def slow_flap():
    # Initialize the servo on the specified GPIO pin
    servo = ContinuousServo(15)

    for i in range(5):
        # Move the servo forward (from 0 to 180 degrees)
        servo.set_speed(-20)
        time.sleep(2)  # Adjust the delay for the desired speed

        servo.set_speed(20)
        time.sleep(0.55)  # Adjust the delay for the desired speed

    # Clean up and release resources
    servo.deinit()
