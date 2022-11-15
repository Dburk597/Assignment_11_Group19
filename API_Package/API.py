'''
Name: David Burkhart, Dipshika Mainali 
email: burkhadj@mail.uc.edu, mainalda@mail.uc.edu

Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Calling an API and returning interesting data
Citations:
Anything else that's relevant:

'''

#https://datausa.io/about/api/
#https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=L880w0wT1PxQiDVhgHkZkurg3uvLAqtMfncTCiXA

import json
import requests


response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population') #Calling the Data USA API to get population information
                                                                                             # No API key was needed for this API
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary.

# Here we are printing out the population for the US in the past 5 years

print('In the year ' + str(parsed_json['data'][0]['Year']) + ' the country, ' + parsed_json['data'][0]['Nation'] + ', has a population of ' + str(parsed_json['data'][0]['Population']) + ' people!' )
print('In the year ' + str(parsed_json['data'][1]['Year']) + ' the country, ' + parsed_json['data'][1]['Nation'] + ', has a population of ' + str(parsed_json['data'][1]['Population']) + ' people!' )
print('In the year ' + str(parsed_json['data'][2]['Year']) + ' the country, ' + parsed_json['data'][2]['Nation'] + ', has a population of ' + str(parsed_json['data'][2]['Population']) + ' people!' )
print('In the year ' + str(parsed_json['data'][3]['Year']) + ' the country, ' + parsed_json['data'][3]['Nation'] + ', has a population of ' + str(parsed_json['data'][3]['Population']) + ' people!' )
print('In the year ' + str(parsed_json['data'][4]['Year']) + ' the country, ' + parsed_json['data'][4]['Nation'] + ', has a population of ' + str(parsed_json['data'][4]['Population']) + ' people!' )

 
 
 
 
 
 
 
 
 
 
 
 
 
 
    