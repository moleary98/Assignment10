# Name: Max O'Leary, Zack Mcquade, Kevin Duritsch
# email: olearymw@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This project demonstrates that we can request and display data from an API
# Citations: https://developer.nrel.gov/docs/api-key/
# Anything else that's relevant:


import json
import requests

# API Key = ImC4H7blVhXRHOaynaEBefET6rfFl3qeBVvwgBc5

response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key=ImC4H7blVhXRHOaynaEBefET6rfFl3qeBVvwgBc5') # Build URL with data request
json_string = response.content # Receive results form server
parsed_json = json.loads(json_string) # Parse results into dictionary
#print(parsed_json)

nameCode = (parsed_json['fuel_stations'][0]['fuel_type_code']) # Gets name code of the fuel station
access = (parsed_json['fuel_stations'][0]['groups_with_access_code']) # Gets the access status of the fuel station
openDate = (parsed_json['fuel_stations'][0]['open_date']) # Gets the opening date of the fuel station
print("Tells us who has access to station: ", access)
print("Name code of the fuel station: ", nameCode)
print("The date the fuel station was opened: ", openDate)
