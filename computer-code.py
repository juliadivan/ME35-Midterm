import paho.mqtt.client as mqtt
import requests

# Replace with your Adafruit IO username, AIO key, and feed names
AIO_USERNAME = 'juliadivan'
AIO_KEY = 'aio_gqdc75VHOnzcXtT11mw60sHizmQM'
FEED_NAME = 'color'

API_KEY = 'keyoGR09SuvJLCt4T'

# Replace with your Airtable base ID
BASE_ID = 'appEjXmQqx3vCE9oC'

# Replace with your Airtable table name
TABLE_NAME = 'ME35'

# Airtable API endpoint URL
url = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

try:
    # Send a GET request to retrieve records from the Airtable table
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        records = data.get('records', [])

        for record in records:
            fields = record.get('fields', {})
            # Process and print the data from each record
            print(fields)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")


# Create an MQTT client and connect to Adafruit IO
client = mqtt.Client()
client.username_pw_set(AIO_USERNAME, AIO_KEY)
client.connect('io.adafruit.com', port=1883)

# Publish data to the Adafruit IO feed
value = str(fields)  # Change this to your desired value
client.publish(f'{AIO_USERNAME}/feeds/{FEED_NAME}', value, qos=1)  # qos=1 for message acknowledgment

# Run the MQTT client loop
client.loop_forever()
