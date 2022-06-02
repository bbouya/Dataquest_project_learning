from email import header
import imp
from requests import head, request

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

# Other Object : 
# Enter your answer here 
response = requests.get('https://api.github.com/repos/octocat/Hello-World', headers=headers)
hello = response.json()

# Pagination # 
param = {'per_page': 50, 'page': 1 }
response = requests.get('https://api.github.com/users/VikParuchuri/starred', headers= headers, params=param)
page1_repos = reponse.json()

new_param = {'per_page': 50, 'page': 2}
response = requests.get('https://api.github.com/users/VikParuchuri/starred', headers = headers, params= new_param)

page2_repos = response.json()

# User level Endpoints:
# Enter your code here: 
response = requests.get('https://api.github.com/users', headers= headers)
user = response.json()

# Post Requests  : 
# Create the data we will pass into the API endpoint, while this endpoint only requires the 'name' key
payload = {'name': 'test'}

# We need to pass in our authentification headers !
response = requests.post('https://api.github.com/user/repos', json = payload, headers=headers)
status_stat = response.status_code
print(status_stat)

# PUT/PATCH requests 
payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)

new_des = {"description":"Learning about requests!","name" : "learning-about-apis"}
new_response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers = headers, json = new_des)
status = new_response.status_code

## 9. DELETE Requests ##

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

response =requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers = headers)
status = response.status_code