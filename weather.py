import requests

location = input('Please type in the location you would like to look up the weather for: ')
key = input('Please enter the API Key for weatherapi.com: ')

request = f"https://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"
response = requests.get(request)

if response.status_code != 200:
    print('Bad response code: ', response.status_code)
    exit(response.status_code)
    
weather_data = response.json()

temp = weather_data['current']['temp_c']
region = weather_data['location']['region']
condition = weather_data['current']['condition']['text']

print(f"The current weather in {location}, region {region}, is {condition}, with a temperature of {temp}")