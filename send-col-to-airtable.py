import requests

# Airtable base and API details
base_id = 'BASEID'
table_name = 'ME35'
api_key = 'APIKEY'
record_id = 'RECORDID'  # Remove query parameters

# URL for the Airtable API to update an existing record
url = f'https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Data to send (replace 'your_data' with the string you want to send)
data = {
    'fields': {
        'color': color
    }
}

# Send a PATCH request to update the existing record in the table
response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
    print("Data sent successfully")
else:
    print(f"Failed to update data. Status code: {response.status_code}")
