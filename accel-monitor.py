import time
import accel

# Function to read accelerometer data (you may need to replace this with your actual data source)
ac = accel.accelerometer(1, 19, 18)
def read_accelerometer():
    return ac.read_a()
    pass

# Define a threshold for movement detection
threshold = 200

# Read the initial data
initial_data = read_accelerometer()

while True:
    # Read the current data
    current_data = read_accelerometer()

    # Calculate the absolute change for each axis
    changes = [abs(current_data[i] - initial_data[i]) for i in range(3)]
    print(changes)

    # Check if any change exceeds the threshold
    if any(change > threshold for change in changes):
        print("Moved")

    # Update the initial data for the next iteration
    initial_data = current_data

    # Adjust the sleep duration to control the rate of data sampling
    time.sleep(1)  # Sleep for 1 second (adjust as needed)
