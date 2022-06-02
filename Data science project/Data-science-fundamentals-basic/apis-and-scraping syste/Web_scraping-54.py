import imp
from requests import request

import requests

## API Authentification : 

# Create a dictionary of headers containing our Authorization header.

headers = {'Authorization': 'token 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'}

# Make a GET request to the Github API with our headers.
# This API endpoint will give us details about Vik Paruhuri : 

reponse = requests.get("https://api.github.com/users/bbouya", headers=headers)

# Print the content of the response, As you can see, this token corresponds to the acount vik
response = requests.get("https://api.github.com/users/bbouya/followers", headers=headers)
orgs = reponse.json()
orgg = response.json()
print(response.json())
print('e')
# Endpoints and Objects ## 
# We have loaded headers in .
