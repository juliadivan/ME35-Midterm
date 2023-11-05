import paho.mqtt.client as mqtt
from machine import ADC
import math
from time import sleep

# Replace with your Adafruit IO username, AIO key, and feed name
AIO_USERNAME = 'USERNAME'
AIO_KEY = 'AIOKEY'
FEED_NAME = 'FEEDNAME'

def thermistorTemp(Vout):
    # Voltage Divider
    Vin = 3.3
    Ro = 10000  # 10k Resistor

    # Steinhart Constants
    A = -0.01640849097420107
    B = 0.002962040240708279
    C = -0.000009557056002920398

    # Calculate Resistance
    Rt = (Vout * Ro) / (Vin - Vout) 
    
    # Steinhart - Hart Equation
    TempK = 1 / (A + (B * math.log(Rt)) + C * math.pow(math.log(Rt), 3))

    # Convert from Kelvin to Celsius
    TempC = TempK - 273.15

    return TempC

# Create an MQTT client and connect to Adafruit IO
client = mqtt.MQTTClient('JuliaPico')
client.username_pw_set(AIO_USERNAME, AIO_KEY)
client.connect('io.adafruit.com', port=1883)

adcpin = 26
sensor = ADC(adcpin)

while True:
    adc = sensor.read_u16()
    Vout = (3.3 / 65535) * adc

    TempC = thermistorTemp(Vout)

    # Publish temperature data to the Adafruit IO feed
    client.publish(f'{AIO_USERNAME}/feeds/{FEED_NAME}', str(round(TempC, 1)), qos=1)  # qos=1 for message acknowledgment

    client.loop_start()  # Start the MQTT client loop in the background

    sleep(300)  # Sleep for 5 minutes (300 seconds)
    gc.collect()
