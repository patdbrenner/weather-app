import requests
# import json
import os

from emoji import emojize

api_key = os.environ.get("WEATHER_API_KEY")
api_endpoint = "http://api.weatherstack.com/current"



class City:
    def __init__(self, name):
        self.name = name
        self.weather_data = None

    def get_weather(self):
        params = {
            "access_key": api_key,
            "query": self.name,
            "units": "f"
        }
        response = requests.get(api_endpoint, params=params)
        self.weather_data = response.json()
    
    def display_weather(self):
        if "current" in self.weather_data:
            temperature = self.weather_data["current"]["temperature"]
            humidity = self.weather_data["current"]["humidity"]
            description = self.weather_data["current"]["weather_descriptions"][0]


            print(f"City: {self.name}")
            print(f"Temperature: {temperature}°F")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")
        else:
            print("Weather data not available.")

    def update_weather(self):
        self.get_weather()
        self.display_weather()

sf = City("San Francisco")
pa = City("Palo Alto")

def main():
    sf.update_weather()
    pa.update_weather()
    # print(emojize(":sun_with_face:"))

if __name__ == "__main__":
    main()