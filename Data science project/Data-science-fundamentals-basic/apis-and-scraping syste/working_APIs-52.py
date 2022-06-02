from email.errors import StartBoundaryNotFoundDefect
from http.client import ResponseNotReady
import requests

### Make a request to get the latest position of the ISS from the OpenNotify API.
response = requests.get('http://api.open-notify.org/iss-now.json')
status_code = response.status_code
print(status_code)
# 200 thats mean the response was oki
## Understanding status codes :
response  = requests.get('http://api.open-notify.org/iss-pass .')
status_code = response.status_code
print(status_code)
# 404 error problem 

# Adding a Query Parameters : 
# Setup the parameters we want to pass to the API 
# This is the latitude and langitude of New York City,
parameters = {'lat': 40.71, 'lon':-70}

# Make a get request with parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response(the data the server returned)
print(response.content)

# This gets the same data as the command above: 
response = requests.get('http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74')
print(response.content)

parameters = {'lat':37.78, 'lon': -122.41}
response = requests.get('http://api.open-notify.org/iss-pass.json', params = parameters)
content = response.content

# Json Format : 
# Make a list of fast food chains

best_food_chains = ['Taco Bell', 'Shake Shake', 'Chipotle']
print(type(best_food_chains))

# Import the JSON library : 
import json

# Use json.dumps to convert best_food_chains to a string: 
best_food_chains_string = json.dumps(best_food_chains)

print(type(best_food_chains_string))
print(best_food_chains)

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary : 
fast_food_franchise = {
    'Subway': 24722,
    'McDonalds': 14098,
    'Starbucks': 10821,
    'Pizza Hut': 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

fast_food_franchise_string_2 = json.loads(fast_food_franchise_string)

print(fast_food_franchise_string_2)

# Getting the same request we did two screens ago.

parameters = {'lat': 37.78, 'lon': -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object, Verify that its a dictionary
json_data = response.json()
print(type(json_data))

first_pass_duration = json_data['response'][0]['duration']

# Content Type : 
# Header is a ditionary : 
print(response.headers)
content_type = response.headers['Content-type']

## Finding the number of people in Space 
# Call the API here 
response = requests.get("http://api.open-notify.org/astros.json")
new = response.json()
in_space_count = new['number']
print(in_space_count)